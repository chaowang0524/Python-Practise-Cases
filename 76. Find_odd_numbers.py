
# Find the quantity of the odd numbers that is made from 0-7

# for one digit number, it's 4 
# for two digit number, it's 7*4
# for three digit number, it's 7*8*4
# for four digit number, it's 7 * 8 * 8 *4
# ... 


import math
def get_quantity(n:int)-> int:
    """Find the total sum of numbers of odd numbers that are made from 0-7

    Args:
        n (int): the request digits of the number

    Returns:
        int: the total number of the odd numbers that are made from 0-7 at n digits
    """

    if n == 1:
        return 4
    elif n ==2: 
        return 7*4
    else:
        return 7*math.pow(8,(n-2))*4

get_quantity(2)
