#!Python
"""A python conversion of the game 'Intergalagtic Games from Osborne's "Computer Spacegames", published 1982."""

import os
import sys
import platform
import random
import numpy as np


if platform.system == "Windows":
    os.system("cls")
else:
    os.system("clear")

HEIGHT = random.randint(1, 100)

print("INTERGALACTIC GAMES")

instructions = f"""
YOU MUST LAUNCH A SATELLITE
TO A HEIGHT OF {HEIGHT}
"""
print(instructions)

for attempts in range(8):
    angle = int(input("ENTER ANGLE (0-90)\n> "))
    velocity = int(input("ENTER SPEED (0-40000)\n> "))

    angle = angle - np.arctan(HEIGHT / 3) * (180 / 3.14159)

    velocity = velocity - (3000 * np.sqrt(HEIGHT + (1 / HEIGHT)))

    if np.abs(angle) < 2 and np.abs(velocity) < 100:
        print("YOU'VE DONE IT\nNCTV WINS-THANKS TO YOU")
        sys.exit()

    if angle < -2:
        print("\nTOO SHALLOW")
    elif angle > 2:
        print("\nTOO STEEP")
    elif np.abs(angle) < 2:
        print("ANGLE LOOKS GOOD")

    if velocity < -100:
        print("TOO SLOW")
    elif velocity > 100:
        print("TOO FAST")
    elif np.abs(velocity) < 100:
        print("SPEED LOOKS GOOD")
    print()

print("YOU'VE FAILED\nYOU'RE FIRED")
sys.exit()
