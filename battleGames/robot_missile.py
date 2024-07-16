#! robot_missle.py
"""A python conversion of the game Robot Missile from Osborne's "Computer Battlegames" from, published 1982."""

import os
import sys
import platform
import string
import random

system = platform.system()

if system == "Windows":
    clear_com = "cls"
else:
    clear_com = "clear"

os.system(clear_com)

num_tries = 4

print("\nROBOT MISSILE\n".center(80))

message = """TYPE THE CPRRECT CODE
LETTER (A-Z) TO DEFUSE THE MISSILE.

YOU HAVE FOUR CHANCES\n"""

print(message)

secret_code = string.ascii_uppercase[random.randint(0, 26)]


for tries in range(num_tries):
    guess = input("Code Letter: ").upper()
    win_msg = False
    if guess == secret_code:
        win_msg = f"\nTHE CORRECT CODE WAS {secret_code}\n"
        win_msg += "TICK...FZZZZ...CLICK\nYOU DID IT\n"
        print(win_msg)
        break
    elif guess < secret_code:
        print("LATER")
    else:
        print("EARLIER")

if not win_msg:
    print(f"YOU BLEW IT\nTHE CORRECT CODE WAS {secret_code}\n")
sys.exit()
