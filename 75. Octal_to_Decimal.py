import math

# convert Decimal to Octal
oct(5349) #12345

# convert back to Decimal
def oct_decimal(n:int)->int:
    """Convert Octal to Decimal

    Args:
        n (int): the given Octal number 

    Returns:
        int: the converted decimal number
    """

    length = len(str(n))
    num_list = [i for i in str(n)]
    result = 0
    for x in range(length):
        result += int(num_list[x]) * math.pow(8,length-1-x)
    return int(result)

oct_decimal(12345)
