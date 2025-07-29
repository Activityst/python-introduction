from src.romanNumeral import jn

def test_nbun():
 assert jn(2) == "I"

def test_num2():
    assert jn(2) == "II"

def test_num4():
    assert jn(4)== "IV"