from src import fizzbuzz

def test_fizzbuzz() :
    assert fizzbuzz(1) == "1"

def test_divsion100() :
    assert fizzbuzz(100) == "Buzz"

def test_division5() :
    assert fizzbuzz(55) == "Buzz"

def test_2():
    assert fizzbuzz(2)== "2"

def test_3( ):
    assert fizzbuzz(3)== "3"