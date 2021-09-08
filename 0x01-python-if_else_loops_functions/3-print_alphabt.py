#!/usr/bin/python3
for alp in range (ord('a'), ord('z')+1):
    if alp is not (ord('q')) and alp is not (ord('e')):
        print('{}'.format(chr(alp)), end='')