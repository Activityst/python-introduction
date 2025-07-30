from src.bowling import Bowling
from src.RegularFrame import RegularFrame
def test_0quilles():
    bowling0 = Bowling("-- -- -- -- -- -- -- -- -- --")
    assert bowling0.calc() == 0
def test_lancé1():
    lancé_1 = RegularFrame()
    assert lancé_1.firstlancé(1)
