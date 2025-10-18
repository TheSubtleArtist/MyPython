def fancy_input(question, validator):
    """Ask a question repeatedly until a valid response is given."""
    while True:
        reply = input(f"{question} ")
        try:
            return validator(reply)
        except Exception:
            print("\nPlease enter a valid response.\n")