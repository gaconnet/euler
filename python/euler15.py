"""
Starting in the top left corner of a 2x2 grid, there are 6 routes (without
backtracking) to the bottom right corner.

How many routes are there through a 20x20 grid?

"""

"""
We want to count how many distinct permutations there are of 20 east steps
and 20 south steps.

If we look at the entire route as 40 empty slots, we merely need to count how
many ways there are to choose 20 of those slots to assign a specific direction,
say, east. For distinct selection of 20 slots, there is only one way to assign
the remaining 20 slots to the remaining direction.

Hence, our answer is bc(40, 20) where bc(n, k) is the binomial coefficient.

"""

def falling_factorial(x, m):
    """`x` to the `m` falling
    http://en.wikipedia.org/wiki/Falling_factorial_power#Alternate_notations

    """
    assert m >= 0

    for i in xrange(x - 1, m, -1):
        x *= i

    return x


def bc(n, k):
    """Binomial Coefficient

    (n)_k / k!

    http://en.wikipedia.org/wiki/Binomial_coefficient#Multiplicative_formula

    """
    return falling_factorial(n, k) / falling_factorial(k, 1)


if __name__ == '__main__':
    print bc(4, 2)
    print bc(40, 20)
