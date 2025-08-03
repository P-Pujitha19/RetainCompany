import re

def is_valid_email(email):
    # Simple regex for validating an email
    pattern = r'^\S+@\S+\.\S+$'
    return re.match(pattern, email) is not None

def validate_register_input(name, email, password):
    if not name or not email or not password:
        return False, "Name, email, and password are required"
    if not is_valid_email(email):
        return False, "Invalid email format"
    if len(password) < 6:
        return False, "Password must be at least 6 characters"
    return True, ""

def validate_login_input(email, password):
    if not email or not password:
        return False, "Email and password are required"
    if not is_valid_email(email):
        return False, "Invalid email format"
    return True, ""
