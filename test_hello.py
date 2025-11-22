from hello import greet, add, divide
import pytest


def test_greet():
    assert greet() == "Hello, Secure World!"
    assert greet("Amen") == "Hello, Amen!"


def test_add():
    assert add(2, 3) == 5


def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ValueError):
        divide(10, 0)

