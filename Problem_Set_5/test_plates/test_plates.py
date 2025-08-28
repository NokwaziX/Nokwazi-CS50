import pytest
from plates import is_valid

def main():
    test_length()
    test_first_two()
    test_number_position()
    test_punc_space()

#Test if the plate has Max 6 & Minimum 2 characters
def test_length():
    assert is_valid('ILOVEU') == True
    assert is_valid('I') == False

#Test if the first 2 charaters of plate are letters only
def test_first_two():
    assert is_valid('IL') == True
    assert is_valid('44') == False

#Test if no numbers in the middle, only at the end and that the fist number is not a '0'
def test_number_position():
    assert is_valid('ILV44') == True
    assert is_valid('ILV044') == False
    assert is_valid('IL44EU') == False

#Test that there are no punctuation marks or spaces in the plate
def test_punc_space():
    assert is_valid('ILV U') == False
    assert is_valid('ILVEU!') == False
