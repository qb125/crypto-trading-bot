# tests/test_main.py
import os
from unittest.mock import patch


@patch.dict(os.environ, {"COINBASE_API_KEY": "test_key", "COINBASE_API_SECRET": "test_secret"})
def test_load_env_variables():
    assert os.getenv("COINBASE_API_KEY") == "test_key"
    assert os.getenv("COINBASE_API_SECRET") == "test_secret"
