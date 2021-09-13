#!/usr/bin/python3
if __name__ == '__main__':
    for alp in range(ord('z'), ord('a')-1, -1):
        if alp % 2 != 0:
            alp = alp - 32
        print('{}'.format(chr(alp)), end="")
