from email_validator import validate_email

def test_valid_email():
    assert validate_email("user@example.com") == True