#!/usr/bin/python3
for i in range(10):
    for j in range(1, 10):
        if i != j and i < j:
            print("{}".format(i), end="")
            if i != 8:
                print("{}".format(j), end=", ")
            else:
                print("{}".format(j))

