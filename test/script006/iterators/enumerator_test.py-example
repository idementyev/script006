import pytest

from script006.iterators import my_enumerate


def test_enumerator():
    inputted = [x for x in range(10)]
    tested, expected = my_enumerate(inputted), enumerate(inputted)
    with pytest.raises(StopIteration):
        while True:
            assert next(tested) == next(expected)


def test_enumerator_with_nonzero_start():
    inputted = [x for x in range(10)]
    start = 5
    tested, expected = my_enumerate(inputted, start), enumerate(inputted, start)
    with pytest.raises(StopIteration):
        while True:
            assert next(tested) == next(expected)