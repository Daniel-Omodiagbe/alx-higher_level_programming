#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    if i != ord('a') + 4 and i != ord('a') + 16:
        print("{}".format(chr(i)), end='')
