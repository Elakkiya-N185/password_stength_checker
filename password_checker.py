import string

def check_password(password):
    score = 0
    tips = []

    if len(password) >= 8:
        score += 1
    else:
        tips.append("Use at least 8 characters")

    if any(c.isupper() for c in password):
        score += 1
    else:
        tips.append("Add uppercase letters")

    if any(c.islower() for c in password):
        score += 1
    else:
        tips.append("Add lowercase letters")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        tips.append("Add numbers")

    if any(c in string.punctuation for c in password):
        score += 1
    else:
        tips.append("Add special characters")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    print("\nPassword strength:", strength)

    if tips:
        print("Suggestions:")
        for tip in tips:
            print("-", tip)

password = input("Enter a test password: ")
check_password(password)
