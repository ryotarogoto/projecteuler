#!/usr/bin/env python

ary1 = list()
ary2 = list()
for i in range(1, 101):
    ary1.append(i**2)
    ary2.append(i)

sum_squares = sum(ary1)
squares_sum = sum(ary2) * sum(ary2)

print squares_sum - sum_squares
