import requests
from typing import Dict, Any
from dotenv import load_dotenv
import os
from ._exceptions import (
    BadRequestError,
    FredAPIError,
    InternalServerError,
    LockedError,
    NotFoundError,
    TooManyRequestsError,
    UnhandledAPIError,
)


class FredClient:
    def __init__(self, api_key: str = None) -> None:
        load_dotenv()
        self.api_key = api_key or os.environ.get("FRED_API_KEY")
        if not self.api_key:
            raise ValueError(
                "API key must be provided or set as FRED_API_KEY environment variable"
            )

        self.base_url = "https://api.stlouisfed.org/fred"

    def call_api(self, endpoint: str, **kwargs) -> Dict[str, Any]:
        """Make the API request and handle potential errors."""
        params = kwargs.get("params", {})
        params["api_key"] = self.api_key
        params["file_type"] = "json"

        url = f"{self.base_url}/{endpoint}"

        try:
            response = requests.get(url, params=params, timeout=10)
        except requests.exceptions.RequestException as e:
            raise UnhandledAPIError(
                f"API request failed due to a network issue: {str(e)}"
            )

        if response.status_code != 200:
            self._handle_api_error(response)

        return response.json()

    def _handle_api_error(self, response: requests.Response) -> None:
        """Handle API errors by raising custom exceptions based on the status code."""
        status_code = response.status_code

        try:
            error_message = response.json().get("error_message", "Unknown error")
        except ValueError:
            # If the response is not JSON (might be XML), fall back to text
            error_message = response.text or "Unknown error"

        if status_code == 400:
            raise BadRequestError(error_message)
        elif status_code == 404:
            raise NotFoundError(error_message)
        elif status_code == 423:
            raise LockedError(error_message)
        elif status_code == 429:
            raise TooManyRequestsError(error_message)
        elif status_code == 500:
            raise InternalServerError(error_message)
        else:
            raise UnhandledAPIError(f"Unhandled error: {status_code} - {error_message}")

    def _test_api_key(self) -> None:
        """Test the API key by calling the FRED API."""
        try:
            self.call_api("series/observations", series_id="GDP")
        except BadRequestError:
            return False
        except FredAPIError as e:
            raise e
        return True
