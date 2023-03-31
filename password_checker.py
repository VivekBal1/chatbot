import re

def is_strong_password(password):
    # at least 8 characters
    if len(password) < 8:
        return False

    # at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False

    # at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False

    # at least one digit
    if not re.search(r'\d', password):
        return False

    # at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False

    return True

def validatePassword():
    print("Chatbot: Please enter a password: ")
    password = input("You: ")
    msg = ""
    if is_strong_password(password):
        msg = "Password is strong!"
    else:
        msg = "Password is not strong enough."
    return msg

