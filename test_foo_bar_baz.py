import pytest

from foo_bar_baz import foo_bar_baz

#Add testcases Here

def test_basic():
    assert foo_bar_baz(1) == "1"
    assert foo_bar_baz(2) == "1 2"
    assert foo_bar_baz(3) == "1 2 Foo"
    assert foo_bar_baz(5) == "1 2 Foo 4 Bar"
    assert foo_bar_baz(15) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz"

def test_invalid():    
    assert foo_bar_baz(0) == ""
    assert foo_bar_baz(-5) == ""

def test_long():
    assert foo_bar_baz(30) == "1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 Baz 16 17 Foo 19 Bar Foo 22 23 Foo Bar 26 Foo 28 29 Baz" 

def test_length():    
    assert foo_bar_baz(6).count(" ") == 5