import twttr


def test_shorten_basic():
    """Test basic vowel removal"""
    assert twttr.shorten("hello") == "hll"
    assert twttr.shorten("world") == "wrld"
    assert twttr.shorten("twitter") == "twttr"


def test_shorten_lowercase():
    """Test with lowercase vowels"""
    assert twttr.shorten("aeiou") == ""
    assert twttr.shorten("apple") == "ppl"
    assert twttr.shorten("example") == "xmpl"


def test_shorten_uppercase():
    """Test with uppercase vowels"""
    assert twttr.shorten("HELLO") == "HLL"
    assert twttr.shorten("AEIOU") == ""
    assert twttr.shorten("WORLD") == "WRLD"


def test_shorten_mixed_case():
    """Test with mixed case"""
    assert twttr.shorten("HeLLo") == "HLL"
    assert twttr.shorten("Twitter") == "Twttr"


def test_shorten_no_vowels():
    """Test strings with no vowels"""
    assert twttr.shorten("xyz") == "xyz"
    assert twttr.shorten("bcdfg") == "bcdfg"
    assert twttr.shorten("rhythm") == "rhythm"


def test_shorten_empty_string():
    """Test with empty string"""
    assert twttr.shorten("") == ""


def test_shorten_with_numbers_and_special_chars():
    """Test that numbers and special characters are preserved"""
    assert twttr.shorten("hello123") == "hll123"
    assert twttr.shorten("test!@#$") == "tst!@#$"
    assert twttr.shorten("hi-there") == "h-thr"


def test_shorten_single_char():
    """Test with single characters"""
    assert twttr.shorten("a") == ""
    assert twttr.shorten("b") == "b"
    assert twttr.shorten("E") == ""
    assert twttr.shorten("X") == "X"

