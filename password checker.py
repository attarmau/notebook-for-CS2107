# Question: "You have a text file containing a list of passwords that needs to be checked for their strength. Implement a Python program that reads the file and determines the strength of each password based on the following criteria:

- The password must be at least 8 characters long.
- It must contain a combination of letters (both uppercase and lowercase), numbers, and special characters (!, @, #, $, %, ^, &, *).
- It should not contain common words or patterns commonly used in passwords (such as "password", "12345678", "qwerty", etc.).
- The program should output the strength of each password as 'Weak', 'Medium', or 'Strong'."

import re
def check_password_strength(password):
    # Minimum length check
    if len(password) < 8:
        return 'Weak'
    # Character combination check
    if not re.search(r"[a-z]", password) or not re.search(r"[A-Z]", password) or \
            not re.search(r"\d", password) or not re.search(r"[!@#$%^&*]", password):
        return 'Weak'

    # Common words or patterns check
    common_patterns = ['password', '12345678', 'qwerty']
    for pattern in common_patterns:
        if pattern in password:
            return 'Weak'
    return 'Strong'
# Read passwords from a text file
with open('passwords.txt', 'r') as file:
    passwords = file.readlines()

# Check strength for each password
for password in passwords:
    password = password.strip()  # Remove newline character if present
    strength = check_password_strength(password)
    print(f"Password: {password}\tStrength: {strength}")
