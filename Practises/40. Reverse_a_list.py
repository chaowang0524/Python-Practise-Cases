
# if the length of the list is even:
# swap the first and last elements, the second and the second last
# if the length of the list is odd:
# 1. swap the first and last elements, the second and the second last
# 2. keep the middle number

lst = [8,2,3,4,5,6,7,8,9,10,11,12,13]
def freverse(a: list) -> list:
    """Output a reversed version of the given list

    Args:
        a (list): the given list

    Returns:
        list: the reversed version of the given list
    """

    # if the length of the list is even:
    if len(a) % 2 == 0:
        for i in range(1, ((len(a)/2)+1)): # start swaping
            # swap the first and last elements, the second and the second last...
            # set the pointers
            a[i-1], a[-i] = a[-i], a[i-1]
    else: # if it is odd:
        # start swaping from first number to the middle number(include)
        for i in range(1, (len(a)//2)+1): 
            if a[i-1] != a[(len(a)//2)+1]: #
                a[i-1], a[-i] = a[-i], a[i-1]
    return(a)


print(freverse(lst))
