#!/usr/bin/python
"""
:copyright: (C) ESPEC North America, INC., Paul Nong-Laolam <pnong-laolam@espec.com> 
:license: MIT, see LICENSE for more details.
:date: January 5, 2022
:May 2024: reviewed and reconfirmed Python 3 testing for general use

A simple procedure to perform communication test with the BTZ133 F4 controller.
The following four lines set communication RS232 via a serial COMM port on MS Windows.
F4 is assumed to use a baud rate at 19200 with address 1 (default settings). 

The COM# is dictated by the OS; so check the COM number via the device manager.

MS Windows: COM?           (? = number assigned by MS Windows OS)
DOS command to list COM ports: \> chgport 

GNU/Linux: /dev/ttyUSB?    (? = number (0,1,2) assigned by Linux)
Linux command to list /dev/ttyUSB: $ ls -l /dev/ttyUSB* 

DISCLAIMER: 
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 
"""
import minimalmodbus
# comm port selected from PC selection 
# NOTE: Check the COM no. selected and used by the OS.
#       modify the COM no. to the one used by the OS. 
BTZ133 = minimalmodbus.Instrument("COM5", 1)

# Set baudrate
BTZ133.serial.baudrate = 19200

# set readTemp cmd 
temp = BTZ133.read_register(100, 1, signed=True)
print(f'\nTemp value read from the F4: {temp}\n')