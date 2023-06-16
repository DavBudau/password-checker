import re
import string

def calculate_password_strength(password):
    # Define the scoring criteria and their weights
    criteria = {
        r".{12,}": 5,                      # Minimum length of 12 characters
        r"(?=.*\d)": 2,                     # At least one digit
        r"(?=.*[a-z])": 2,                   # At least one lowercase letter
        r"(?=.*[A-Z])": 2,                   # At least one uppercase letter
        r"(?=.*[!@#$%^&*(),.?\":{}|<>])": 3  # At least one special character
    }

    # Check if the password is a common password
    if is_common_password(password):
        return 0

    # Calculate the score based on the criteria
    score = 0
    for pattern, value in criteria.items():
        if re.search(pattern, password):
            score += value

    # Apply additional variations to the score
    score += check_complexity_variations(password)

    return score

def is_common_password(password):
    common_passwords = ["password", "123456", "qwerty", "letmein"]  # Add more common passwords as needed

    if password.lower() in common_passwords:
        return True

    return False

def check_complexity_variations(password):
    variations = 0

    # Check for consecutive characters
    consecutive_patterns = [r"0123456789", r"abcdefghijklmnopqrstuvwxyz", r"ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    for pattern in consecutive_patterns:
        if re.search(pattern, password):
            variations -= 2

    # Check for repeating characters
    repeating_pattern = r"(\w)\1{2,}"
    if re.search(repeating_pattern, password):
        variations -= 3

    # Check for sequential patterns
    sequential_pattern = fr"({'|'.join([re.escape(s) for s in string.ascii_lowercase])})"
    if re.search(sequential_pattern, password.lower()):
        variations -= 3

    return variations

def check_password_strength(password):
    score = calculate_password_strength(password)

    if score >= 15:
        return "Password is very strong."
    elif score >= 10:
        return "Password is strong."
    elif score >= 7:
        return "Password is moderate."
    elif score >= 1:
        return "Password is weak."
    else:
        return "Password is too common or extremely weak."

# Test the function
password = input("Enter a password: ")
result = check_password_strength(password)
print(result)
