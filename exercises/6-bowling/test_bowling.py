from src.bowling import Bowling
def test_0quille():
    bowling0 = Bowling()
    assert bowling0.zero(0 + 0) == True

def test_1quille():
    bowling1 = Bowling()
    assert bowling1.zero(0+1) == True