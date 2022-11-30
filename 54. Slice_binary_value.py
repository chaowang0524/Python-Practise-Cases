# Slice the fourth to the seventh digits from right side of an integer's binary value

# 1. use bitwise right shift to move 4 digits to its right
# 2. set a binary number with 4 ones at its last 4 digits and 0s with the rest (use: ~(~0<<4))
# 3. Use & to calculate two values

def slice_binary(n:int, left:int, right:int) -> int:
    """ Get the sliced value from the given interval of the given integer's binary value

    Args:
        n (int): the given integer
        left(int): the seventh digit from the right side of the given integer's binary value
        right(int): the fourth digit from the right side of the given integer's binary value'


    Returns:
        int: an integer which represents the sliced binary value
    """

    
    # move x digits to its right:
    x = left - right + 1
    temp_a = n>>x 
    temp_b = ~(~0<<x)
    return temp_a & temp_b



slice_binary(9,7,4)
