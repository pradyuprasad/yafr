# YAFR: Yet Another FRED Client

YAFR (Yet Another FRED Client) is a robust Python library for interacting with the Federal Reserve Economic Data (FRED) API. Built with a focus on data integrity and developer experience, YAFR leverages the power of Pydantic for data validation and strong typing.

## Key Features

1. **Pydantic Data Validation**: YAFR uses Pydantic models to ensure that all data retrieved from the FRED API is properly validated and typed. This provides:
   - Automatic data parsing and type conversion
   - Clear error messages for invalid data
   - Self-documenting code through type hints

2. **Strong Typing**: With YAFR, you get the benefits of Python's type hinting system, offering:
   - Improved code readability
   - Better IDE support with autocompletion and type checking
   - Catch potential errors at development time rather than runtime

3. **Easy-to-Use API**: YAFR provides a simple and intuitive interface to interact with FRED data, making it accessible for both beginners and experienced developers.

4. **Comprehensive Data Models**: All FRED API responses are mapped to Pydantic models, ensuring consistent and predictable data structures throughout your application.

5. **Efficient Data Handling**: YAFR optimizes data retrieval and processing, making it suitable for handling large datasets from FRED.
