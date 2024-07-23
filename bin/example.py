'''
examples of using the chamberconnectlibrary
'''
import pprint
import time
import signal

from chamberconnectlibrary.watlowf4t import WatlowF4T
from chamberconnectlibrary.watlowf4 import WatlowF4
from chamberconnectlibrary.espec import Espec

LOOP_NAMES = ['Temperature', 'Humidity']

# CONTROLLER = Espec(
#     interface='Serial',
#     serialport='//./COM10',
#     baudrate=19200,
#     loop_names=LOOP_NAMES
# )
# CONTROLLER = WatlowF4(
#     interface='RTU',
#     serialport='//./COM7',
#     baudrate=19200,
#     loop_names=LOOP_NAMES
# )
CONTROLLER = WatlowF4T(
    interface='TCP',
    host='10.10.1.205',
    loop_names=LOOP_NAMES
)
# CONTROLLER = WatlowF4T(
#     interface='RTU',
#     serialport='//./COM4',
#     baudrate=38400,
#     loop_names=LOOP_NAMES
# )
print CONTROLLER.process_controller()

# print '\ncascade loops:'
# for i in range(CONTROLLER.cascades):
#     print CONTROLLER.get_loop(i+1, 'cascade', ['processvalue', 'setpoint'])

# print '\nloops:'
# for i in range(CONTROLLER.loops):
#     print CONTROLLER.get_loop(i+1, 'loop', 'processvalue', 'setpoint')

# print '\nnamed loops:'
# for name in LOOP_NAMES:
#     print CONTROLLER.get_loop(name, ['processvalue', 'setpoint'])

# for name in LOOP_NAMES:
#     print CONTROLLER.set_loop(name, setpoint=60.0)

# print '\noperations:'
# print CONTROLLER.get_operation()
# CONTROLLER.set_operation('standby')

# print '\nEvents:'
# for i in range(8):
#     print CONTROLLER.get_event(i+1)

running = True



file = open('data.csv', 'w+', 0)
file.write('timestamp,temperature setpoint (C),temperature current (C),humidity setpoint (%RH),humidity current (%RH)\n')

def signal_handler(signal, frame):
    global running
    running = False

signal.signal(signal.SIGINT, signal_handler)

while running:
    stm = time.time()
    lookup = {'cascade':[], 'loop':[]}
    lookup['loop'].append({'name':'Temperature', 'id': 1, 'number': 1})
    lookup['loop'].append({'name':'Humidity', 'id': 2, 'number': 2})
    params = {'get_loops':True, 'get_status':True, 'get_alarms':True, 'get_program_status':True, 'get_program_list':False, 'get_refrig':True}
    params['get_events'] = [{'N':i+1, 'name':'TS#%d'%(i+1)} for i in range(8)]
    smpl = CONTROLLER.sample(lookup, **params)
    
    pprint.pprint(smpl)

    if len(smpl['loops']) < 2:
        continue

    print(",")
    file.write("%s,%s,%s,%s,%s\n" % (time.strftime('%Y-%m-%d %H:%M:%S'), smpl['loops'][0]['setpoint']['current'], smpl['loops'][0]['processvalue']['air'], smpl['loops'][1]['setpoint']['current'], smpl['loops'][1]['processvalue']['air']))

file.close()
CONTROLLER.close()
