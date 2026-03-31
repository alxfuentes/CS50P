import um

def test_um_lowercase():
    assert um.count("hello, um, world!") == 1

def test_um_uppercase():
    assert um.count("hello, UM, world!") == 1

def test_no_um():
    assert um.count("hello world") == 0

def test_words_with_um():
    # Test words that start with, contain, or end with "um"
    # Assuming the function counts "um" as a separate word, not within other words
    assert um.count("umbrella album drum") == 0  # No standalone "um"
    # If the function is supposed to count standalone "um", these should be 0