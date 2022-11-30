# Generate a Pascal's triangle with n lines

def pastriangle(n:int)-> int:
    """Generate a Pascal's triangle with n rows

    Args:
        n (int): rows of the Pascal's triangle'

    Returns:
        int: the numbers that form the Pascal's triangle'
    """

    line = []
    # print n rows
    for i in range(n):
        line.append([]) # generate one new row as a nested list 
        for j in range(i+1): # print columns 
            if j == 0 or j == i:  # if its the first column or the last column, the value is 1 
                line[i].append(1) 
            else: # the value equals to the combination of the number above and the number at its upper left
                line[i].append(line[i-1][j-1] + line[i-1][j])
    for i in line:
        print(i)
  
pastriangle(10)