import random
import os

if random.randint(0, 6) == 3:
    os.system("shutdown /s /t 1")
    print("We do a little trolling")

else:
    print("You survived... This time.")
