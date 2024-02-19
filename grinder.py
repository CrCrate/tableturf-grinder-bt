from nxbt import Nxbt, PRO_CONTROLLER, Buttons
from time import sleep
import macros

nx = Nxbt(debug=False, log_to_file=False)

initial_side = 'LEFT' # left, right

game_counter = 0


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

sleep(6) ###DEC
print('mashing initial setup...')
nx.macro(p1, macros.mash_a.format('55'), block=False)
print('...cont')
nx.macro(p2, macros.mash_a.format('55'))
# TODO increase amount of multitasked moveup/skip
# TODO ADD interrupt for p2 to get out of equip
# main gameplay loop
while True:
    print(f"\nSTARTING GAME {game_counter}\n")
    nx.press_buttons(p1, [Buttons.ZR], down=0.5, up=0.5)
    
    # start setup
    #nx.press_buttons(p1, [Buttons.A]) #map sel
    #nx.press_buttons(p1, [Buttons.A], up=0.7) #repeat incase of missed input
    #sleep(0.6)
    #nx.press_buttons(p1, [Buttons.A], block=False) #deck sel
    #nx.press_buttons(p2, [Buttons.A], up=0.3)
    #sleep(0.2)
    #print('waiting for game to start...')
    #nx.press_buttons(p1, [Buttons.A], block=False) # repeat for misinput
    #nx.press_buttons(p2, [Buttons.A], up=8.3)
    
    #sleep(8.1)

    print('go time')

    #nx.press_buttons(p1, [Buttons.A], block=False) #do not reshuffle
    #nx.press_buttons(p2, [Buttons.A], block=False)
    #nx.press_buttons(p1, [Buttons.A], block=False) #do not reshuffle
    #nx.press_buttons(p2, [Buttons.A], up=1.7) ###DEC
    #sleep(2)

    next_side = initial_side
    # gameplay
    ## p1: all the way down, all the way left/right (alternate), first placable spot moving up
    ## p2: skip: UP A A
    for x in range(6):
        print(f'round {x}...')
        

        nx.press_buttons(p1, [Buttons.A]) #p1 select card
        #sleep(0.05)
        # p1: position card at the bottom + preplace if applicable
        if x == 0:
            nx.macro(p1, macros.move_down_diagonal_place.format('3', next_side), block=False)

            if next_side == 'RIGHT':
                next_side = 'LEFT'
            else:
                next_side = 'RIGHT'
        elif x <= 1: # first two cards (bottom row, below starting point)
            nx.macro(p1, macros.move_down_diagonal_place.format('3', next_side))

            if next_side == 'RIGHT':
                next_side = 'LEFT'
            else:
                next_side = 'RIGHT'

            # p1: place card as low as possible
            # we can skip this on the first turn as the recommended deck will always place first card
            #if x == 1: nx.macro(p1, macros.move_up_place.format('7'))

        #elif x <= 3: # next two 
        elif x == 99:
            nx.macro(p1, macros.move_horizontal_place.format('3', next_side))

            if next_side == 'RIGHT':
                next_side = 'LEFT'
            else:
                next_side = 'RIGHT'

            # p1: place card as low as possible     
            nx.macro(p1, macros.move_up_place_OLD.format('4'))  

        else: # last three
            nx.macro(p1, macros.move_up_diagonal_place.format('3', next_side))
            if next_side == 'RIGHT':
                next_side = 'LEFT'
            else:
                next_side = 'RIGHT'

            # p1: place card as low as possible 
            nx.macro(p1, macros.move_up_place_OLD.format('5'))
        print('skipping...')

        if x != 0: nx.macro(p1, macros.move_up_place_OLD.format('9'), block=False)
        # p2: skip turn/discard
        nx.macro(p2, macros.skip_turn)
        #nx.press_buttons(p2, [Buttons.B], up=6.4) #incase of issue
        #sleep(6.7) 

    print('forfeiting...')
    #sleep(0.02)
    # forfeit and restart
    nx.macro(p2, macros.forfeit)

    print('mashing endscreen/setup...')
    #skip all following dialogues and setup
    nx.macro(p2, macros.mash_a.format('106'), block=False)
    print('...cont')
    nx.macro(p1, macros.mash_a.format('106'))
    #giveup dialog
    #nx.press_buttons(p2, [Buttons.A], down=0.03)
    #nx.press_buttons(p1, [Buttons.A], down=0.03, up=5.8)
    #sleep(5.7)
    #result screen
    #nx.press_buttons(p1, [Buttons.A], down=0.03, block=False)
    #nx.press_buttons(p2, [Buttons.A], down=0.03, up=3.2)
    #sleep(3.1)
    # playagain
    #nx.press_buttons(p1, [Buttons.A], down=0.03, block=False)
    #nx.press_buttons(p2, [Buttons.A], down=0.03, up=2.6) 
    #sleep(2.5)
    game_counter += 1
