move_up_place = """
LOOP {}
    DPAD_UP 0.02s
    A 0.02s
    0.005s
"""

move_down_diagonal_place = """
LOOP {}
    DPAD_DOWN 0.02s
    DPAD_{} 0.02s
    A 0.02s
"""

move_horizontal_place = """
LOOP {}
    DPAD_{} 0.03s
    A 0.02s
"""

move_up_diagonal_place = """
LOOP {}
    DPAD_UP 0.02s
    DPAD_{} 0.02s
    A 0.02s
"""

skip_turn = """
DPAD_UP 0.03s
0.1s
A 0.03s
0.6s
A 0.03s
"""

forfeit = """
PLUS 0.03s
0.4s
DPAD_RIGHT 0.03s
0.6s
A 0.03s
1.1s
"""