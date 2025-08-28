import pytest
from fuel import convert, gauge


def main():
    test_convert()
    test_gauge()
    test_for_errors()



#Test if fraction gives rounded percentage
def test_convert():
    assert convert('3/4') == 75
    assert convert('99/100') == 99
    assert convert('1/100') == 1


#Test if gauge displays E or F - indicating fuel levels
def test_gauge():
    assert gauge(75) == '75%'
    assert gauge(99) == 'F'
    assert gauge(1) == 'E'


#Test errors
def test_for_errors():
    with pytest.raises(ValueError):
        convert('cat/rat')
    with pytest.raises(ZeroDivisionError):
        convert('5/0')
    with pytest.raises(ValueError):
        convert('-5/10')
    with pytest.raises(ValueError):
        convert('5/-10')
