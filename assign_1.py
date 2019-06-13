import numpy as np
import sys

initial_state = np.array([[0, 15, 9, 13], [11, 12, 10, 14], [3, 7, 6, 2], [4, 8, 5, 1]])
final_state = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]])


def solvable(input_matrix):
    pos_z = -1
    count = 0
    matrix_size = input_matrix.shape[0]
    for i in range(matrix_size):
        for j in range(matrix_size):
            if input_matrix[i][j] == 0:
                pos_z = i
    array = [num for row in input_matrix for num in row]
    size = matrix_size*matrix_size
    for i in range(size - 1):
        for j in range(i+1, size):
            if array[i] != 0 and array[j] != 0 and array[i] > array[j]:
                count += 1
    return (pos_z % 2 == 0 and count % 2 == 1) or (pos_z % 2 == 1 and count % 2 == 0)


def manhattan_dist(i_st, f_st):
    x = (i_st[:, None] != f_st).all(-1)
    i, j = np.where(x)
    print('*****----*********-----*******-----*******----******')
    print("The number of values that are wrongly placed are,", len(i_st[i, j]) - 1)
    sum = 0
    m = i_st.shape[0]
    for i in range(m):
        for j in range(m):
            num = i_st[i][j]
            if num != i*m + (j + 1) and num != 0:
                correct_row = (num - 1)//m
                correct_col = (num - 1) % m
                sum += abs(i - correct_row) + abs(j - correct_col)
    print(sum)
    return sum

answer = solvable(initial_state)

if answer == True:
    manhattan_dist(initial_state, final_state)
else:
    print("This matrix is not solvable. Please try again with a different matrix.")

