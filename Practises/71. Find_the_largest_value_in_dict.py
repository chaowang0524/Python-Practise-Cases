# Create a function to find the largest value in the dict:

diction = {
    "a": 15,
    "b": 20,
    "c": 35,
}

# get the maximum value from the dictionary
# values = [v for v in diction.values()]
# max_value = max(values)

# # get the key from the max_value in the dictionary
# max_key = [k for k in diction if diction[k]==max_value]
# print(max_key)

def fmaxvalue(n:dict) -> str:
    """Find the largest value in the dict

    Args:
        n (dict): The given dictionary

    Returns:
        str: the key to the largest value
    """ 
    # list all the values to find the largest value
    values = [v for v in n.values()]
    max_value = max(values)
    
    # to iterate the dictionary to match the key to the largest value
    max_key = [k for k in n if n[k]==max_value]
    return max_key

fmaxvalue(diction)