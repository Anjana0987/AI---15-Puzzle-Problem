def misplaced_tiles(start, end):
    start = eval(str(start))
    end = eval(end)
    misplaced = []
    for i in range(len(start)):
        for j in range(len(start)):
            if start[i][j] != end[i][j]:
                misplaced.append(start[i][j])
    return len(misplaced) - 1  # since ignoring the blank space


def is_solvable(input_matrix):
    input_matrix = eval(input_matrix)
    pos_zero = -1
    count = 0
    matrix_size = len(input_matrix)
    for m in range(matrix_size):
        for n in range(matrix_size):
            if input_matrix[m][n] == 0:
                pos_zero = m  # row when the value is the blank space
    array = [num for row in input_matrix for num in row]  # converting the matrix into a list
    # conditions for solvability
    for a in range(len(array) - 1):
        for b in range(a+1, len(array)):
            if array[a] != 0 and array[b] != 0 and array[a] > array[b]:
                count += 1
    return (pos_zero % 2 == 0 and count % 2 == 1) or (pos_zero % 2 == 1 and count % 2 == 0)