from les_1 import checktext

def test_step1(badword, goodword):
    assert goodword in checktext(badword), 'Test_1 FAIL'