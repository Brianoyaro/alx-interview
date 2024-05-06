#!/usr/bin/python3
def getPrime(start):
    while True:
        if (start % 2 == 0) or (start % 3 == 0) or \
                (start % 5 == 0) or (start % 7 == 0):
            if start not in [2, 3, 5, 7]:
                start += 1
            else:
                return start
                break
        else:
            return start
            break


def minOperations(n):
    val = 0
    prime = 2
    temp = n
    while n > 1:
        while (n % prime != 0):
            prime = getPrime(prime + 1)
        if temp < prime:
            return 0
        n /= prime
        if (n == 1) and (prime == temp):
            return 0
        val += prime
    return val
