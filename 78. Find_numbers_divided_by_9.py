# find the smallest number that only consists of 9 can be divided by the odd number and return the number of 9s.

def find_nine(odd:int)->int:
    """find the smallest number that only consists of 9 can be divided by the odd number and return the number of 9s.

    Args:
        n (int): the given odd number

    Returns:
        int: the number of 9s of the answer
    """

    def num9(n:int)->int:
        """create a number consists of only 9 

        Args:
            n (_type_): the digit of the nine

        Return: 
            the number only consists of 9

        """
        result = ""
        for i in range(n):
            result = result + "9"
        return int(result)

# divde num9 by the odd number, if fails, num9(n+1)
    i = 1 # start to count the number of 9
    while True:
        if num9(i)% odd == 0:
            break
        else:
            i += 1
    return i 


find_nine(13)