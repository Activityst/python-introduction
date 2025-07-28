from src import fizzbuzz

def test_fizzbuzz() -> str:
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(9) == "Fizz"
    assert fizzbuzz(10) == "Buzz"


def test_multiple3() ->str:
    assert fizzbuzz(100)

def test_division5() ->str:
    assert fizzbuzz(55) == "Fizz"

