"""Repeat Characters Challenge"""
def solve(text):
    """_summary_

    Args:
        text (_type_): _description_
    """
    result = ''
    for c in text:
        result += c * 2
    return result
