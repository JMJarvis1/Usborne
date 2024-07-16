import os
import random

os.system("cls")

print("STARSHIP TAKE-OFF")

g = random.randint(1, 20)
w = random.randint(1, 40)

r = g * w

print(f"GRAVITY= {g}\n")
print("TYPE IN FORCE")

for tries in range(10):
    force = int(input("> "))

    if force > r:
        print("TOO HIGH")
        continue
    elif force < r:
        print("TOO LOW")
        continue
    elif force == r:
        print("GOOD TAKE OFF")
        break
    else:
        print("YOU FAILED - \n THE ALIENS GOT YOU. ")
