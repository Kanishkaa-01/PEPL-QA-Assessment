# PEPL QA Assessment

## Project Overview

This repository contains the solutions for the three-level Testing / QA technical assessment.

The assessment focuses on API automation, browser-based testing, and differential testing through automated test frameworks.

## Repository Structure

```text
PEPL_QA_Assessment/
│
├── .github/
│   └── workflows/
│       └── level1-api-tests.yml
│
├── level1-restful-booker/
│   ├── docs/
│   │   └── Test_Plan.docx
│   ├── schemas/
│   │   └── booking_schema.json
│   ├── tests/
│   ├── utils/
│   ├── conftest.py
│   ├── pytest.ini
│   └── requirements.txt
│
├── level2-toolshop/
│   ├── bug-reports/
│   │   ├── BUG-001.md
│   │   ├── ...
│   │   └── BUG-011.md
│   ├── screenshots/
│   ├── tests/
│   ├── utils/
│   ├── conftest.py
│   ├── pytest.ini
│   ├── requirements.txt
│   └── README.md
│
├── level3-toml-fuzzing/
│
└── README.md
```

---

## Level 1 – Restful Booker REST API

**Status: Completed**

### Overview

Developed an automated API testing framework using Python and Pytest to validate the Restful Booker REST API.

### Features

- Reusable API client class.
- Dynamic test-data builder.
- Authentication testing using token cookies and Basic Authentication.
- Positive and negative API testing.
- Booking creation, retrieval, full update, partial update and deletion.
- Complete booking lifecycle validation.
- JSON Schema response validation.
- Parameterized negative test cases.
- API response-time validation.
- Configurable application base URL.
- HTML test reporting.
- GitHub Actions CI integration.

### Technology Stack

- Python 3.11
- Pytest
- Requests
- JSON Schema
- pytest-html
- Git and GitHub
- GitHub Actions

### Test Plan

The Level 1 test plan is available at:

`level1-restful-booker/docs/Test_Plan.docx`

### Setup Instructions

**1. Clone the repository**

```bash
git clone https://github.com/Kanishkaa-01/PEPL-QA-Assessment.git
cd PEPL-QA-Assessment
```

**2. Navigate to Level 1**

```bash
cd level1-restful-booker
```

**3. Create a virtual environment**

```bash
python -m venv venv
```

**4. Activate the virtual environment**

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

**5. Install dependencies**

```bash
pip install -r requirements.txt
```

### Start the Restful Booker Application

The test suite requires the Restful Booker API to be running locally.

Open a separate terminal and execute:

```bash
git clone https://github.com/mwinteringham/restful-booker.git
cd restful-booker
npm ci
npm start
```

The application runs at:

`http://localhost:3001`

Verify API availability:

```bash
curl http://localhost:3001/ping
```

Expected response: `201 Created`.

### Run Automated Tests

From the `level1-restful-booker` directory:

```bash
pytest -v
```

### Generate HTML Test Report

```bash
pytest -v --html=reports/report.html --self-contained-html
```

The generated report will be available at:

`level1-restful-booker/reports/report.html`

### Configure Base URL

The application URL can be configured using the `BASE_URL` environment variable.

PowerShell:

```powershell
$env:BASE_URL="http://localhost:3001"
```

### CI/CD Integration

GitHub Actions automatically:

1. Checks out the assessment repository.
2. Sets up Node.js and Python.
3. Clones and starts the Restful Booker application.
4. Installs Python dependencies.
5. Executes the automated test suite.
6. Generates and uploads the HTML test report.

**Verified CI Execution:** 24 tests passed, 0 failed.

---

## Level 2 – Toolshop Web Application

**Status: Completed**

### Overview

Developed a browser-based automated testing framework using Python, Playwright and Pytest to test the Toolshop e-commerce web application.

The testing approach compares two versions of the application:

- **Reference application:** https://practicesoftwaretesting.com
- **Bug-injected application:** https://with-bugs.practicesoftwaretesting.com

The same automated test suite can be executed against both applications to identify differences in application behaviour and detect defects.

### Features

- Homepage and navigation validation.
- Product listing validation.
- Product search functionality.
- Product sorting validation.
- Product details page validation.
- Add-to-cart functionality.
- Shopping cart quantity update.
- Shopping cart product removal.
- Contact form field validation.
- Contact form submission testing.
- Configurable application base URL.
- Automated comparison between reference and bug-injected applications.
- Defect documentation with reproduction steps, expected and actual results, severity, and screenshots.

### Bug Reports

A total of **11 bug reports** are documented in:

`level2-toolshop/bug-reports/`

Screenshots supporting selected defects are available in:

`level2-toolshop/screenshots/`

### Technology Stack

- Python 3.11
- Playwright
- pytest
- pytest-playwright
- pytest-html
- Git and GitHub

### Setup Instructions

**1. Navigate to Level 2**

From the repository root:

```bash
cd level2-toolshop
```

**2. Create a virtual environment**

```bash
python -m venv venv
```

**3. Activate the virtual environment**

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

**4. Install dependencies**

```bash
pip install -r requirements.txt
```

**5. Install Playwright browser**

```bash
playwright install chromium
```

### Configure Application URL

The test suite uses the reference application by default.

To execute tests against the bug-injected application, set the `BASE_URL` environment variable.

**Reference application – PowerShell**

```powershell
$env:BASE_URL="https://practicesoftwaretesting.com"
```

**Bug-injected application – PowerShell**

```powershell
$env:BASE_URL="https://with-bugs.practicesoftwaretesting.com"
```

### Run Automated Tests

Run the complete test suite:

```bash
pytest -v
```

Run tests against the reference application:

```powershell
$env:BASE_URL="https://practicesoftwaretesting.com"
pytest -v
```

Run tests against the bug-injected application:

```powershell
$env:BASE_URL="https://with-bugs.practicesoftwaretesting.com"
pytest -v
```

### Generate HTML Test Report

```bash
pytest -v --html=reports/report.html --self-contained-html
```

The generated report will be available at:

`level2-toolshop/reports/report.html`

### Project Documentation

Detailed setup instructions, test execution details and bug reports are available in the `level2-toolshop` directory.

---

## Level 3 – TOML Differential Fuzzing

**Status: Not yet implemented**

### Planned Scope

- Differential testing using `toml` and Python's `tomllib`.
- Property-based testing using Hypothesis.
- TOML document generation.
- Parser behaviour comparison.
- Failure minimization and defect analysis.
- Bug reproduction and proposed fixes.

---

## Author

**Kanishkaa**

GitHub: https://github.com/Kanishkaa-01