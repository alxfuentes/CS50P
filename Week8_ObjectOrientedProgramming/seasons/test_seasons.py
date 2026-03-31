from datetime import date

from seasons import minutes_passed, to_words


def test_passed():
    birthdate = date(2000, 1, 1)
    expected = (date.today() - birthdate).days * 24 * 60
    assert minutes_passed(birthdate) == expected


def test_to_words():
    assert to_words(0) == "zero"
    assert to_words(1) == "one"
    assert to_words(12) == "twelve"
    assert to_words(101) == "one hundred one"
    assert to_words(1_000_000) == "one million"
    assert to_words(1_234_567) == "one million, two hundred thirty-four thousand, five hundred sixty-seven"
