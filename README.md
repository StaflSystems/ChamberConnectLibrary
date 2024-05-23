# ChamberConnectLibrary (codename: cclibrary-py3) 

Python 3 library for interfacing with ESPEC North America chambers with P300 and P300 w/ vibration, SCP-220, ES-102 Watlow F4T and Watlow F4S/D controllers. 

## Requirements

Python 3.8.x and above is required for using this distributed library. 

This library has been completely tested under the following Python 3 versions: 

* Python 3.8.x
* Python 3.9.x
* Python 3.10.x

Such requirements were due to the use of a print format function for strings, called f-strings, which was added in Python 3.6. 

## Installation

There are two ways to use this distribution: 

1. PyPI
2. src folder

HOWEVER, the PyPI package or the src distribution folder has not yet been published. 

In the meantime, to take advantage of this free library, simply clone it to your local system and git checkout cclibrary-py3. The clone directory must also carry the name ```chamberconnectlibrary```; navigate to this root directory to execute and test run the sample programs provided in the bin directory. 

Sample programs are included in the bin folder. Program names specify the type of controllerfor, for instance, ```f4_runRTU.py``` is a program to control and oeprate a chamber with Watlow F4. With this clone, it is probably best that a virtualenv with specific Python 3 version created in the root directory to test and run these sample programs. This is to avoid any conflict with base Python 3 already exists on your system, unless it was installed specifically for this project. For RTU modbus (serial connect), the ```serial_requirements.txt``` is needed to install the pyserial and/or minimalmodbus modules in this virtualenv. 

Sample programs are available as follows: 

* ```f4t_runTCP.py```: Sample program via TCP/IP for F4T w/ Temp
* ```f4t_runTCP_TempHumi.py```: Sample program via TCP/IP for F4T w/ Temp and Humi
* ```f4t_runRTU.py```: Sample program via RTU Modbus for F4T w/ Temp
* ```f4_runRTU.py```: Sample program via RTU Modbus for F4 w/ Temp
* ```f4_test_read.py```: Sample program to test RTU modbus connection for F4; a quick and small program to test the cable as well as communication settings.  
* ```f4nf4t_sample_run.py```: Sample program with options on F4 RTU, F4T RTU and F4T TCP/IP. A connection to either F4 or F4T via RTU or TCP/IP must be established prior to selecting the option. Default baud rate for F4T is 38400 and F4 9600. It is best to select the one used by the controller. 
* ```p300_rs232.py```: Sample program via serial connect RS232 for both ESPEC P300 and ESPEC SCP-220 w/ Temp and/or Humi. A connection to SCP-220 must be established prior to selecting the option. Default baud rate for P300 is 19200 and SCP-220 9600. 
* ```p300_rs232-direct.py```: Sample program using a direct serial connect via RS232 to a "modified" ESPEC P300 main library (called ```p300serial.py```); this program bypasses the chamberconnectlibrary (espec.py and especinteract.py). ```p300serial.py``` is simply a modified ```p300.py``` to provide a direct connect via RS232. 
* ```espec-ctlr_rs232.py```: Sample program with option to communicate and control ESPEC P300, SCP-220 and ES-102. Vibration features w/ P300 will be reimplemented.  
* ```p300vib_rs232.py```: Sample program to test, control and operate P300 w/ Vibration. 


These and other sample programs may be modified to include different communication interfaces for your application requirements as outlined in the [controllerinterface.md](controllerinterface.md). 

**MS Windows**: To test the above program, navigate to first-level chamberconnectlibrary directory and execute the program as follows:

```python bin/f4t_runTCP.py```

or 

```python bin/f4t_runRTU.py```

**GNU/Linux**: To test the above program, navigate to first-level chamberconnectlibrary (root) directory and execute the program as follows:

```sudo python3 bin/f4t_runTCP.py```

or 

```su -c 'python3 bin/f4t_runTCP.py'```

Accessing TCP/IP or RTU modbus port requires a root privilege in GNU/Linux. The ```sudo``` may be used on a GNU/Linux system for a regular user with sudoer privilege; or, ```su -c``` may be used on a system with regular user to execute the program as root.

A virtualenv is a viable option, again, since all the necessary modules or libraries can be installed and used without interring with the main setup. 
Examples to run the sample programs: 

```sudo venv/bin/python bin/f4nf4t_sample_run.py```

```sudo venv/bin/python bin/p300_rs232-direct.py```

In the venv, double check that ```python``` symbolic links to ```python3```.  

Any questions, contact Paul Nong-Laolam at ESPEC <pnong-laolam@espec.com> for assistance.  

## Documentation

For further documentation on the different communication interface and controller type options, see [controllerinterface.md](controllerinterface.md)
