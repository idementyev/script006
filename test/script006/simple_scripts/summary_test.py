import pytest
from script006.simple_scripts import summary

fixtures = [
    (0, 0),
    (5, 15),
    (1, 1),
    (3,6),
    (4,10)
]


@pytest.mark.parametrize("input, expected", fixtures)
def test_summary(input, expected):
    assert summary(input) == expected


def test_summary_raises():
    with pytest.raises(ValueError):
        summary(-1)
