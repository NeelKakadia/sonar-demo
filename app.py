import os

def get_user(id):
    # Bad practice - SQL injection vulnerability
    query = "SELECT * FROM users WHERE id = " + id
    return query

def divide(a, b):
    # Bug - no check for division by zero
    return a / b

password = "hardcoded_password_123"  # Security hotspot
