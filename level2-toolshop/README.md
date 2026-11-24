# Level 2 – Toolshop Web Application Testing

## 1. Project Overview

This project focuses on manual and automated testing of the Toolshop e-commerce web application using Python, Playwright and Pytest.

The objective is to identify functional and UI defects in the bug-injected application by comparing its behaviour with the correct reference application.

The same automated test suite is executed against both applications to identify differences in functionality and verify expected behaviour.

## 2. Application Under Test

| Application | URL |
|---|---|
| Bug-injected application | https://with-bugs.practicesoftwaretesting.com |
| Reference application | https://practicesoftwaretesting.com |

The reference application is used as the expected-behaviour baseline.

## 3. Technology Stack

- Programming Language: Python 3.11
- Automation Framework: Playwright
- Test Framework: Pytest
- Reporting: Pytest HTML
- Browser: Chromium
- Version Control: Git and GitHub
- IDE: Visual Studio Code

## 4. Project Structure

```text
level2-toolshop/
│
├── tests/
│   ├── test_homepage.py
│   ├── test_search.py
│   ├── test_sorting.py
│   ├── test_product_details.py
│   ├── test_product_listing.py
│   ├── test_cart.py
│   └── test_contact.py
│
├── bug-reports/
│   ├── BUG-001.md
│   ├── BUG-002.md
│   ├── BUG-003.md
│   ├── BUG-004.md
│   ├── BUG-005.md
│   ├── BUG-006.md
│   ├── BUG-007.md
│   ├── BUG-008.md
│   ├── BUG-009.md
│   ├── BUG-010.md
│   └── BUG-011.md
│
├── screenshots/
│   └── Bug evidence screenshots
│
├── utils/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## 5. Test Coverage

| Module | Test Coverage |
|---|---|
| Homepage | Homepage loading and search element visibility |
| Search | Search input, product search and nonexistent product search |
| Product Listing | Product visibility and product name validation |
| Sorting | Sorting by name and price in ascending and descending order |
| Product Details | Opening product details and verifying product information |
| Shopping Cart | Adding products, updating quantities and removing products |
| Contact Form | Form field visibility, successful submission and required field validation |

## 6. Installation and Setup

### Prerequisites

- Python 3.11 or above
- Visual Studio Code
- Git
- Internet connection

### Step 1: Navigate to the project directory

```powershell
cd level2-toolshop
```

### Step 2: Create a virtual environment

```powershell
python -m venv venv
```

### Step 3: Activate the virtual environment

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 4: Install dependencies

```powershell
pip install -r requirements.txt
```

### Step 5: Install Playwright Chromium browser

```powershell
playwright install chromium
```

## 7. Running the Automated Tests

The application URL is configured through the `BASE_URL` environment variable. The reference application is used by default.

### Run tests against the reference application

```powershell
$env:BASE_URL = "https://practicesoftwaretesting.com"
pytest -v
```

### Run tests against the bug-injected application

```powershell
$env:BASE_URL = "https://with-bugs.practicesoftwaretesting.com"
pytest -v
```

### Run individual test modules

```powershell
pytest tests/test_homepage.py -v
pytest tests/test_search.py -v
pytest tests/test_sorting.py -v
pytest tests/test_product_details.py -v
pytest tests/test_product_listing.py -v
pytest tests/test_cart.py -v
pytest tests/test_contact.py -v
```

## 8. Test Reports

HTML test reports can be generated using:

```powershell
pytest --html=report.html --self-contained-html
```

The generated report contains test execution results, including passed, failed and skipped tests.

## 9. Bug Reporting

A total of **11 individual bug reports (BUG-001 to BUG-011)** are maintained in the `bug-reports/` directory.

Each report includes:

- Bug ID and title
- Severity and priority
- Application module
- Preconditions
- Steps to reproduce
- Expected result
- Actual result
- Screenshot evidence
- Impact of the defect
- Reference application comparison, where applicable

Screenshots supporting the identified defects are maintained in the `screenshots/` directory.

## 10. Reference Application Comparison

The same automated test suite is executed against both application versions.

The comparison helps identify:

- Functional inconsistencies
- Incorrect sorting behaviour
- Form validation issues
- UI differences
- Product and cart functionality issues

Tests are evaluated against the expected behaviour observed in the reference application. A failure in the bug-injected application is investigated before being classified as a confirmed defect.

## 11. Testing Approach

The following testing activities are performed:

1. Functional testing
2. UI testing
3. Form validation testing
4. Product search testing
5. Sorting validation
6. Shopping cart testing
7. Cross-version comparison
8. Defect identification and documentation
9. Automated regression testing

## 12. Conclusion

This project demonstrates the use of Playwright and Pytest for automating web application tests and identifying software defects.

By comparing the bug-injected application with the reference application, the project aims to identify functional and interface inconsistencies, document reproducible defects and provide test evidence to support the findings.

