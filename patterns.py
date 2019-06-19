def manhattan_distance(i_state, f_state):
    i_state = eval(i_state)
    f_state = eval(f_state)
    f_state_list = []
    result = 0

    for i in range(len(f_state)):
        for j in range(len(f_state)):
            if f_state[i][j] != 0:  # ignore the location of the blank space
                # Goal state and their exact locations (row and col values)
                f_state_list.append([[i, j], f_state[i][j]])

    for i in range(len(i_state)):
        for j in range(len(i_state)):
            if i_state[i][j] != 0:  # ignore the location of the blank space
                for s in f_state_list:
                    if s[1] == i_state[i][j]:  # get the location of each of the values from initial state
                        row = s[0][0]  # row of the value
                        col = s[0][1]  # column of the value
                result += abs(i - row) + abs(j - col)  # Calculating manhattan distance
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
