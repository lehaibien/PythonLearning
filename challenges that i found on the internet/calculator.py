"""Calculator Challenge"""
def solve(first_number, operator, second_number):
    """Calculator

    Args:
        first_number (_type_): _description_
        operator (_type_): _description_
        second_number (_type_): _description_

    Raises:
        ValueError: _description_

    Returns:
        _type_: _description_
    """
    operators = {'+', '-', '*', '/'}
    if operator not in operators:
        raise ValueError('Operator should be + or - or * or /')
    return eval(f'{first_number}{operator}{second_number}')
