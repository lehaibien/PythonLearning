"""Hide the Number of Credit Card Challenge"""
def solve(credit):
    """Hide all number of the credit card exept the last four.

    Args:
        credit (string): The number of credit card.

    Returns:
        string: The last four number of the credit card.
    """
    length = len(credit)
    return credit[length - 4:]
