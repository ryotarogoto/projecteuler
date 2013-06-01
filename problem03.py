#!/usr/bin/env python

num = 600851475143

flag = 0
count = 0
def checkPrime(innum):
    a = list()
    if (innum % 2) == 0:
        return False
    for i in range(3, innum-1, 2):
        if (innum % i) == 0:
            a.append(i)
            if len(a) == 1:
                return False
    return True

b = list()
multi = 1
flag = 3
while True:
    if checkPrime(flag):
        if (num % flag) == 0:
            b.append(flag)
            for p in b:
                multi = multi * p
            if multi == num:
                break;
            multi = 1
    flag = flag + 2

print max(b)
