#!/usr/bin/env python3

import pytest
from script006.labs.idementyev.lab_01_01_sum import numbers_sum

tests = [
    ([1, 2, 3], 6.0),
    ([], 0.0),
    (["string here", 'another'], 0.0),
    ([-64.43, 83, True, 2.7] +
     ["what's this", 9, "i can't even"], 30.269999999999992),  # binary float!
    (1, 1.0),
    ((34, 88, -29), 93.0)
]


@pytest.mark.parametrize("case, result", tests)
def test_summary(case, result):
    assert result == numbers_sum(case)
