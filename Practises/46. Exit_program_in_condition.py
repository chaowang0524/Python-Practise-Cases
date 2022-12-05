import math
def check_number(n:int) -> bool:
    """if the square of the number is greater than 50, exit the program

    Args:
        n (int): the input number

    Returns:
        bool: whether to carry on checking
    """

    while True:
        n = int(input("Please enter an integer: "))
        if n*n> 50:
            return False

print(check_number(10))