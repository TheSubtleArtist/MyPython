def calculate_total(amounts, apply_tax=True, tax_rate=.10):
    total = sum(amounts)
    if apply_tax:
        total *= (1 + tax_rate)
    return round(total, 2)