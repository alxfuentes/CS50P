from jar import Jar
import pytest

def test_init():
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar("not an integer")
        
def test_str():        
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(-1)
    with pytest.raises(ValueError):
        jar.deposit("not an integer")
    jar.deposit(5)
    assert jar.size == 5

def test_withdraw():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(-1)
    with pytest.raises(ValueError):
        jar.withdraw("not an integer")
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3