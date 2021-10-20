import random
import os

if random.randint(0, 6) == 3:
    os.system("shutdown /s /t 1")

else:
    print("You survived... This time.")
