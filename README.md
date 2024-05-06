# ChamberConnectLibrary

Python library for interfacing with ESPEC North America chambers with P300, SCP-220, Watlow F4T and Watlow F4S/D controllers. 

## Requirements

Python 3.8.x and above is required for using this distributed library. 

This library has been completely tested under the following Python 3 versions: 

* Python 3.8.x
* Python 3.9.x
* Python 3.10.x

Such requirements were due to the use of new print function calls. 

## Installation

There are two ways to use this distribution: (1) PyPI and (2) src folder. HOWEVER, the PyPI package or the src distribution folder has not yet been published. 
In the meantime, to take advantage of this free library, simply clone it to your local system and git checkout py3-chamberconnectlibrary. Then navigate to the root directory to execute and test run the sample programs provided as a starter. 

Sample programs are included in the bin folder, particularly for Watlow F4 and F4T controllers. A virtualenv with specific Python 3 version can be created in the root directory to test and run these sample programs. For RTU modbus (serial connect), the ``serial_requirements.txt``` is needed to install the pyserial and/or minimalmodbus modules. 

* ```f4t_runTCP.py```: Sample program via TCP/IP for F4T w/ Temp
* ```f4t_runTCP_TempHumi.py```: Sample program via TCP/IP for F4T w/ Temp and Humi
* ```f4t_runRTU.py```: Sample program via RTU Modbus for F4T w/ Temp
* ```f4_runRTU.py```: Sample program via RTU Modbus for F4 w/ Temp
* ```f4_test_read.py```: Sample program to test RTU modbus connection for F4 
* ```f4nf4t_sample_run.py```: Sample program with options on F4 RTU, F4T RTU and F4T TCP/IP 

These and other sample programs may be modified to include different communication interfaces for your application requirements as outlined in the [controllerinterface.md](controllerinterface.md). 

**MS Windows**: To test the above program, navigate to first-level chamberconnectlibrary directory and execute the program as follows:

```python bin/f4t_runTCP.py```

or 

```python bin/f4t_runRTU.py```

**GNU/Linux**: To test the above program, navigate to first-level chamberconnectlibrary directory and execute the program as follows:

```sudo python3 bin/f4t_runTCP.py```

or 

```su -c 'python3 bin/f4t_runTCP.py'```

Accessing TCP/IP or RTU modbus port requires a root privilege in GNU/Linux. The ```sudo``` may be used on a GNU/Linux system for a regular user with sudoer privilege; or, ```su -c``` may be used on a system with regular user to execute the program as root. 

Any questions, contact Paul Nong-Laolam at ESPEC <pnong-laolam@espec.com> for assistance.  

## Documentation

For further docuemntation on the different communication interface and controller type options, see [controllerinterface.md](controllerinterface.md)
