import pytest
from calc import add, div


def test_add():
    assert add(2, 3) == 5


def test_div_zero():
    with pytest.raises(ZeroDivisionError):
        div(1, 0)
