# What is new in this cclibrary-py3. 

Python 3 library for interfacing with ESPEC North America chambers with P300 with vibration features, SCP-220, ES-102 Watlow F4T and Watlow F4S/D controllers.

This library attemps to cover and support the complete list of ESPEC controllers: P300, P300 with vibration, SCP-220 and ES-102, include Watlow F4/T. 

The only difference between this and ```py3-chamberconenctlibrary``` is the inclusion of P300 vibration features and ES-102. 

Date of implementation and updates: 

May 15, 2024: 

- Implementation initiated; P300 vibration and ES-102 have not yet been completeley converted to support Python 3.
- Sampe programs in the bin directory were added to support general application except P300 vibration and ES-102. 


## Requirements

Python 3.8.x and above is required for using this distributed library. 

This library has been completely tested under the following Python 3 versions: 

* Python 3.8.x
* Python 3.9.x
* Python 3.10.x

Such requirements were due to the use of new print function calls. 