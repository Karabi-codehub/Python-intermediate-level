#Use manual checks (any() and string methods)
def is_valid_password(password):
    # 1. Check length
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    
    # 2. Check for at least one uppercase letter
    if not any(char.isupper() for char in password):
        return "Password must have at least one uppercase letter."
    
    # 3. Check for at least one lowercase letter
    if not any(char.islower() for char in password):
        return "Password must have at least one lowercase letter."
    
    # 4. Check for at least one digit
    if not any(char.isdigit() for char in password):  # ← fixed 'nor' and 'for in char'
        return "Password must have at least one digit."
    
    # 5. Check for at least one special character
    special_characters = "!@#$%^&*()-_=+[]{};:,.<>?/\\|"
    if not any(char in special_characters for char in password):
        return "Password must have at least one special character."
    
    # If all checks pass
    return "Password is valid!"
# Get user input
password_input = input("Enter the password: ")
print(is_valid_password(password_input))