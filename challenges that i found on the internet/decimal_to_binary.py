"""Convert Decimal to Binary Challenge"""
def solve(number):
    """Convert any number into binary string.

    Args:
        number (int): number that need to be converted

    Returns:
        string: Binary string after converted
    """
    return bin(number).removeprefix('0b')
