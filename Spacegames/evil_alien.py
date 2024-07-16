#!Python
"""A python conversion of the game 'Evil Alien' from Osborne's 'Computer Spacegames', published 1982."""

import os
import platform
import itertools
import random
from time import sleep


if platform.system == "Windows":
    os.system("cls")
else:
    os.system("clear")

messages = [
    ["EVIL ALIEN: THE SPACE GAME"],
    [
        "SOMEWHERE BENEATH YOU, IN DEEPEST, BLACKEST SPACE, LURKS ELRON, THE EVIL ALIEN.",
    ],
    [
        "YOU HAVE MANAGED TO DEACTIVATE ALL BUT HIS SHORT RANGED WEAPONS,",
        "BUT HE CAN STILL MAKE HIS SHIP INVISIBLE.",
    ],
    [
        "YOU KNOW HE IS SOMEWHERE WITHIN THE THREE-DIMENSIONAL GRID YOU CAN",
        "SEE ON YOUR SHIP'S SCREEN,",
    ],
    ["BUT WHERE?"],
    [
        "YOU HAVE FOUR SPACE BOMBS.",
        "EACH ONE CAN BE EXPLODED AT A POSITION IN THE GRID SPECIFIED BY THREE",
        "NUMBERS BETWEEN 0 AND 9.",
    ],
    [
        "CAN YOU BLAST THE EVIL ELRON OUT OF SPACE BEFORE HE CREEPS UP AND",
        "CAPTURES YOU?",
    ],
]

# message = "\n".join(messages)
# for lines in messages:
#     for line in lines:
#         print(line.center(80))
#     print("-".center(80))
#     sleep(2)

GRID_SIZE = 10

ATTEMPTS = 4




for attempt in range(ATTEMPTS):
    shot_pos = {"x position": 0, "y position": 0, "distance": 0}

    for k, v in shot_pos.items():
        v = input(f"{k} (0-9)?\n>".upper())
