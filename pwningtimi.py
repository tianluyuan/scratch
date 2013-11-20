#!/usr/bin/python
import random
from array import array

def pwnTimi(number):
    biglist = [1]*(len(number)-4)

    # highest = 0
    for idx, digit_str in enumerate(number):
        for i in range(5): 
            if (idx-i)<0: break

            try:
                biglist[idx-i]=biglist[idx-i]*int(digit_str)
                # if biglist[idx-i] > highest: highest = biglist[idx-i]
            except:
                continue

    biglist.sort(reverse=True)

    highest = biglist[0]
    print highest
    return

if __name__=='__main__':
    num = str(random.randint(0, 10**1001-1))
    pwnTimi(num)
