import pytest

from greetingkata import greet


def test_greet():
    message = greet("Luma")
    assert message == "Hello, Luma!"


def test_null():
    message = greet()
    assert message == "Hello, my friend!"


def test_shout():
    message = greet("LUMA")
    assert message == "HELLO, LUMA!"


def test_list():
    message = greet(["Luma", "Mateus", "Deco", "Ingrid"])
    assert message == "Hello, Luma, Mateus, Deco and Ingrid!"
