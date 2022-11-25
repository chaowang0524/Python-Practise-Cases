x = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]
y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]


def add_two_matrices(x, y):
    result = []
    for i in range(len(x)):
        result.append([])  # add the nested list for first loop
        for j in range(len(x[i])):
            # add the placeholder for upcoming assignment
            result[i].append(x[i][j])
            # assign the result
            result[i][j] = (x[i][j] + y[i][j])
    return result


print(add_two_matrices(x, y))
