from lib.report_length import *

def test_report_1():
    result = report_length("horse")
    assert result == "This string was 5 characters long"

def test_report_2():
    result = report_length("spiderman")
    assert result == "This string was 9 characters long"