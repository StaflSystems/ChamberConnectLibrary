#!/usr/bin/python3
'''
:author: Paul Nong-Laolam <pnong-laolam@espec.com>
:license: MIT, see LICENSE for more detail.
:copyright: (c) 2020, 2021. ESPEC North America, INC.
:file: p300rs_sample_run.py 
:date: March 2022
:updated: May 2024
--------------------------------------------------------------------------
README:
====== 

Application interface for controlling ESPEC P300 operations. 
This program may be and can be reimplemented with additional
call methods to utilize the P300 operation modes from its 
class and method definitions. 

The program has been modified from its original code that made use of
the original call methods from chamberconenctlibrary file p300.py. 
To make is easy and accessible, this file has been modified 
and palced under a new filename (p300serial.py) to provide a 
direct call to each methods. The ESPEC P300 library has been 
extracted, modified and formalized to support all the available features. 

The following is a simple sample call program to serve as a starting 
point on how to utilize our ESPEC P300 library. Programmer can implement
or/and modified to include more complex call methods for their 
specific application.  
--------------------------------------------------------------------------

How to Determine Communication Port: 
===================================

MS Windows: COM? How to determine COM number assigned by MS Windows OS.
DOS command to list COM ports: \> chgport

GNU/Linux: /dev/ttyUSB? How to determine USB number assigned by Linux. 
Linux command to list /dev/ttyUSB: $ ls -l /dev/ttyUSB* 

How to find COM or USB number: 
1. apply the cmd before plugging in the cable; study the list
2. plug in the cable, apply the cmd again and study the list
3. the new USB or COM port listed will be the one to use in the program 

Tested: 
GNU/Linux platform: Python 3.8.x, 3.9.x, 3.10.x
MS Windows platform: Python 3.9.x 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
'''
import time
import serial
import os, sys
import re
import logging
sys.path.insert(0,'../chamberconnectlibrary')

from chamberconnectlibrary.p300serial import EspecP300
from chamberconnectlibrary.dictcode import dict_code

def get_status():
    '''read parameters from chamber/controller
    
    this is a general method for reading a type of chamber
    operating values (status). 

    Examples: 
    To read temperature value, modify the try statment as:
    get_val = p300.read_temp() 

    To read vibration value, modify the try statment as:
    get_val = p300.read_vib() 

    To read ROM value, modify the try statment as:
    get_val = p300.read_rom() 

    To read 'product temperature control' value (PTC value), modify the try statment as:
    get_val = p300.read_constant_ptc() 

    To read alarm, set it as: 
    get_val = p300.read_alarm() 
    '''
    try:
        get_val = p300.read_temp()
    except Exception as e: 
        get_val = e 
    return get_val 

def get_mon():
    '''read MON value'''
    try: 
        mon_val = p300.read_mon()
    except: 
        mon_val = "reading failed..."
    return mon_val 

def main():
    '''main driver program'''
    print (f'Temp Status:\n {get_status()}')

if __name__ == '__main__':
    '''set up low-level communication with ESPEC P300 via RS232C
       call to the main definition to start the sample program. 
    '''
    os.system('clear||cls')
    p300=EspecP300()
    p300.open()
    main()
    p300.close()