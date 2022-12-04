def addfrom(x,y)-> int:
    """add up all numbers from x to y 

    Args:
        x (_type_): the starting number
        y (_type_): the end number(included)
    """
    # two pointers:
    # 1. the base/result
    # 2. the next number 
    # 3. add them up. the result becomes the new base

    # for i in range(x,y+1):
    #     x += i

    # pythonic way:
    
    return sum(range(x,y+1))

print(addfrom(0,100))
    
       
