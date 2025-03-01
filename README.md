# QA Automation Repository

## Overview
This repository contains an automated testing framework using Selenium in Python. It follows the **Page Object Model (POM)** for organizing test scripts efficiently. The framework is built with **pytest** as the test runner and **Allure** for reporting. 

### Repository Structure
This project is structured based on different websites. The main directory follows this pattern:

```
QA-practice/
  ├── <website_name>/
      ├── POM/  # Page Object Model classes for different web pages
      ├── tests/
          ├── tests/test_case/  # Individual test cases
          ├── tests/test_suite/  # Test suites that group multiple test cases
      ├── report/  # Allure reports are stored here (--alluredir=report)
      ├── pyproject.toml  # Poetry configuration
      ├── poetry.lock  # Poetry lock file
```

## Known Issues
- A recent update involving **ActionChains** has caused most test cases to break.
- There are some redundant files that may need cleanup.

## Prerequisites
- Python (Recommended: 3.8 or later)
- Poetry package manager

## Installation
First, go to what website QA automation you're trying to clone, then clone the repository and install dependencies using **Poetry**:

```sh
# Clone the repository
git clone <repo_url>
cd <repo_directory>

# Install dependencies using Poetry
poetry install
```

## Running Tests
You can execute test cases using **pytest** and generate Allure reports.

```sh
poetry run pytest <path_to_test_file> --alluredir=report
```

Example:
```sh
poetry run pytest tests/test_case/test_sample.py --alluredir=report
```

## Generating and Viewing Allure Reports
After running tests, generate and serve the Allure report:

```sh
allure serve report/
```

This will open the report in your default web browser.

## Contribution Guide
- Ensure tests pass before pushing changes.
- Remove redundant files if identified.
- Fix ActionChains-related issues in test cases.
- Follow POM structure and maintain modularity.

## License
This project is licensed under [Your License Here].

