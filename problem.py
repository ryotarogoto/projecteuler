#!/usr/bin/env python

def div3or5(num):
    ans = list()
    for i in range(num):
        if (i % 3) == 0:
            ans.append(i)
        elif (i % 5) == 0:
            ans.append(i)
        else:
            continue
    return sum(ans)

print div3or5(1000)
