import os
import platform
import random

if platform.system == "Windows":
    os.system("cls")
else:
    os.system("clear")


g = random.randint(1, 20)
w = random.randint(1, 40)

r = g * w

print("STARSHIP TAKE-OFF\n")
print(f"GRAVITY = {g}\n")
print("TYPE IN FORCE")

for tries in range(10):
    force = int(input("> "))

    if force > r:
        print("TOO HIGH")
    elif force < r:
        print("TOO LOW")
    elif force == r:
        print("GOOD TAKE OFF")
        break

    if tries == 9:
        print("YOU FAILED - \nTHE ALIENS GOT YOU. ")
