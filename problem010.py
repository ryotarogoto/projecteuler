#!/usr/bin/env python

from algorithm import *

num = 2000000
element = [i for i in range(1, num) if isprime(i)]

print element
print sum(element)
