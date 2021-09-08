#!/usr/bin/python3
for x in range(0, 10):
    for i in range((x+1), 10):
        if (x is not 8) or (i is not 9):
            print("{}{}, ".format(x,i), end="")
        else:
            print("{}{}, ".format(x,i))
