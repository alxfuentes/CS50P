import plates

def test_alphanumeric():
    assert plates.is_valid("HELLO") == True
    assert plates.is_valid("HELLO!") == False

def test_two_letters():
    assert plates.is_valid("CS50") == True
    assert plates.is_valid("HI") == True
    assert plates.is_valid("H501") == False

def test_no_zero():
    assert plates.is_valid("CS50") == True
    assert plates.is_valid("CS050") == False

def test_no_trailing_letters():
    assert plates.is_valid("CS50P") == False
    assert plates.is_valid("CS50X") == False

def test_six_or_less():
    assert plates.is_valid("CSP501") == True
    assert plates.is_valid("OUTATIME") == False

def test_no_alpha():
    assert plates.is_valid("2187") == False
    assert plates.is_valid("1138") == False

