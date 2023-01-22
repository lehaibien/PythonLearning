"""SORT A LIST CHALLENGE"""
def solve(list_of_numbers, sort_type):
    """Sort a list of integers by ascending or descending.

    Args:
        list_of_numbers (list): list of integers
        sort_type (int): 1 for ascending, 0 for none and -1 for descending

    Raises:
        ValueError: if the value of sort_type is not -1, 0 or 1

    Returns:
        list: sorted list
    """
    if sort_type < -1 or sort_type > 1:
        raise ValueError("Value should be 1, 0 or -1")
    if sort_type == 0:
        return list_of_numbers
    if sort_type == -1:
        list_of_numbers.sort(reverse=True)
    else:
        list_of_numbers.sort(reverse=False)
