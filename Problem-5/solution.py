# Import the regular expression module
import re

def is_valid_email(email):
    # Define the regular expression pattern for a valid email address
    # [a-zA-Z0-9._%+-]:Username part (before the @)
    #[a-zA-Z0-9.-]: Domain part (after the @)
    #We do not use _, %, + in the domain part because valid domain names (after the @) are more restricted than the username part.
    #Valid characters in domain names:(a-z, A-Z),(0-9),Hyphen (-),Dot (.) 

    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Use re.match to check if the pattern matches the email string
    if re.match(pattern,email):
        return True
    else:
        return False
        
print(is_valid_email("test@domain.com"))