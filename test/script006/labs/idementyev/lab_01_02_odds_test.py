#!/usr/bin/env python3

import pytest
from script006.labs.idementyev.lab_01_02_odds import odd_numbers

default = [x for x in range(0, 100) if x % 2 != 0]
tests = [
    ((0, 10), [1, 3, 5, 7, 9]),
    ((0, 100), default),
    (435, []),
    ((0, 0), []),
    ("string here", []),
    ((-1, 59), []),
    (("one", "two"), []),
    ((None, None), []),
    ((9, 1), [1, 3, 5, 7]),
]


@pytest.mark.parametrize("case, result", tests)
def test_summary(case, result):
    assert result == odd_numbers(case)
