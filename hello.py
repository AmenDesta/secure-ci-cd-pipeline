def greet(name="Secure World!"):
    message = f"Hello, {name}"
    print(message)
    return message


def add(a, b):
    return a + b


def divide(a, b):
    return a / b


# Simulated secret for Gitleaks to catch
# SECRET_ACCESS = "12345"
# Extra blank line below to trigger Flake8 rule
