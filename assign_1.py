import pprint
import numpy as np


pp = pprint.PrettyPrinter(indent=4)


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


def manhattan_distance(i_state, f_state):
    i_state = eval(i_state)
    f_state = eval(f_state)
    f_state_list = []
    result = 0

    for i in range(len(f_state)):
        for j in range(len(f_state)):
            if f_state[i][j] == 0:  # ignore the location of the blank space
                continue
            f_state_list.append([[i, j], f_state[i][j]])  # Goal state and their exact locations (row and col values)

    for i in range(len(i_state)):
        for j in range(len(i_state)):
            if i_state[i][j] == 0:  # ignore the location of the blank space
                continue
            for s in f_state_list:
                if s[1] == i_state[i][j]:  # get the location of each of the values from initial state
                    x = s[0][0]  # row of the value
                    y = s[0][1]  # column of the value
            result += abs(i - x) + abs(j - y)  # Calculating manhattan distance
    return result


def moves(matrix):
    choices = []
    matrix = eval(matrix)
    i = 0
    while 0 not in matrix[i]:
        i += 1
    j = matrix[i].index(0)

    if i > 0:
        # moving up
        # moving a row up since i = i - 1
        matrix[i][j], matrix[i - 1][j] = matrix[i - 1][j], matrix[i][j]
        choices.append(str(matrix))
        matrix[i][j], matrix[i - 1][j] = matrix[i - 1][j], matrix[i][j]
    if i < 3:
        # moving down
        # moving a row down since i = i + 1
        matrix[i][j], matrix[i + 1][j] = matrix[i + 1][j], matrix[i][j]
        choices.append(str(matrix))
        matrix[i][j], matrix[i + 1][j] = matrix[i + 1][j], matrix[i][j]
    if j > 0:
        # moving left
        # moving a column down(left) since j = j - 1
        matrix[i][j], matrix[i][j - 1] = matrix[i][j - 1], matrix[i][j]
        choices.append(str(matrix))
        matrix[i][j], matrix[i][j - 1] = matrix[i][j - 1], matrix[i][j]
    if j < 3:
        # moving right
        # moving a column up(right) since j = j + 1
        matrix[i][j], matrix[i][j + 1] = matrix[i][j + 1], matrix[i][j]
        choices.append(str(matrix))
        matrix[i][j], matrix[i][j + 1] = matrix[i][j + 1], matrix[i][j]
    return choices


def a_star(start, end):
    """
    A* algorithm
    """
    start = str(start)
    front = [[manhattan_distance(start, end), start]]
    expanded = []
    expanded_nodes = 0
    while front:
        i = 0
        for j in range(1, len(front)):
            if front[i][0] > front[j][0]:
                i = j
        path = front[i]
        front = front[:i] + front[i + 1:]
        endnode = path[-1]
        if endnode == end:
            break
        if endnode in expanded:
            continue
        for k in moves(endnode):
            if k in expanded:
                continue
            newpath = [path[0] + manhattan_distance(k, end) - manhattan_distance(endnode, end)] + path[1:] + [k]
            front.append(newpath)
            expanded.append(endnode)
        expanded_nodes += 1

    print ("Expanded nodes:", expanded_nodes)
    print ("Solution: in", len(path)/4, 'moves')
    pp.pprint(path)


if __name__ == '__main__':
    initial_state = [[0, 15, 9, 13], [11, 12, 10, 14], [3, 7, 6, 2], [4, 8, 5, 1]]
    final_state = str([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]])
    if is_solvable(str(initial_state)):
        print("This matrix is solvable and the solution is given below !!!!")
        print("********--------*********---------*********--------*********")
        a_star(initial_state, final_state)