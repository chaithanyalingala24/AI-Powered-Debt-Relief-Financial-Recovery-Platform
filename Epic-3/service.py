def calculate_settlement(outstanding_amount, percentage):
    return (outstanding_amount * percentage) / 100

def validate_loan(amount):
    if amount <= 0:
        return False
    return True


def settlement_recommendation(amount):
    if amount > 500000:
        return 60
    elif amount > 100000:
        return 70
    return 80


def generate_letter(borrower, lender):
    return f"""
Dear {lender},

I request a settlement for my loan.

Borrower Name: {borrower}

Kindly consider my request.

Thank You
"""