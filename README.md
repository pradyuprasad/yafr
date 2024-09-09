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

## Roadmap and Progress

| Feature Name | Status  |
|--------------|---------|
| Basic API Client   | In Progress  |
| Series    | Planned|
| Categories | Planned|
| Releases | Planned|
| Sources | Planned|
| Tags | Planned|

## Why Yet Another FRED Client?

Most existing FRED clients suffer from a few common problems. YAFR aims to address these issues and provide a more robust, user-friendly, and maintainable solution:

1. **Lack of Data Safety and Validation**: Many clients don't provide strong type checking or data validation, leading to potential runtime errors and inconsistent data structures. YAFR leverages Pydantic for:
   - Automatic data parsing and validation
   - Clear, informative error messages for invalid data
   - Self-documenting code through type hints

2. **Inconsistent API Coverage**: Some clients only implement a subset of the FRED API, limiting their usefulness. YAFR aims to provide:
   - Comprehensive coverage of all FRED API endpoints
   - Consistent interface across all API sections (Categories, Releases, Series, Sources, Tags)

3. **Poor Error Handling**: Existing clients often don't handle API errors gracefully, making debugging difficult. YAFR focuses on:
   - Comprehensive error handling for various API responses
   - Clear distinction between client-side and server-side errors
   - Informative error messages to aid in troubleshooting

4. **Outdated or Unmaintained Codebases**: Some existing clients are no longer actively maintained, leading to compatibility issues with newer Python versions or API changes. YAFR is committed to:
   - Regular updates and maintenance
   - Compatibility with modern Python versions
   - Keeping pace with any changes to the FRED API
