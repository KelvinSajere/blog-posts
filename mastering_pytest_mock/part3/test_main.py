import pytest
from unittest.mock import AsyncMock, patch
from main import long_computation

@pytest.mark.asyncio
async def test_main():
    result = await long_computation()
    assert result == "DONE"


@pytest.mark.asyncio  
@patch("main.asyncio.sleep")
async def test_main_with_mock(sleep_mock:AsyncMock):
    """
    How to mock async function. 
    Here we try to mock the asyncio.sleep 
    Remeber, we mock where the function is called , i.e main.asyncio.sleep 
    
    """
    sleep_mock.return_value = None
    result = await long_computation()
    sleep_mock.assert_awaited_once()
    assert result == "DONE"