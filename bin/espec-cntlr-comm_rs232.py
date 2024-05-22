#!/usr/bin/python3
'''
:author: Paul Nong-Laolam <pnong-laolam@espec.com>
:license: MIT, see LICENSE for more detail.
:copyright: (c) 2020. ESPEC North America, Inc.
:filename: espec-cntlr-comm_rs232.py 

This simple program is provided for testing communication with ESPEC
P300, SCP-220 and/or ES-102 via RS232C communication interface. Once
communication is established commands for P300, SCP-220 or ES-102 may
be used to communicate and control the controller operation via this
command-line interface. This technique provides the quickest and
cleanest way to communicate with your controller via a simple 
Python 3 program in place of a tool such as PuTTY or termite. 
 
ESPEC P300/SCP-220/ES-102 serial communication protocol via RS232 to USB has 
the following configuration parameters:

    baudrate:  19200       (for P300; 9600 for SCP-220 and ES-102) 
    port: /dev/ttyUSB0     (on GNU/Linux; COM? where ? is a number)
    port: //./COM?         (on MS Windows where ? is a number used by the OS)
    bytesize=8, 
    parity='N', 
    stopbits=1, 
    timeout=3

This program connects to ESPEC P300/SCP-220 or ES-102 for control and operation. 
It allows a direct communication with the controller via its native text command. 
Refer to the communication/command manual for the respective controller. 

DISCLAIMER: 
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 
'''
import time
import os
import serial

def open_com():
    '''open communication port'''
    CONTROLLER.isOpen()

def close():
    '''close communication port'''
    try:
        CONTROLLER.close()
        exit()
    except Exception:
        pass

def options():
    '''list of chamber/controller options'''
    print ("""This program connects to ESPEC controller P300, \n"""
    + """SCP-220 or ES-102 directly via RS232 communication \n"""
    + """interface to allow programmers to issue commands \n"""
    + """to control and operate the target controller.""")
    print ("\nChamber/Controller Selection:\n"
           "==================================\n"
           "0. ESPEC ES-102 via RS232\n"
           "1. ESPEC SCP-220 via RS232\n"
           "2. ESPEC P300 via via RS232\n"
           "==================================")

def cmd_rsp():
    '''controller command and response'''
    print('Enter command at the command prompt.\n')
    cmd=1
    while 1:
        cmd = input('[Enter cmd ("exit" to quit) ] >> ') 
        if cmd == 'exit': close()   
        else:
            CONTROLLER.write((cmd + '\r\n').encode()) # requires \r\n carriage return & line feed    
            rsp = ''.encode()                         # if response is null
            time.sleep(1)                             # wait 1 second for controller to respond
            while CONTROLLER.inWaiting() > 0:
                rsp += CONTROLLER.read(1)             # build string of response from controller
                        
            if rsp != ''.encode():
                # decode and print the response data: rsp 
                response = rsp.decode('utf-8', 'replace')
                print(f'[Response ]: {response}')                 
            else:
                print ('No response from device. Check cable or controller option. \n') 

def main():
    '''start main program'''
    open_com()
    cmd_rsp() 

if __name__ == '__main__':
    '''
    set up low-level communication with ESPEC P300, SCP-220 
    and ES-102 via RS232C
    '''
    os.system('clear||cls')
    SELECT_OPT = 0

    options() 
    while True:
        try:
            SELECT_OPT = int(input("Make Selection (0, 1, 2): "))
        except ValueError:
            print("Invalid number. Try again.")
            continue
        else:
            # SELECT_OPT = 0 for ES102 RTU SERIAL INTERFACE 
            if SELECT_OPT == 0:
                baudrate_spd = 9600
                print ("\nESPEC ES-102 CONTROLLER via RS232:")

            elif SELECT_OPT == 1:
            # SELECT_OPT = 1 for SCP220 via RS232 INTERFACE 
                baudrate_spd = 9600
                print ("\nESPEC SCP-220 CONTROLLER via RS232:")
            
            elif SELECT_OPT == 2:
            # SELECT_OPT = 1 for P300 via RTU SERIAL 
                baudrate_spd = 19200 
                print ("\nESPEC P300 CONTROLLER via VIA RS232:")     
            else: 
                print ("Number out of range. Try again.") 
                continue  
            break 

    CONTROLLER = serial.Serial( 
        port='/dev/ttyUSB0',    # set '//./COM?' for MS Windows 
                                # set '/dev/ttyUSB?' for GNU/Linux 
        baudrate=baudrate_spd,  # 19200:P300; 9600:ES102,SCP220 
        bytesize=8, 
        parity='N', 
        stopbits=1, 
        timeout=3               # apply 3-second time-out 
    )
    main()