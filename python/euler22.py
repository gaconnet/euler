"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name
score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938  53 = 49714.

What is the total of all the name scores in the file?

"""


from itertools import chain
import string


LETTER_SCORES = dict((l, i + 1) for i, l in enumerate(string.lowercase))


def parse_names(filename):
    with open(filename) as f:
        flatlines = chain(*(line.split(',') for line in f))

    return (name.strip('"').lower() for name in flatlines)
        

if __name__ == '__main__':
    names = parse_names('data/names.txt')
    print sum((i + 1) * sum(LETTER_SCORES[letter] for letter in name)
              for i, name in enumerate(sorted(names)))
