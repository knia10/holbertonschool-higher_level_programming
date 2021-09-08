#!/usr/bin/python3
def uppercase(s):
    for i in s:
        if (ord(i) >= ord('a')) and (ord(i) <= ord('z')):
            i = chr(ord(i)-ord('a')+ord('A'))
        print("{}".format(i), end='')
    print()
    