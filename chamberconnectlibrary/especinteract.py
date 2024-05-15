'''
Handle the actual communication with Espec Corp. Controllers
:copyright: (C) Espec North America, INC.
:original author: Myles Metzler
:license: MIT, see LICENSE for more details.

Code modification for Python 3.6+
:author: Paul Nong-Laolam  <pnong-laolam@espec.com>
:date: May 2024 

Tested: 
GNU/Linux platform: Python 3.8.x, 3.9.x, 3.10.x
MS Windows platform: Python 3.9.x 

NOTE: 
The original source code was implemented for Python 2.7.x by Myles Metzler. 
To set this library available for Python 3, the entire set of source code
has been reimplemented to represent and handle byte-string encoding and decoding
scheme.  

Some changes were made within the Python 3 itself and this code as updated 
to reflect those changes. 
'''
#pylint: disable=W0703
import socket
import serial
import time
from chamberconnectlibrary.controllerinterface import ControllerInterfaceError

ERROR_DESCIPTIONS = {
    'CMD ERR':'Unrecognized command',
    'ADDR ERR':'Bad address',
    'CONT NOT READY-1':'Chamber does not support PTCON/Humidity',
    'CONT NOT READY-2':'Chamber is not running a program',
    'CONT NOT READY-3':'Command not supported by this controller',
    'CONT NOT READY-4':'Keys may not be locked while controller is off',
    'CONT NOT READY-5':'Specified time signal is not enabled',
    'DATA NOT READY':'Specified program does not exist',
    'PARA ERR':'Unrecognizable or missing parameter',
    'DATA OUT OF RANGE':'Data not within valid range',
    'PROTECT ON':'Controller data protection is enabled via HMI',
    'PRGM WRITE ERR-1':'Program slot is read-only',
    'PRGM WRITE ERR-2':'Not in program edit/overwrite mode',
    'PRGM WRITE ERR-3':'Edit request not allowed not in edit mode',
    'PRGM WRITE ERR-4':'A program is already being edited',
    'PRGM WRITE ERR-5':'A program is already being edited',
    'PRGM WRITE ERR-6':'Not in overwrite mode',
    'PRGM WRITE ERR-7':'Cannot edit program other than the one in edit mode',
    'PRGM WRITE ERR-8':'Steps must be entered in order',
    'PRGM WRITE ERR-9':'Invalid counter configuration',
    'PRGM WRITE ERR-10':'Cannot edit a running program',
    'PRGM WRITE ERR-11':'Missing data for counter or end mode',
    'PRGM WRITE ERR-12':'Program is being edited on HMI',
    'PRGM WRITE ERR-13':'Invalid step data',
    'PRGM WRITE ERR-14':'Cannot set exposure time while ramp control is on.',
    'PRGM WRITE ERR-15':'Humidity must be enabled for humidity ramp mode',
    'INVALID REQ':'Unsupported function',
    'CHB NOT READY':'Could not act on given command.'
}

class EspecError(ControllerInterfaceError):
    '''
    Generic Espec Corp controller error
    '''
    pass

class EspecSerial(object):
    '''
    Handles low level communication to espec corp controllers via serial (RS232/485)
    '''
    def __init__(self, **kwargs):
        self.address = kwargs.get('address', None)
        self.delimiter = kwargs.get('delimiter', '\r\n')
        self.serial = serial.Serial(
            port=kwargs.get('port'),
            baudrate=kwargs.get('baud', 19200),
            bytesize=kwargs.get('databits', 8),
            parity=kwargs.get('parity', 'N'),
            stopbits=kwargs.get('stopbits', 1),
            timeout=kwargs.get('timeout', 3)
        )

    def __del__(self):
        try:
            self.close()
        except Exception:
            pass

    def close(self):
        '''
        Close the connection the the chamber
        '''
        self.serial.close()

    def interact(self, message):
        '''
        Send a message to the chamber and wait to get its response

        params:
            message: the message to send encoded (str)
        returns:
            byte string: response from the chamber
        raises:
            EspecError
        '''
        if not isinstance(message, (list, tuple)):
            message = [message]
        recvs = []

        for msg in message:
            str_cmd1 = f'{self.address},{msg}{self.delimiter}'
            str_cmd2 = f'{msg}{self.delimiter}'
            
            if self.address:
                self.serial.write(str_cmd1.encode('ascii', 'ignore'))
            else:
                self.serial.write(str_cmd2.encode('ascii', 'ignore'))
            recv = ''.encode('ascii', 'ignore')

            while recv[0-len(self.delimiter):].decode("ascii","ignore") != self.delimiter: 
                rbuff = self.serial.read(1)    # note: str object has no attribute decode 

                if len(rbuff) == 0:
                    raise EspecError('Chamber did not respond in time') 

                recv += rbuff
                #print (f'TYPE of string: {type(recv)}\n   Raw: {recv}\n   Decode: {recv.decode("ascii", "ignore")}')
                
            #if recv.startswith('NA:'):                         # call err msg in response to cmd error 
            if recv.decode("ascii","ignore").startswith('NA:'): # requires decoding... 
                errmsg = recv[3:0-len(self.delimiter)].decode("ascii","ignore")
                descriptErr=ERROR_DESCIPTIONS.get(errmsg, "missing description")
                msg = f'EspecError: command:"{message}" generated Error:"{errmsg}"({descriptErr})'
                raise EspecError(msg)

            recvs.append(recv[:-1*len(self.delimiter)])
        return recvs if len(recvs) > 1 else recvs[0]

class EspecTCP(object):
    '''
    Handles low level communication to espec corp controllers via serial TCP
    '''
    def __init__(self, **kwargs):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setblocking(True)
        self.socket.connect((kwargs.get('host'), kwargs.get('port', 10001)))
        self.address = kwargs.get('address', None)
        self.delimiter = kwargs.get('delimiter', '\r\n')

    def __del__(self):
        try:
            self.close()
        except Exception:
            pass

    def close(self):
        '''
        Close the connection the the chamber
        '''
        self.socket.close()
        time.sleep(0.1)

    def interact(self, message):
        '''
        Send a message to the chamber and get its response

        params:
            message: the message to send (str)
        returns:
            string: response from the chamber
        raises:
            EspecError
        '''
        str_cmd = (f'{message}{self.delimiter}')
        self.socket.send(str_cmd.encode('ascii', 'ignore'))
        recv = ''.encode('ascii', 'ignore') 
        while recv[0-len(self.delimiter):].decode("ascii","ignore") != self.delimiter:
            recv += self.socket.recv(1)

        if recv.decode("ascii","ignore").startswith('NA:'):            
            errmsg = recv[3:0-len(self.delimiter)].decode("ascii","ignore")
            descriptErr=ERROR_DESCIPTIONS.get(errmsg, "missing description")
            msg = f'EspecError: command:"{message}" generated Error:"{errmsg}"({descriptErr})'
            raise EspecError(msg)
        return recv[:-2]
