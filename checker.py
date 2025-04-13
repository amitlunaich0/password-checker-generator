# checker.py
import re

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include numbers.")

    if re.search(r"[!@#$%^&*()_+=\-]", password):
        score += 1
    else:
        feedback.append("Include special symbols.")

    return score, feedback
