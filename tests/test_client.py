import unittest
from unittest.mock import patch
import os
from src.yafr._client import FredClient
from src.yafr._exceptions import FredAPIError, BadRequestError


class TestFredClientInitialization(unittest.TestCase):
    @patch.dict(os.environ, {"FRED_API_KEY": "test_key"})
    @patch("src.yafr._client.FredClient.call_api")
    def test_successful_initialization(self, mock_call_api):
        mock_call_api.return_value = {"some": "data"}
        client = FredClient()
        self.assertEqual(client.api_key, "test_key")
        self.assertEqual(client.base_url, "https://api.stlouisfed.org/fred")
        mock_call_api.assert_called_once_with("category", category_id="125")

    @patch("src.yafr._client.load_dotenv")
    def test_missing_api_key(self, mock_load_dotenv):
        mock_load_dotenv.return_value = {}  # Simulate no .env file
        with patch.dict(os.environ, {}, clear=True):
            with self.assertRaises(ValueError) as context:
                FredClient()
            self.assertIn("API key must be provided", str(context.exception))

    @patch.dict(os.environ, {"FRED_API_KEY": "invalid_key"})
    @patch("src.yafr._client.FredClient.call_api")
    def test_invalid_api_key(self, mock_call_api):
        mock_call_api.side_effect = BadRequestError("Invalid API key")
        with self.assertRaises(ValueError) as context:
            FredClient()
        self.assertEqual(str(context.exception), "Invalid API key")

    @patch.dict(os.environ, {"FRED_API_KEY": "valid_key"})
    @patch("src.yafr._client.FredClient.call_api")
    def test_api_error_during_initialization(self, mock_call_api):
        mock_call_api.side_effect = FredAPIError("API Error")
        with self.assertRaises(FredAPIError) as context:
            FredClient()
        self.assertEqual(str(context.exception), "API Error")


if __name__ == "__main__":
    unittest.main()
