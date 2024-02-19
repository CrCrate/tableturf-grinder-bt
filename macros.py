# 0.045s per cycle (in theory)
# every other frame despite supposedly frame perfect?
move_up_place = """
LOOP {}
    DPAD_UP A 0.016s
    0.016s
"""
move_up_place_OLD = """
LOOP {}
    DPAD_UP 0.02s
    A 0.02s
    0.005s
"""


move_down_diagonal_place = """
0.003s
A 0.02s
LOOP {}
    DPAD_DOWN DPAD_{} 0.016s
    A 0.016s
"""

move_horizontal_place = """
LOOP {}
    DPAD_{} A 0.016s
    0.016s
"""

move_up_diagonal_place = """
LOOP {}
    DPAD_UP DPAD_{} 0.016s
    A 0.016s
"""

move_down_diagonal_place_OLD = """
0.003s
A 0.02s
LOOP {}
    0.003s
    DPAD_DOWN 0.03s
    DPAD_{} 0.02s
    A 0.02s
"""

move_horizontal_place_OLD = """
LOOP {}
    DPAD_{} 0.02s
    A 0.02s
"""

move_up_diagonal_place_OLD = """
LOOP {}
    DPAD_UP 0.02s
    DPAD_{} 0.02s
    A 0.02s
"""
# 1.03s (without dropped inputs)
skip_turn = """
0.03s
DPAD_UP 0.1s
0.1s
A 0.1s
0.6s
A 0.1s
0.04s
A 0.1s
0.1s
B 0.02s
6s
"""

forfeit = """
0.005s
PLUS 0.016s
0.016s
PLUS 0.03s
0.03s
PLUS 0.03s
0.35s
DPAD_RIGHT 0.03s
0.6s
A 0.03s
1.3s
"""

# hits A twice in 0.1s N amount of times
mash_a = """
LOOP {}
    A 0.03s
    0.02s
    A 0.03s
    0.02s
"""