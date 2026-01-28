import re

# List of test passwords
passwords = ["abc", "123456", "Pass@123", "Admin"]

def validate_password(pwd):
    """
    Validates a password based on:
    - Minimum length of 8 characters
    - At least one number
    - At least one special character
    """
    if len(pwd) < 8:
        return False, "Less than 8 characters"

    if not re.search(r"\d", pwd):
        return False, "No number found"

    if not re.search(r"[@#$%^&*!]", pwd):
        return False, "No special character found"

    return True, "Valid password"

print("\nPassword Strength Validation Report")
print("----------------------------------")

for pwd in passwords:
    status, reason = validate_password(pwd)
    if status:
        print(f"{pwd} => PASS ({reason})")
    else:
        print(f"{pwd} => FAIL ({reason})")
