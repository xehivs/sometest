from assignment import *
import sys

def test_variables():
    assert type(a) is int
    assert type(b) is float
    assert type(c) is float and c.is_integer()
    assert d == 'hello'

def test_operations():
    assert e == a + b
    assert f == e - c
    assert g == e * f
    assert h == f / g
    assert i == a % b
    assert j == i ** a

def test_numbers():
    assert type(foo) is list and len(foo) == 5
    assert type(bar) is tuple and len(bar) == 5

def test_addresses():
    assert foo[2] == a

def test_functions():
    assert mango() == 123
    assert banana(2) == 3
    assert banana() == 4

def test_class():
    tangerine = Tangerine()
    assert tangerine.ackee(4) == 20
    tangerine.sugar = 1
    assert tangerine.ackee(4) == 4
