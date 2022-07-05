## To run the tests in this file:
##      pip install pytest
##      pytest -s

from main import processNumber

def test_3_multiple():
    assert processNumber(3, 'True', 'True', 'True', 'True', 'True', 'True') == "Fizz"
    assert processNumber(6, 'True', 'True', 'True', 'True', 'True', 'True') == "Fizz"

def test_5_multiple():
    assert processNumber(5, 'True', 'True', 'True', 'True', 'True', 'True') == "Buzz"
    assert processNumber(10, 'True', 'True', 'True', 'True', 'True', 'True') == "Buzz"
    
def test_3_and_5_multiple():
    assert processNumber(15, 'True', 'True', 'True', 'True', 'True', 'True') == "FizzBuzz"
    assert processNumber(30, 'True', 'True', 'True', 'True', 'True', 'True') == "FizzBuzz"
    
def test_7_multiple():
    assert processNumber(7, 'True', 'True', 'True', 'True', 'True', 'True') == "Bang"
    assert processNumber(21, 'True', 'True', 'True', 'True', 'True', 'True') == "FizzBang"
    assert processNumber(105, 'True', 'True', 'True', 'True', 'True', 'True') == "FizzBuzzBang"
    
def test_11_multiple():
    assert processNumber(11, 'True', 'True', 'True', 'True', 'True', 'True') == "Bong"
    assert processNumber(22, 'True', 'True', 'True', 'True', 'True', 'True') == "Bong"
    assert processNumber(33, 'True', 'True', 'True', 'True', 'True', 'True') == "Bong"
    assert processNumber(44, 'True', 'True', 'True', 'True', 'True', 'True') == "Bong"
    assert processNumber(55, 'True', 'True', 'True', 'True', 'True', 'True') == "Bong"
    
def test_13_multiple():
    assert processNumber(65, 'True', 'True', 'True', 'True', 'True', 'True') == "FezzBuzz"
    assert processNumber(195, 'True', 'True', 'True', 'True', 'True', 'True') == "FizzFezzBuzz"
    assert processNumber(143, 'True', 'True', 'True', 'True', 'True', 'True') == "FezzBong"

def test_17_multiple():
    assert processNumber(255, 'True', 'True', 'True', 'True', 'True', 'True') == "BuzzFizz"
    
def test_prime_numbers():
    assert int(processNumber(19, 'True', 'True', 'True', 'True', 'True', 'True')) == 19
    assert int(processNumber(23, 'True', 'True', 'True', 'True', 'True', 'True'))== 23
    assert int(processNumber(89, 'True', 'True', 'True', 'True', 'True', 'True')) == 89
    assert int(processNumber(97, 'True', 'True', 'True', 'True', 'True', 'True')) == 97
