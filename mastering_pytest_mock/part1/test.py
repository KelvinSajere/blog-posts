import pytest
from main import Cloth, calculate_total,validate_promo, main
from contextlib import nullcontext as does_not_raise

def test_calculate_total():
    """
    Test that the total is calculated correctly
    """
    total = calculate_total(30)
    # 30 - (discount * price) == 30 - (10/100 * 30) = 30 - 3 = 27
    assert total == 27


@pytest.mark.parametrize("input_size,input_color,expected_price, expected_size, expected_color", [
    ("S", "Green",29.99,"S", "Green"),    # Test case 1
    ("S", "Green",29.99,"S", "Green"),      # Test case 2
    ("S", "Green",29.99,"S", "Green"),      # Test case 3
])
def test_cloth_with_valid_sizes(input_size,input_color,expected_price, expected_size, expected_color):
    """
    Test that we allow standard sizes and we are able to create the object
    """
    
    cloth = Cloth(input_size,input_color)
    assert cloth.size == expected_size
    assert cloth.color == expected_color
    assert cloth.price == expected_price

def test_invalid_size():
    with pytest.raises(Exception, match="Invalid Size, Please enter S, M , L"):
        Cloth("Small","Green")

def test_cloth_to_str():
    cloth = Cloth("S","Green")
    assert str(cloth) == "size : S, color:Green"


@pytest.mark.parametrize("input, behavior", [
    ("Xasd1q2341", does_not_raise()),    # Test case 1
    ("Casqwe12&", does_not_raise()),      # Test case 2
    ("as&*&*HAG", does_not_raise()),      # Test case 3
])
def test_validate_valid_promo_code(input, behavior):
    with behavior:
        validate_promo(input)

def test_validate_invalid_promo_code():
    with pytest.raises(Exception, match="Invalid Promo Code"):
        validate_promo("Invalid_Promo_code")
        