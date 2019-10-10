import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

DuplicateAndMissing = collections.namedtuple('DuplicateAndMissing',
                                             ('duplicate', 'missing'))


def find_duplicate_missing(A):
    unique_nums = set()
    duplicate = None
    missing = 0
    for num in A:
        if num in unique_nums:
            duplicate = num
        else:
            unique_nums.add(num)

    for num in unique_nums:
        missing ^= num

    for i in range(len(A)):
        missing ^= i

    return DuplicateAndMissing(duplicate, missing)


def res_printer(prop, value):
    def fmt(x):
        return 'duplicate: {}, missing: {}'.format(x[0], x[1]) if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_for_missing_element.py",
            'find_missing_and_duplicate.tsv',
            find_duplicate_missing,
            res_printer=res_printer))
