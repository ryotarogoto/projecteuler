#!/usr/bin/env python

num = 10
while True:
    flag = 0
    for i in range(1, 21):
        flag = flag + (num % i)
        if flag > 0:
            break
    if flag == 0:
        break
    num = num + 10

print num


