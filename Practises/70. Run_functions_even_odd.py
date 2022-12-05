# create a function. If the input number is even, run another function A. If the input number is odd, run another function B.

def run_input(n:int)->float:
    """If the input number is even, run another function A. If the input number is odd, run another function B.

    Args:
        n (int): The input number, should not be 0.

    Returns:
        float: The final result of the function A or B.
    """
    def funca(n:int)->float:
        """the function A 

        Args:
            n (int): the given integer

        Returns:
            float: the result
        """
        result = 0
        for i in range(2,n+1,2): 
            result += 1/i
        return result

    def funcb(n:int)->float:
        """the function B 

        Args:
            n (int): the given integer

        Returns:
            float: the result
        """
        result = 0
        for i in range(1,n+1,2):
            result += 1/i
        return result

    if n % 2 == 0: # if the input is even
        # run function A 
        return funca(n)
    else: # if the input is odd
        return funcb(n)


run_input(6)