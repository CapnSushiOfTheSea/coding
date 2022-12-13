#i made this during science cuz i finished early
import time
import random

def cryAboutIt():
    tears = 0
    sobbing = True
    while sobbing:
        tears += 1
        sniffles = random.randint(0,5)
        if sniffles > 0:
            print(str(tears) + " tears")
        else:
            print("*sniff*")
        time.sleep(.3)

cryAboutIt()