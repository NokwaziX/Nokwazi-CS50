import pytest
from bank import value

def main():
    test_hello()
    test_startwith_h()
    test_other()
    test_lower()
    test_upper()

#Test that if the greeting is starts with 'hello' - it must equal $0
def test_hello():
    assert value('hello') == 0
    assert value('hello, stranger') == 0

#Test that if the greeting is starts with 'h' - it must equal $20
def test_startwith_h():
    assert value('heita') == 20
    assert value('heita bafwethu') == 20

#Test that if the greeting is starts with anything else - it must equal $100
def test_other():
    assert value('sho!') == 100
    assert value('sho, fede?') == 100


#Test case sensitivity - lowercase
def test_lower():
    assert value('hello') == 0
    assert value('hello, stranger') == 0
    assert value('heita') == 20
    assert value('heita bafwethu') == 20
    assert value('sho!') == 100
    assert value('sho, fede?') == 100

#Test case sensitivity - uppercase
def test_upper():
    assert value('HELLO') == 0
    assert value('HELLO, STRANGER') == 0
    assert value('HEITA') == 20
    assert value('HEITA, BAFWETHU') == 20
    assert value('SHO!') == 100
    assert value('SHO, FEDE?') == 100
