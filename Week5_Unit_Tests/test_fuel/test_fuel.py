import fuel

def test_fuel():
    """Test fuel function with various inputs"""
    assert fuel.fuel(1, 2) == 50.0
    assert fuel.fuel(1, 4) == 25.0
    assert fuel.fuel(3, 4) == 75.0
    assert fuel.fuel(0, 1) == 0.0
    assert fuel.fuel(1, 1) == 100.0
    
    # Test with larger numbers
    assert fuel.fuel(50, 200) == 25.0
    assert fuel.fuel(75, 300) == 25.0
    
    # Test with edge cases
    try:
        fuel.fuel(1, 0)
        assert False, "Expected ValueError for division by zero"
    except ValueError:
        pass
    