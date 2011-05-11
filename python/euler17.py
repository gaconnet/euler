"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.  

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?  

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with
British usage.

"""

"""
http://en.wikipedia.org/wiki/List_of_numbers#Small_numbers

"""


def single(n):
    return {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
    }[n]


def tens(n):
    return {
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
    }[n]


def magnitudes(n):
    return {
        100: "hundred",
        1000: "thousand",
    }[n]


def to_english(n):
    """Non-robustly convert decimal to english"""
    words = []

    count, n = divmod(n, 1000)
    if count:
        words.append(single(count))
        words.append(magnitudes(1000))
        if 0 < n < 100:
            words.append('and')

    count, n = divmod(n, 100)
    if count:
        words.append(single(count))
        words.append(magnitudes(100))
        if n:
            words.append('and')

    if n > 19:
        count, n = divmod(n, 10)
        words.append(tens(count * 10))

    if n:
        words.append(single(n))

    return ''.join(words)


if __name__ == '__main__':
    print to_english(342), len(to_english(342))
    print to_english(115), len(to_english(115))
    print sum(len(to_english(i)) for i in xrange(1, 1001))
