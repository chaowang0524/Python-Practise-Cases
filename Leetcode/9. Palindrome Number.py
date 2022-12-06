# Given an integer x, return true if x is a palindrome, and false otherwise.

def isPalindrome(x: int) -> bool:
    """Given an integer x, return true if x is a palindrome, and false otherwise.

    Args:
        x (int): the given integer

    Returns:
        bool: True if x is a palindrome, and false otherwise
    """

    num = list(str(x))
    num_check = num[::-1]
    if num == num_check:
        return True
    else:
        return False


isPalindrome(-121)