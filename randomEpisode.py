import os

import random

p = '/home/shruti/Videos/Scam 1992 the Harshad Mehta Story'

os.chdir(p)



folder_name = random.choice(os.listdir(p)) 


print("Enjoy!")

#play to file

os.system("xdg-open " + folder_name)

