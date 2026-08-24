"""
Automated tests for calculator.py (STUDENT VERSION)
======================================================

Run these with:

    pytest -v

You should not need to edit this file. If you think a test is
wrong, ask your tutor rather than changing the test to make it pass.
"""

import pytest

from calculator.calculator import (
    add,
    subtract,
    multiply,
    divide,
    modulo,
    power,
    percentage_of,
    convert_currency,
)


def test_add():
    assert add(2, 3) == 5
    assert add(-2, 3) == 1
    assert add(2.5, 2.5) == 5.0


def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(4, 10) == -6


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10


def test_divide():
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5


def test_divide_by_zero_raises_error():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


def test_modulo():
    assert modulo(10, 3) == 1
    assert modulo(17, 5) == 2


def test_modulo_by_zero_raises_error():
    with pytest.raises(ZeroDivisionError):
        modulo(10, 0)


def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1


def test_percentage_of():
    assert percentage_of(200, 15) == 30.0
    assert percentage_of(50, 100) == 50.0


def test_convert_currency():
    assert convert_currency(100, 1.27) == 127.0
    assert convert_currency(10, 0.79) == 7.9
