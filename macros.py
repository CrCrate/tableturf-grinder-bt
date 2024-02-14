move_up_place = """
LOOP {}
    DPAD_UP 0.02s
    A 0.02s
    0.005s
"""

move_down_diagonal_place = """
LOOP {}
    0.003s
    DPAD_DOWN 0.03s
    DPAD_{} 0.02s
    A 0.02s
"""

move_horizontal_place = """
LOOP {}
    DPAD_{} 0.02s
    A 0.02s
"""

move_up_diagonal_place = """
LOOP {}
    DPAD_UP 0.02s
    DPAD_{} 0.02s
    A 0.02s
"""

skip_turn = """
0.005s
DPAD_UP 0.03s
0.1s
A 0.03s
0.7s
A 0.04s
0.005s
"""

forfeit = """
0.005s
PLUS 0.03s
0.4s
DPAD_RIGHT 0.03s
0.6s
A 0.03s
1.3s
"""