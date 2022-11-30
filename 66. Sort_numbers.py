
number_1 = 20
number_2 = 10
number_3 = 15

# use `sort` function
# lst=[]
# lst.append(number_1)
# lst.append(number_2)
# lst.append(number_3)
# lst.sort()
# print(lst)

# write own code to compare 

def sort_three_numbers(number_1:int, number_2:int, number_3:int)-> list:
    """sort the given numbers in descending order

    Args:
        number_1 (int): the given number 3
        number_2 (int): the given number 3
        number_3 (int): the given number 3

    Returns:
        list: the list of numbers in descending order
    """

    result = []

    if number_1> number_2:
        result.append(number_1)
        if number_2> number_3:
            result.append(number_2)
            result.append(number_3)
        else: 
            result.append(number_3)
            result.append(number_2)
    else:
        result.append(number_2)
        if number_1> number_3:
            result.append(number_1)
            result.append(number_3)
        else:
            result.append(number_3)
            result.append(number_1)
    return result 


sort_three_numbers(number_1, number_2, number_3)