#!/usr/bin/env python

a = list()
flag = 0
for i in range(100, 999):
    for j in range(100, 999):
        a.append(str(i * j))

#number of half caluculation if i <=  j

b = list()
for e in a:
    if e[0] == e[-1]:
        if e[1] == e[-2]:
            if e[2] == e[-3]:
                b.append(int(e))

print max(b)
print a.index(str(max(b)))
print 


