import time
from a_star import a_star
from solvable import is_solvable, misplaced_tiles

start_time = time.time()

if __name__ == '__main__':
    initial_state = [[0, 12, 9, 13], [15, 11, 10, 14], [3, 7, 2, 5], [4, 8, 6, 1]]
    final_state = str([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]])
    if is_solvable(str(initial_state)):
        print("********--------*********---------*********--------*********")
        print("This matrix is solvable and the solution is given below !!!!")
        print("********--------*********---------*********--------*********")
        print("The number of misplaced tiles are : ", misplaced_tiles(str(initial_state), final_state))
        print("********--------*********---------*********--------*********")
        a_star(str(initial_state), final_state)
        print("")
        print("The time taken for the execution : --- %s seconds ---" % (time.time() - start_time))
    else:
        print("This matrix is not solvable. Try with another !!!")
