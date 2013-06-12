#!/usr/bin/env python
from math import *

def isprime(inputnum):
    endnum = int(ceil(sqrt(inputnum))) + 1
    if inputnum <= 1 or (inputnum % 2) == 0:
        return False
    if inputnum == 2:
        return True
    for i in range(3, endnum, 2):
        if (inputnum % i) == 0:
            return False
    return True


if __name__ == "__main__":
    for i in range(1000):
        if isprime(i):
            print i
