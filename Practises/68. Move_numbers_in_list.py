# move numbers m times to its right, the last m numbers become the first m numbers 

list_1 = [1,2,3,4,5,6,7,8,9,10]
# print(len(list_1))
def move_numbers(m:int, n:list)-> list:
    """Generate a new list in line with the rule: 
        move numbers m times to its right, 
        the last m numbers become the first m numbers 

    Args:
        m (int): the number of the positions to move
        n (list): the given list

    Returns:
        list: the generated list
    """
    ncopy = n.copy()
    for i in range(len(n)-m):
        n[i+m] = n[i]
    for i in range(m):
        n[i]=ncopy[len(n)-m+i]
    return n

move_numbers(3,list_1)