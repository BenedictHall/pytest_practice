from lib.check_codeword import *

def test_check_codeword_returns_correct():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_check_codeword_returns_almost():
    result = check_codeword("hose")
    assert result == "Close, but nope."

def test_check_codeword_returns_wrong():
    result = check_codeword("Horsey")
    assert result == "WRONG!"