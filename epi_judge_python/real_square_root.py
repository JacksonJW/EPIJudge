from test_framework import generic_test
import math


def square_root(x):
    lower_bound, upper_bound = (x, 1.0) if x < 1 else (1.0, x)

    while not math.isclose(lower_bound, upper_bound):
        median = lower_bound + (upper_bound - lower_bound) * 0.5
        if median * median > x:
            upper_bound = median
        else:
            lower_bound = median

    return lower_bound


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("real_square_root.py",
                                       'real_square_root.tsv', square_root))
