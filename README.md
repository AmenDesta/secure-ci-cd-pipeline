Secure CI/CD Pipeline with GitHub Actions
Overview
This project demonstrates a secure CI/CD pipeline using GitHub Actions. It automates testing, linting, and secret scanning to ensure code quality and prevent credential leaks before deployment.

Features:

Automated Testing with pytest

Code Quality Enforcement using flake8

Secret Scanning via gitleaks

Fail-Fast Logic: blocks merges if tests fail or secrets are detected

Secure Workflow Design using GitHub’s encrypted secrets

Project Structure
Code
secure-ci-cd-pipeline/
├── .github/
│   └── workflows/
│       └── secure-pipeline.yml
├── hello.py
├── test_hello.py
├── requirements.txt
└── README.md

How It Works

On every push or pull request to main, GitHub Actions:

Sets up Python 3.11

Installs dependencies

Runs flake8 to check code style

Runs pytest to validate functionality

Scans for secrets using gitleaks

If any step fails, the pipeline blocks the commit from merging.

Setup Instructions
bash
# Clone the repo
git clone https://github.com/AmenDesta/secure-ci-cd-pipeline.git
cd secure-ci-cd-pipeline

# Install dependencies
pip install -r requirements.txt

# Run tests locally
pytest

# Run linting locally
flake8 .
Sample Output
✅ Tests passed ❌ Secret detected in hello.py line 12 ❌ Linting failed: missing docstring in test_hello.py

Why It Matters
This project showcases the ability to:

⦁	Automate secure software delivery
⦁	Enforce code hygiene
⦁	Integrate DevSecOps principles into everyday development
