#This piece of code is a joke do NOT take this seriously
import random
chances = 0

b=random.randint(1,10)
while chances < 5:
    a=int(input("Dear fine gentleman,what number do you choose from 1 to 9,and if within 3 chances it matches with what i choose, then 2 tickets to No Way Home I will give you.\n"))
    if a==b :
        print("Fine you win. Here you go.")
        break
    elif a>b:
        print("HAHAHAHA LOSER.YOUR GUESS WAS TOO HIGH")
        chances=chances+1
    else:
            print("HAHAHAHA LOSER. YOUR GUESS WAS TOO LOW")
            chances=chances+1

if not chances < 5
    print("HAHAHAHA LOSER YOU LOST. THE NUMBER WAS", b)

chances += 1

