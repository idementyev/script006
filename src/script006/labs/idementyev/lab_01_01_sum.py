#!/usr/bin/env python3

"""
Function that returns the sum of n numbers
"""

__version__ = '0.0.1'
__author__ = 'Ilya R. Dementyev'
__date__ = '2018-10-14'


def numbers_sum(numbers: list) -> float:
    """
    Return sum of all numbers in a list or tuple, skip NaN.
    :param numbers: list with numbers to sum
    :return: sum of numbers (float)
    """

    result = 0
    n_type = type(numbers)

    if n_type is list or n_type is tuple:
        for n in numbers:
            # substitution for math.isnan()
            if type(n) is int or type(n) is float:
                result += n
    elif n_type is int or n_type is float:
        result = numbers
    return float(result)
