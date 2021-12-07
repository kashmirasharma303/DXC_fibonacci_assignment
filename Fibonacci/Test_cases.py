import pytest
from Fibonacci import main
def test_1():
    assert main.get_fibonacci(1) == "0", "nterms = 1 test failed"

def test_2():
    assert main.get_fibonacci(3) == "0,1,1", "nterms = 3 test failed"
