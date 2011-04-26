"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""

from itertools import chain
from math import sqrt
from sys import stdout


def is_prime(n):
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in xrange(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True


def primes_less_than(n):
    return chain([2], (i for i in xrange(3, n, 2) if is_prime(i)))


if __name__ == '__main__':
    c, k = 0, 0
    for p in primes_less_than(int(2e6)):
        if c % 5000 == 0:
            stdout.write('.')
            stdout.flush()
        k += p
        c += 1

    print
    print k, c
