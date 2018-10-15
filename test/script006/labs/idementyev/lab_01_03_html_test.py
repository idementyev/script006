#!/usr/bin/env python3

import pytest
from script006.labs.idementyev.lab_01_03_html import html_decorator

tests = [
    # 2 parameters in tuple, then expected result
    (("tag", "string"), "<tag>string</tag>"),
    ((2, "string"), "string"),
    ((8.33, "string"), "string"),
    (([1, 3, 5], "string"), "string"),
    ((None, "string"), "string"),
    (("228", "string"), "string"),
    (("I have spaces", "string"), "string"),
    (("n42", "string"), "<n42>string</n42>"),
    (("b", 'test with "quotes"'), "<b>test with &quot;quotes&quot;</b>"),
    (("i", '1 & 0 <> 2'), "<i>1 &amp; 0 &lt;&gt; 2</i>"),
]


@pytest.mark.parametrize("case, result", tests)
def test_cases(case, result):
    assert result == html_decorator(*case)


def test_one_param():
    with pytest.raises(TypeError):
        html_decorator("only 1 param")


def test_three_params():
    with pytest.raises(TypeError):
        html_decorator("too", "many", "params")
