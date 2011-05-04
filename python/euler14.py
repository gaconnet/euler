def collatz_counter(start):
    count, n = 1, start
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        count += 1

    return count


def collatz(n):
    yield n
    while n > 1:
        if n % 2 == 0:
            n = n / 2
            yield n
        else:
            n = 3 * n + 1
            yield n

    raise StopIteration


if __name__ == '__main__':
    m, m_i = 0, 0
    for i in xrange(1, int(1e6)):
        c = collatz_counter(i)
        if c > m:
            m, m_i = c, i

    print m, m_i
