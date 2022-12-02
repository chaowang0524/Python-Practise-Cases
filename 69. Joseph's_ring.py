# A ring consists of number of n people who start to count numbers from 1-3
# The person who counts 3 leaves the ring.
# Find the sequence number of the person survives

def joseph_count(n:int)->int:
    """Find the sequence number of the survival

    Args:
        n (int): the number of people to count in the original ring

    Returns:
        int: the sequence number of the survival
    """
    # use another list to store the data
    # set the original ring
    oring =[i for i in range(1,n+1)]
    removed= []
    index = 0 # index
    count = 0 # 报数计数器

    while len(oring)>1: # 一直转，剩最后一个人
        length = len(oring)
        current_number = oring[index]
        count += 1  # 报数
        if count == 3: # 如果有人报到3时
            # number_to_be_deleted = oring[index]
            oring.pop(index) # 从圈中删掉此人
            # removed.append(the_third_person) # 看下踢了那些人
            count = 0 # 重新报
        else:   
            # 如果没报到3，+1，准备踢下一个人(pop method)，
            # 用取模的方法回归一圈，此时i重置(当a<b, a%b =a, 当a=b, a%b =0)
            index = (index+1) % length # Key algorithm
            # current_number = oring[index]
    return oring[0]

joseph_count(15)
