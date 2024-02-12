from nxbt import Nxbt, PRO_CONTROLLER, Buttons
from time import sleep

nx = Nxbt(debug=False, log_to_file=False)

initial_side = 'left' # left, right


game_counter = 0

last_side = ''
if initial_side == 'left': last_side = 'right'
else: last_side = 'left'

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
sleep(0.1)


print("\nstarting script")

sleep(5)

print('initiating battle...')

# battle init
nx.press_buttons(p1, [Buttons.A]) #seat
sleep(2)
nx.press_buttons(p2, [Buttons.A]) #challange
sleep(1)
nx.press_buttons(p1, [Buttons.A]) #accept chal

sleep(6.5) ###DEC


# TODO try block=false for rapid inputs?
# TODO try premade full macros -||- instead of loops?
# main gameplay loop
while True:
    print(f"\nSTARTING GAME {game_counter}\n")

    print('setup...')
    # start setup
    nx.press_buttons(p1, [Buttons.A]) #map sel
    sleep(0.6)
    nx.press_buttons(p1, [Buttons.A]) #deck sel
    nx.press_buttons(p2, [Buttons.A])

    print('waiting for game to start...')
    sleep(8.5)

    print('go time')

    nx.press_buttons(p1, [Buttons.A]) #do not reshuffle
    nx.press_buttons(p2, [Buttons.A])
    sleep(2)

    # gameplay
    ## p1: all the way down, all the way left/right (alternate), first placable spot moving up
    ## p2: skip: UP A A
    for x in range(7):
        print(f'round {x}...')

        nx.press_buttons(p1, [Buttons.A]) #p1 select card
        #sleep(0.3)
        # p1: position card at the bottom + preplace if applicable
        if x <= 1: # first two cards (bottom row, below starting point)
            if last_side == 'right':
                for x in range(3): 
                    nx.press_buttons(p1, [Buttons.DPAD_DOWN], down=0.03, up=0.0)
                    nx.press_buttons(p1, [Buttons.DPAD_LEFT, Buttons.A], down=0.03, up=0.02)
                last_side = 'left'
            else:
                for x in range(3): 
                    nx.press_buttons(p1, [Buttons.DPAD_DOWN], down=0.03, up=0.0)
                    nx.press_buttons(p1, [Buttons.DPAD_RIGHT, Buttons.A], down=0.03, up=0.02)
                last_side = 'right'

            # p1: place card as low as possible 
            for x in range(10):
                nx.press_buttons(p1, [Buttons.DPAD_UP, Buttons.A], down=0.03, up=0)
                sleep(0.02)

        elif x <= 3: # next two 
            if last_side == 'right':
                sleep(0.05)
                for x in range(3): 
                    nx.press_buttons(p1, [Buttons.DPAD_LEFT, Buttons.A], down=0.03, up=0.03)
                last_side = 'left'
            else:
                for x in range(3): 
                    nx.press_buttons(p1, [Buttons.DPAD_RIGHT, Buttons.A], down=0.03, up=0.03)
                last_side = 'right'

            # p1: place card as low as possible 
            for x in range(13):
                nx.press_buttons(p1, [Buttons.DPAD_UP, Buttons.A], down=0.03, up=0)
                sleep(0.02)        
        else: # last four
            if last_side == 'right':
                for x in range(3): 
                    nx.press_buttons(p1, [Buttons.DPAD_LEFT, Buttons.DPAD_UP, Buttons.A], down=0.03, up=0.02)
                last_side = 'left'
            else:
                for x in range(3): 
                    nx.press_buttons(p1, [Buttons.DPAD_RIGHT, Buttons.DPAD_UP, Buttons.A], down=0.03, up=0.02)
                last_side = 'right'

            # p1: place card as low as possible 
            for x in range(16):
                nx.press_buttons(p1, [Buttons.DPAD_UP, Buttons.A], down=0.03, up=0)
                sleep(0.02)
        print('p1 done')

        sleep(0.1)
        # p2: skip turn/discard
        nx.press_buttons(p2, [Buttons.DPAD_UP])
        sleep(0.1)
        nx.press_buttons(p2, [Buttons.A], down=0.05, up=0.1)
        sleep(0.2)
        nx.press_buttons(p2, [Buttons.A], down=0.05)

        sleep(6.5) 

    print('forfeiting...')
    sleep(0.02)
    # forfeit and restart
    nx.press_buttons(p2, [Buttons.PLUS], down=0.03)
    sleep(0.3)
    nx.press_buttons(p2, [Buttons.DPAD_RIGHT], down=0.03)
    sleep(0.5)
    nx.press_buttons(p2, [Buttons.A], down=0.03)
    sleep(1)
    #giveup dialog
    nx.press_buttons(p1, [Buttons.A], down=0.03, up=0)
    nx.press_buttons(p2, [Buttons.A], down=0.03)
    sleep(6)
    #result screen
    nx.press_buttons(p1, [Buttons.A], down=0.03, up=0)
    nx.press_buttons(p2, [Buttons.A], down=0.03)
    sleep(3)
    # playagain
    nx.press_buttons(p1, [Buttons.A], down=0.03)
    sleep(0.1)
    nx.press_buttons(p2, [Buttons.A], down=0.03)

    sleep(2.1)
    game_counter += 1
