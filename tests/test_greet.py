from lib.greet import *

def test_greet_returns_name():
    result = greet("Greg")
    assert result == "Hello, Greg!"