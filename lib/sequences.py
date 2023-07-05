#!/usr/bin/env python3

def print_fibonacci(length):

    fib = []
    for i in range(length):
        if (i < 2):
            fib.append(i)
        else:
            fib.append(fib[i-1] + fib[i-2])

    print(fib)