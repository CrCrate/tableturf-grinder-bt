from nxbt import Nxbt, PRO_CONTROLLER, Buttons
from time import sleep

nx = Nxbt(debug=False, log_to_file=False)

print("init")
# TODO add reconnect (config file?)
# p1 is the target, p2 will skip turns and forfeit

p1 = nx.create_controller(PRO_CONTROLLER, adapter_path='/org/bluez/hci1', reconnect_address='34:2F:BD:D7:E1:EA')
print("waiting for player 1 (target)...")
nx.wait_for_connection(p1)
print("connected to player 1 (target)!")

sleep(0.1)
#input("enter to continue...")

p2 = nx.create_controller(PRO_CONTROLLER, reconnect_address='DC:68:EB:12:6A:1C')
print("waiting for player 2...")
nx.wait_for_connection(p2)
print("connected to player 2!")
sleep(2)


print("\nstarting script")

nx.press_buttons(p1, [Buttons.DPAD_DOWN])
nx.press_buttons(p2, [Buttons.DPAD_DOWN])
sleep(2)
