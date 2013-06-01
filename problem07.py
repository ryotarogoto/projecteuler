#!/usr/bin/env python

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

prime = [2]
num = 3
num_th = 10001
while len(prime) < num_th:
    if checkPrime(num):
        prime.append(num)
    num = num + 2

print prime[-1]
