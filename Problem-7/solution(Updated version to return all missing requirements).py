#Use manual checks (any() and string methods)
# check all conditions and return all the issues in one go — not just the first one.
def is_valid_password(password):
    errors = []

    # 1. Check length
    if len(password) < 8:
        errors.append("Password must be at least 8 characters long.")
    
    # 2. Check for at least one uppercase letter
    if not any(char.isupper() for char in password):
        errors.append("Password must have at least one uppercase letter.")
    
    # 3. Check for at least one lowercase letter
    if not any(char.islower() for char in password):
        errors.append("Password must have at least one lowercase letter.")
    
    # 4. Check for at least one digit
    if not any(char.isdigit() for char in password):
        errors.append("Password must have at least one digit.")
    
    # 5. Check for at least one special character
    special_characters = "!@#$%^&*()-_=+[]{};:,.<>?/\\|"
    if not any(char in special_characters for char in password):
        errors.append("Password must have at least one special character.")
    
    # Return result
    if errors:
        return "\n".join(errors)
    else:
        return "Password is valid!"

password_input = input("Enter the password: ")
print(is_valid_password(password_input))