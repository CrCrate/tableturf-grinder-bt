move_up_place = """
LOOP {}
    DPAD_UP A 0.02
    0.02
"""

move_down_diagonal_place = """
LOOP {}
    DPAD_DOWN 0.02
    DPAD_{} A 0.02
"""

move_horizontal_place = """
LOOP {}
    DPAD_{} A 0.02
    0.02
"""

move_up_diagonal_place = """
LOOP {}
    DPAD_UP 0.02
    DPAD_{} A 0.02
"""
