"""Count Vowels In The String Challenge"""
def solve(text):
    """Return number of vowels in a string

    Args:
        str (string): string that need to be count

    Returns:
        int: number of vowels
    """
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for character in text.lower():
        if character in vowels:
            count += 1
    return count
