import re

def check_password_strength(password):
    score = 0

    # Length
    if len(password) >= 8:
        score += 1

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1

    # Number
    if re.search(r"\d", password):
        score += 1

    # Special Character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    print("\nPassword Analysis")
    print("------------------")
    print(f"Length: {len(password)}")

    if score == 5:
        print("Strength: Very Strong")
    elif score == 4:
        print("Strength: Strong")
    elif score == 3:
        print("Strength: Medium")
    elif score == 2:
        print("Strength: Weak")
    else:
        print("Strength: Very Weak")

    # Suggestions
    print("\nSuggestions:")
    if len(password) < 8:
        print("- Use at least 8 characters.")
    if not re.search(r"[A-Z]", password):
        print("- Add at least one uppercase letter.")
    if not re.search(r"[a-z]", password):
        print("- Add at least one lowercase letter.")
    if not re.search(r"\d", password):
        print("- Add at least one number.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        print("- Add at least one special character.")

password = input("Enter your password: ")
check_password_strength(password)
