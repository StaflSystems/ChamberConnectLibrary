'''
:author: Paul Nong-Laolam <pnong-laolam@espec.com>
:license: MIT, see LICENSE for more detail.
:copyright: (c) 2020, 2021. ESPEC North America, INC.
###############################################################
# filename: dictcode.py 
# This function will incorporated into the p300serial.py 
# implementer currently the file will be called by the 
# folloing programs: 
#     call_p300serial.py 
#     p300serial.py 
###############################################################
'''
def dict_code():
    '''define dictionary list
       for the ESPEC P300 error code
       to be returned by each key. 
    '''
    err_code = { 
        'READY-1':'Does not support humidity',
        'READY-2':'No remote program running',
        'READY-3':'Key cannot lock when power is off',
        'READY-4':'Cannot change time signal',
        'READY-5':'No refrigerator',
        'READY-6':'Does not support damper',
        'ERR': 'Command not recognized',
        'ERR-1': 'Requires over write command',
        'ERR-2': 'Not in edit mode',
        'ERR-3': 'Attempting to overwrite in edit mode',
        'ERR-4': 'Attempting to edit in overwrite mode',
        'ERR-5': 'Attempting to overwrite, but not in overwrite mode',
        'ERR-6': 'Writing data to a different program',
        'ERR-7': 'Counter is wrong',
        'ERR-8': 'Skipping step number or out of sequence',
        'ERR-9': 'Cannot edit while program is running.'
    }
    return err_code 
