from src.romanNumeral import jn

def test_nbun():
 assert jn(2) == "I"

def test_num2():
    assert jn(2) == "II"

def test_num4():
    assert jn(4)== "IV"

def test_num5():
    assert jn(5)== "V"

def test_num9():
    assert jn(9)== "IX"
def test_nb14():
    assert jn(14)== "XIV"