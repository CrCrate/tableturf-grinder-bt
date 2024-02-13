from nxbt import Nxbt, PRO_CONTROLLER, Buttons
from time import sleep
import macros

nx = Nxbt(debug=False, log_to_file=False)

initial_side = 'LEFT' # left, right

game_counter = 0
next_side = initial_side

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
    sleep(0.7)
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
        sleep(0.05)
        # p1: position card at the bottom + preplace if applicable
        if x <= 1: # first two cards (bottom row, below starting point)
            nx.macro(p1, macros.move_down_diagonal_place.format('3', next_side))

            if next_side == 'RIGHT':
                next_side = 'LEFT'
            else:
                next_side = 'RIGHT'

            # p1: place card as low as possible 
            nx.macro(p1, macros.move_up_place.format('10'))

        elif x <= 3: # next two 
            nx.macro(p1, macros.move_horizontal_place.format('3', next_side))

            if next_side == 'RIGHT':
                next_side = 'LEFT'
            else:
                next_side = 'RIGHT'

            # p1: place card as low as possible     
            nx.macro(p1, macros.move_up_place.format('14'))  

        else: # last four
            nx.macro(p1, macros.move_up_diagonal_place.format('3', next_side))
            if next_side == 'RIGHT':
                next_side = 'LEFT'
            else:
                next_side = 'RIGHT'

            # p1: place card as low as possible 
            nx.macro(p1, macros.move_up_place.format('17'))
        print('p1 done')

        sleep(0.1)
        # p2: skip turn/discard
        nx.macro(p2, macros.skip_turn)

        sleep(7) 

    print('forfeiting...')
    sleep(0.02)
    # forfeit and restart
    nx.macro(p2, macros.forfeit)
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
