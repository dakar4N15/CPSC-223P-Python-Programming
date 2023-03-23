def matrix_math(matrix_a=[], matrix_b=[], mode="add"):
    size_a = len(matrix_a)
    size_b = len(matrix_b)
    for i in range(size_a):
        if(len(matrix_a) != len(matrix_a[i])):
            return False
    for row in matrix_a:
        for element in row:
            if not isinstance(element, int):
                return False
    for i in range(size_b):
        if(len(matrix_b) != len(matrix_b[i])):
            return False
    for row in matrix_b:
        for element in row:
            if not isinstance(element, int):
                return False
    if(size_a != size_b):
        return False
    if(mode == "add"):
        new_list = []
        for i in range(len(matrix_a)):
            row = []
            for j in range(len(matrix_a[0])):
                row.append(matrix_a[i][j] + matrix_b[i][j])
            new_list.append(row)
        return new_list
    if(mode == "subtract"):
        new_list = []
        for i in range(len(matrix_a)):
            row = []
            for j in range(len(matrix_a[0])):
                row.append(matrix_a[i][j] - matrix_b[i][j])
            new_list.append(row)
        return new_list

    