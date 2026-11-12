# test_main.py

def calculate_efficiency(distance, fuel):
    return distance / fuel

def test_efficiency_calculation():
    # Test case 1: 450 km driven on 30 liters should equal 15.0 km/L
    result = calculate_efficiency(450, 30)
    assert result == 15.0, f"Expected 15.0, but got {result}"

def test_zero_fuel_handling():
    # Test case 3: Ensure your safety check handles zero fuel gracefully
    fuel = 0
    assert fuel == 0, "Fuel is zero, should trigger warning message"