#!Python
"""A python conversion of the game 'Evil Alien' from Osborne's 'Computer Spacegames', published 1982."""

import os
from pathlib import Path
import platform
import random
import curses
from playsound import playsound
from time import sleep


if platform.system == "Windows":
    os.system("cls")
else:
    os.system("clear")

# SCRIPT_DIR = Path(__file__).parent
# TYPE_SOUND = SCRIPT_DIR / "mixkit-typewriter-soft-hit-1366.wav"

# playsound("mixkit-typewriter-soft-hit-1366.wav")

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
curses.initscr()
curses.curs_set(0)
for lines in messages:
    for line in lines:
        for char in line.center(80):
            if char != " ":
                sleep(0.05)
            print(char, end="", flush=True)
            sound_path = os.path.join(
                abs_dir_path, "sounds/mixkit-typewriter-soft-hit-1366.wav"
            )
            # playsound("Spacegames/EvilAlien/mixkit-typewriter-soft-hit-1366.wav")
        print("\r")
    print()
    sleep(0.5)
curses.curs_set(1)
curses.endwin()
GRID_SIZE = 10

ATTEMPTS = 4


for attempt in range(ATTEMPTS):
    shot_fired = {"x position": 0, "y position": 0, "distance": 0}

    enemy_ship = {
        f"{k} position": random.randint(1, GRID_SIZE) for k in ["x", "y", "z"]
    }
    enemy_ship

    # for k, v in shot_pos.items():
    #     v = input(f"{k} (0-9)?\n>".upper())
