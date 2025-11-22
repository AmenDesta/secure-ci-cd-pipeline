def greet(name="Secure World"):
    return f"Hello, {name}!"


def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# Simulated secret for Gitleaks to catch
# AWS_SECRET_ACCESS_KEY = "AKIAFAKEKEY1234567890"

# Extra blank line below to trigger flake8 W391