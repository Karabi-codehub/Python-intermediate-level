# Use regular expressions (regex) — a pattern-matching method.
import re

def is_valid_password(password):
    errors = []

    # 1. Check length
    if len(password) < 8:
        errors.append("Password must be at least 8 characters long.")

    # 2. Check for uppercase letter
    if not re.search(r"[A-Z]", password):
        errors.append("Password must have at least one uppercase letter.")

    # 3. Check for lowercase letter
    if not re.search(r"[a-z]", password):
        errors.append("Password must have at least one lowercase letter.")

    # 4. Check for digit
    if not re.search(r"[0-9]", password):
        errors.append("Password must have at least one digit.")

    # 5. Check for special character
    if not re.search(r"[!@#$%^&*()\-_=+\[\]{};:,.<>?/\\|]", password):
        errors.append("Password must have at least one special character.")

    # Final decision
    if errors:
        return "\n".join(errors)  # Return all collected error messages
    else:
        return "Password is valid!"

# Ask the user for input
user_input = input("Enter a strong password: ")
print(is_valid_password(user_input))
