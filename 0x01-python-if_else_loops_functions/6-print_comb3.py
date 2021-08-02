#!/usr/bin/python3
<<<<<<< HEAD

for i in range(0, 10):
    for j in range(1 + 1, 10):
        if i >= j:
            continue
=======
for i in range(0, 9):
    for j in range(i + 1, 10):
>>>>>>> ccfe7c23a5d97fd1bb90585a58a1d2e39525adab
        if i == 8 and j == 9:
            print("{:d}{}".format(i, j))
        print("{}{}".format(i, j), end=", ")
