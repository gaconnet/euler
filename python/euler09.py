"""
A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

    a^2 + b^2 = c^2

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""

"""
I see two subproblems here:
    * Generate all distinct sets {a, b, c} where the elements sum to 1000.
    * Add constraints to the above set generation so that we only look at
      numbers that are "close" to satisfying the Pythagorean equation.

For now here is a not-quite-distinct approximation to the first subproblem,
followed by a trivial filter operation.

"""
def pairs(t):
    return ((a, t - a) for a in xrange(1, int(t/2) + 1))


def triples(t):
    return ((a, b, c) for a in xrange(1, int(t/3) + 1)
            for b, c in pairs(t - a))  # XXX still some symmetries here

if __name__ == '__main__':
    for a, b, c in triples(1000):
        if a ** 2 + b ** 2 == c ** 2:
            print a, b, c, a * b * c, c ** 2

    # count redundant triples
    stats = dict(
        used=len(list(triples(1000))),
        needed=len(set(map(frozenset, triples(1000)))),
    )
    stats['redundant'] = stats['used'] - stats['needed']

    print "used {used}; needed {needed}; redundant {redundant}".format(**stats)
