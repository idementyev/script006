#!/usr/bin/env python3

"""
Function that returns odd numbers from a given interval.
The interval is given from standard input.
The default is not implemented: tests lose any meaning.
"""

__version__ = '0.0.1'
__author__ = 'Ilya R. Dementyev'
__date__ = '2018-10-14'


def odd_numbers(interval: tuple = ()) -> list:
    """
    Return list of odd numbers from an interval
    :param interval: tuple of (start, end) values
    :return: list
    """

    odds = []

    if not interval:
        print("Enter interval start and end values below. "
              "Positive integers, please.")
        while True:
            _ = input("Start: ")
            try:
                int(_)
            except ValueError:
                print("Not an integer, let's try again!")
            else:
                if int(_) >= 0:
                    start = int(_)
                    print("Start is set to {}".format(start))
                    break
                else:
                    print("Positive, please!")

        while True:
            _ = input("End: ")
            try:
                int(_)
            except ValueError:
                print("Not an integer, let's try again!")
            else:
                if int(_) >= 0:
                    end = int(_)
                    print("End is set to {}".format(end))
                    break
                else:
                    print("Positive, please!")

        interval = (start, end)

    try:
        start, end = interval
        start >= 0
        end >= 0
    except ValueError:
        print("Too many values given")
    except TypeError:
        print("Cannot unpack this, check your input")
    else:
        if start >= 0 and end >= 0:
            if end < start:
                start, end = end, start
                print("Had to swap them for you, smartass!")
            for n in range(start, end):
                if n % 2 != 0:
                    odds.append(n)

    return odds
