from src.romanNumeral import dec_to_rom
from src.romanNumeral import rom_to_dec
def test_num1():
 assert dec_to_rom(1) == "I"

def test_num2():
    assert dec_to_rom(2) == "II"

def test_num4():
    assert dec_to_rom(4)== "IV"

def test_num5():
    assert dec_to_rom(5)== "V"

def test_num9():
    assert dec_to_rom(9)== "IX"
def test_nb14():
    assert dec_to_rom(14)== "XIV"
def test_nb19():
    assert dec_to_rom(19)== "XIX"
def test_convI():
    assert rom_to_dec('I') == 1
