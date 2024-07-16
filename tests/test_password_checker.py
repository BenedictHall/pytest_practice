import pytest
from lib.password_checker import *

def test_password_checker_bad():
    password = PasswordChecker()
    with pytest.raises(Exception) as e:
        password.check("abc")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters"

def test_password_checker_good():
    password = PasswordChecker()
    result = password.check("abcdefgh")
    assert result == True