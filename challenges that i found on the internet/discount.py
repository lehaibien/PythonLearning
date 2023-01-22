"""Appy Discount Challenge"""
def solve(price, discount):
    """Calculate the price after applying discount

    Args:
        price (float): Price
        discount (float): Discount percentage

    Returns:
        float: Price after applying discount
    """
    return price * (100 - discount) / 100
