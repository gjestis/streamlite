#Import packages
import random

#Make two dices function
def roll_dice():
    die_1 = random.randint(1,6)
    die_2 = random.randint(1,6)

    if die_1 == die_2:
        same_num = True

    else:
        same_num = False
    return same_num
