import numb3rs

def test_valid_ips():
    assert numb3rs.validate("192.168.1.1") == True
    assert numb3rs.validate("255.255.255.255") == True
    assert numb3rs.validate("0.0.0.0") == True
    assert numb3rs.validate("127.0.0.1") == True

def test_invalid_ips():
    assert numb3rs.validate("256.1.1.1") == False
    assert numb3rs.validate("192.168.1") == False
    assert numb3rs.validate("192.168.1.1.1") == False
    assert numb3rs.validate("abc.def.ghi.jkl") == False
    assert numb3rs.validate("192.168.1.256") == False

def test_leading_zeros():
    assert numb3rs.validate("192.168.001.1") == False
    assert numb3rs.validate("010.0.0.0") == False
    assert numb3rs.validate("192.168.1.01") == False