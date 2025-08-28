import pytest
from twttr import shorten

def main():
    test_vowels()
    test_consonants()
    test_numbers()

def test_vowels():
    assert shorten('Twitter') == 'Twttr'
    assert shorten('Watermelon') == 'Wtrmln'
    assert shorten('What do you mean?') == 'Wht d y mn?'

def test_consonants():
    assert shorten('RS3') == 'RS3'
    assert shorten('Rythm') == 'Rythm'

def test_numbers():
    assert shorten('246') == '246'
    assert shorten ('666') == '666'

#Test case sensitivity - lowercase
def test_lower():
    assert shorten('twitter') == 'twttr'
    assert shorten('rS3') == 'rS3'
    assert shorten('246') == '246'

#Test case sensitivity - uppercase
def test_upper():
    assert shorten('TWITTER') == 'TWTTR'
    assert shorten('RS3') == 'RS3'
    assert shorten('246') == '246'