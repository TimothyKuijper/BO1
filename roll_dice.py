from doctest import DONT_ACCEPT_TRUE_FOR_1
import random
import time

#dice

def rolldice1():
    d = random.randint(1,6)
    return d

def rolldice2():
    e = random.randint(1,6)
    return e

#print dice

d1 = rolldice1()
d2 = rolldice2()
print(d1)
print(d2)

#dubble rol repeater

while True:
    if d1 == d2:
        print("you rolled a dubble, you can go again")
        time.sleep(0.5)
        d3 = random.randint(1,6)
        d4 = random.randint(1,6)

        print(d3)
        print(d4)

        if d3 == d4:
            
            continue
        else:
            break
    else :
        break    

#total worth of roll + print

if d1 == d2:
    print("you rolled",  d1 + d2 + d3 + d4)
else:
    print("you rolled", d1 + d2)
 
print("thank you for rolling")




    