from src.bowling import Bowling
from src.RegularFrame import RegularFrame
def test_0quilles():
    bowling0 = Bowling("-- -- -- -- -- -- -- -- -- --")
    assert bowling0.calc() == 6
def test_bowling_part2():
    party_2= Bowling("")

