# tests/test_utils.py
from unittest.mock import MagicMock
from utils import retry_on_failure

def test_retry_on_failure_success():
    mock_func = MagicMock(side_effect=[Exception("Error"), 42])  # Fail once, succeed next
    result = retry_on_failure(mock_func, retries=3, delay=1)
    assert result == 42
    assert mock_func.call_count == 2

def test_retry_on_failure_failure():
    mock_func = MagicMock(side_effect=Exception("Error"))
    with pytest.raises(Exception, match="Error"):
        retry_on_failure(mock_func, retries=2, delay=1)
    assert mock_func.call_count == 2
