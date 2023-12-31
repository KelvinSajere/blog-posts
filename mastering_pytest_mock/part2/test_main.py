from logging import LogRecord
import logging
import os
from unittest.mock import MagicMock, patch
import pytest
from main import Cloth, calculate_total,validate_promo, record_transaction, purchase
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

# Set up a reusable cloth object we can use
@pytest.fixture()
def set_up_cloth():
    return Cloth("S","Green")


@pytest.fixture()
def tear_down():
    yield
    if os.path.exists("transaction.log"):
        os.remove("transaction.log")

# use the set up fixture 
def test_record_transaction(caplog:pytest.LogCaptureFixture,set_up_cloth, tear_down):
    
    caplog.set_level(logging.INFO, logger="Best Ecommerce")
    # Call the record_transaction method with Cloth("S","Green") and 100
    # We call this twice so we can generate 2 different log messages. This helps us to test that the logs is always appended to the transaction.log file if any exists
    record_transaction(set_up_cloth, 100)
    record_transaction(set_up_cloth, 200)
    
    # Get the first log message
    log_record_1:LogRecord = caplog.records[0]
    log_record_2:LogRecord = caplog.records[1]
    
    # Check the log level is correct
    assert log_record_1.levelname == "INFO"
    assert log_record_1.message == "Purchased size : S, color:Green for a total of :$100"
    assert log_record_2.message == "Purchased size : S, color:Green for a total of :$200"
    
    # Test that the file is created
    assert os.path.exists("transaction.log")

    # Test that the logs write to the file
    with open("transaction.log", mode="r") as file :
        lines = file.readlines()
        assert lines[0] == log_record_1.asctime+" - Best Ecommerce - INFO - Purchased size : S, color:Green for a total of :$100\n"
        assert lines[1] == log_record_2.asctime+" - Best Ecommerce - INFO - Purchased size : S, color:Green for a total of :$200\n"

@patch("main.record_transaction")
@patch("main.calculate_total")
@patch("main.validate_promo")
def test_purchase(validate_promo_mock:MagicMock, calculate_total_mock:MagicMock, record_transaction_mock:MagicMock, set_up_cloth, tear_down):
    
    # Mock the calculate_total method
    calculate_total_mock.return_value = 10

    # Call the purchase function
    purchase(set_up_cloth, "PROMO_CODE")

    # Spy the validate_promo for any interaction with the correct promo_code i passed into the purchase function
    validate_promo_mock.assert_called_once_with("PROMO_CODE")
    
    # Spy the record transaction for any interaction
    record_transaction_mock.assert_called_once_with(set_up_cloth, 10)
