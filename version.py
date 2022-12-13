from datetime import datetime as d
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()
title = input('Game Title: ') 

clear()
answer = input('Select a style: [S]eperated [C]ombined ')

t = d.now()
cdt = t.strftime('%Y%M%d')
sdt = t.strftime('%Y.%M.%d')

if answer == 'S':
    clear()
    print(title + '\n' + sdt)
elif answer == 'C':
    clear()
    print(title + '\n' + cdt)
else:
    clear()
    print('Error: Not an option')
    quit()