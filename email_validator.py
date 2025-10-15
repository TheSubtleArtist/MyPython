def validate_email(email):
    """Validate an email address with basic checks."""
    if not email:
        return False

    if '@' not in email:
        return False

    local, domain = email.split('@', 1)

    if not local or not domain:
        return False

    if domain.count('.') == 0:
        return False

    return True