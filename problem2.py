#!/usr/bin/env python

def answer(input):
    if input == 1:
        return 1
    elif input == 2:
        return 2
    else:
        return answer(input - 2) + answer(input - 1)

def checkeven(num):
    if num % 2 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    i = 1
    a = list()
    while answer(i) < 4000000:
        fib = answer(i)
        if checkeven(fib):
            a.append(fib)
        i = i + 1

    print sum(a)
