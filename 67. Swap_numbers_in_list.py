# swap the largest number with the first element and smallest number with the last element

a = [1,2,3,4,5]
import numpy as np

def inlistswap(list_1:list)->list:
    """Swap the largest number with the first element and 
        smallest number with the last element in the given list

    Args:
        list_1 (list): The given list

    Returns:
        list: the swapped list 
        """
    # method 1: use numpy functions
    # result = list_1
    # # swap the first number with the largest number

    # # The index of the largest number
    # index_large = np.argmax(list_1)
    # # swap
    # result[0], result[index_large] = list_1[index_large], list_1[0]

    # # swap the smallest number with the last element
    # # the index of the smallest number
    # index_small = np.argmin(list_1)
    # # swap
    # result[-1], result[index_small] = list_1[index_small], list_1[-1]

    # return result

    # method 2: use built-in functions 
    # the largest number
    maximum = list_1.index(max(list_1))
    list_1[0],list_1[maximum] = list_1[maximum], list_1[0]
    minimum = list_1.index(min(list_1))
    list_1[-1], list_1[minimum] = list_1[minimum], list_1[-1]
    return list_1

print(inlistswap(a))

# do not use built in functon to find the largest index

def largeindex(list_1:list)->int:
   # find the largest number in the list: maximum
    maximum = list_1[0]
    for x in list_1:
        if x > maximum:
            maximum = x
   # find the index of 'maximum'
    for i,j in enumerate(list_1):
        if maximum == j:
            return i

# largeindex(a)
