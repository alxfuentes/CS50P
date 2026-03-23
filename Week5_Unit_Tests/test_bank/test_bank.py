import bank

def test_hello():
    assert bank.value("Hello, there!") == 0

def test_hi():
    assert bank.value("Hi, how are you") == 20

def test_any_news():
    assert bank.value("Any news from the front!") == 100


