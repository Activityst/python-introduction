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
def test_convII():
    assert rom_to_dec('II') == 2
def test_concIV():
    assert rom_to_dec('IV') == 4


def test_concV():
    assert rom_to_dec('V') == 5


def test_convIX():
    assert rom_to_dec('IX') == 9


def test_concXIX():
    assert rom_to_dec('XIX') == 19


def test_concIC():
    assert rom_to_dec('IC') == 99


def test_concC():
    assert rom_to_dec('C') == 100


def test_convMMCDXCVIII():
    assert rom_to_dec('MMCDXCVIII') == 2498

