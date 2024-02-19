from nxbt import Nxbt, PRO_CONTROLLER, Buttons
from time import sleep
import macros

nx = Nxbt(debug=False, log_to_file=False)

initial_side = 'LEFT' # left, right
p1 = nx.create_controller(PRO_CONTROLLER, adapter_path='/org/bluez/hci1', reconnect_address='34:2F:BD:D7:E1:EA')
print("waiting for player 1 (target)...")
nx.wait_for_connection(p1)
print("connected to player 1 (target)!")

sleep(0.1)
#input("enter to continue...")

#p2 = nx.create_controller(PRO_CONTROLLER, reconnect_address='DC:68:EB:12:6A:1C')
#print("waiting for player 2...")
#nx.wait_for_connection(p2)
#print("connected to player 2!")
#sleep(0.1)


print("\nstarting script")

sleep(5)

nx.macro(p1, macros.move_down_diagonal_place.format('3', 'LEFT'), block=True)
        # p2: skip turn/discard
#nx.macro(p2, macros.skip_turn)