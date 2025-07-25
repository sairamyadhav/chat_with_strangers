from django.core.exceptions import ValidationError
import re

def validate_username(value):
    if not re.match(r'^[a-zA-Z0-9_]+$', value):
        raise ValidationError('Username can only contain letters, numbers, and underscores.')

    if len(value) < 3:
        raise ValidationError('Username must be at least 3 characters long.')
    
def validate_password(value):
    if len(value) < 8:
        raise ValidationError("Password must be at least 8 characters long.")

    if not re.search(r'[A-Z]', value):
        raise ValidationError("Password must contain at least one uppercase letter.")

    if not re.search(r'[a-z]', value):
        raise ValidationError("Password must contain at least one lowercase letter.")

    if not re.search(r'\d', value):
        raise ValidationError("Password must contain at least one digit.")

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
        raise ValidationError("Password must contain at least one special character.")