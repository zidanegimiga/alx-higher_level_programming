#!/usr/bin/python3
i = 0
for i in range(0, 99):
    if i != 99:
        print("{:d}".format(i), end = ", ")
    else:
        print("{:d}\n".format(i))
