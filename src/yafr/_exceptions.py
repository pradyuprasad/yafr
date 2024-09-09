from abc import ABC, abstractmethod


class FredAPIError(Exception, ABC):
    """Abstract base class for all FRED API errors."""

    @abstractmethod
    def __init__(self, message: str = None):
        self.message = message or "An error occurred with the FRED API."
        super().__init__(self.message)


class BadRequestError(FredAPIError):
    """Exception raised for a 400 Bad Request error."""

    def __init__(self, message: str = None):
        default_message = "Bad Request. Please check the API request."
        super().__init__(message or default_message)


class NotFoundError(FredAPIError):
    """Exception raised for a 404 Not Found error."""

    def __init__(self, message: str = None):
        default_message = "Resource not found."
        super().__init__(message or default_message)


class LockedError(FredAPIError):
    """Exception raised for a 423 Locked error."""

    def __init__(self, message: str = None):
        default_message = "The requested resource is locked."
        super().__init__(message or default_message)


class TooManyRequestsError(FredAPIError):
    """Exception raised for a 429 Too Many Requests error."""

    def __init__(self, message: str = None):
        default_message = "Rate limit exceeded. Please try again later."
        super().__init__(message or default_message)


class InternalServerError(FredAPIError):
    """Exception raised for a 500 Internal Server Error."""

    def __init__(self, message: str = None):
        default_message = "Internal Server Error. Something went wrong on the server."
        super().__init__(message or default_message)


class UnhandledAPIError(FredAPIError):
    """Exception raised for unhandled API errors."""

    def __init__(self, message: str = None):
        default_message = "An unhandled API error occurred."
        super().__init__(message or default_message)
