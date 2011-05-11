"""
n! means n * (n - 1) * ... * 3 * 2 * 1

For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

"""


import euler15 as eu


if __name__ == '__main__':
    fact_100 = eu.falling_factorial(100, 1)
    print reduce(lambda a, b: int(a) + int(b), str(fact_100))
