from nxbt import Nxbt, PRO_CONTROLLER, Buttons
from time import sleep

nx = Nxbt(debug=False, log_to_file=False)

frame_interval = 0.05

L_spam = """
LOOP 1000
    ZR 0.02s
    L 0.02s

"""
p1 = nx.create_controller(PRO_CONTROLLER, adapter_path='/org/bluez/hci1', reconnect_address='34:2F:BD:D7:E1:EA')
print("waiting for player 1 (target)...")
nx.wait_for_connection(p1)
print("connected to player 1 (target)!")

sleep(3)
print('starting')

nx.macro(p1, L_spam)

"""
while True:
    nx.press_buttons(p1, [Buttons.ZR], down=0.02, up=0, block=True)
    nx.press_buttons(p1, [Buttons.L], down=0.02, up=0, block=True)
"""

sleep(2)
