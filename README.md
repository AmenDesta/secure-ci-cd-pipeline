![CI Status](https://github.com/AmenDesta/secure-ci-cd-pipeline/actions/workflows/secure-pipeline.yml/badge.svg)

Secure CI/CD Pipeline with GitHub Actions

Overview
This project demonstrates a secure CI/CD pipeline using GitHub Actions. It automates testing, linting, and secret scanning to ensure code quality and prevent credential leaks before deployment.

Features
Automated testing with pytest

Code quality enforcement using flake8

Secret scanning via gitleaks

Fail-fast logic: blocks merges if tests fail or secrets are detected

Secure workflow design leveraging GitHub’s encrypted secrets

Project Structure
secure-ci-cd-pipeline/ ├── .github/ │ └── workflows/ │ └── secure-pipeline.yml ├── hello.py ├── test_hello.py ├── requirements.txt └── README.md

How It Works
On every push or pull request to main, GitHub Actions:

Sets up Python 3.11

Installs dependencies

Runs flake8 to check code style

Runs pytest to validate functionality

Scans for secrets using gitleaks

If any step fails, the pipeline blocks the commit from merging.

Setup Instructions
Clone the repo: git clone https://github.com/AmenDesta/secure-ci-cd-pipeline.git cd secure-ci-cd-pipeline

Install dependencies: pip install -r requirements.txt

Run tests locally: pytest

Run linting locally: flake8 .

Sample Output
✅ Tests passed

❌ Secret detected in hello.py line 12

❌ Linting failed: missing docstring in test_hello.py

Why It Matters
This project showcases the ability to:

Automate secure software delivery

Enforce code hygiene

Integrate DevSecOps principles into everyday development

About the Author
This project was developed by Amen Desta, Software Development and Security BA. Amen specializes in building secure workflows, integrating DevSecOps principles, and ensuring professional code quality through automation and CI/CD best practices.
