import pprint
from patterns import manhattan_distance, moves


pp = pprint.PrettyPrinter(indent=4)


def a_star(start, end):

    # A - star Algorithm using Manhattan Distance

    start = str(start)
    lists = [[manhattan_distance(start, end), start]]
    expanded_nodes_list = []
    expanded_nodes = 0
    # Repeat the process for the all the combinations of wrongly placed tiles
    while lists:
        i = 0
        for j in range(1, len(lists)):
            if lists[i][0] > lists[j][0]:
                i = j
            # Lower values of manhattan distance for the wrongly placed tiles (ideal moves)
        pattern = lists[i]
        lists = lists[:i] + lists[i + 1:]
        end_node = pattern[-1]
        if end_node == end:
            break
        if end_node not in expanded_nodes_list:
            for move in moves(end_node):
                if move not in expanded_nodes_list:
                    # Getting all the plausible transitions of the matrix
                    new_path = [pattern[0] + manhattan_distance(move, end) - manhattan_distance(end_node, end)]\
                        + pattern[1:] + [move]
                    lists.append(new_path)
                    expanded_nodes_list.append(end_node)
                expanded_nodes = expanded_nodes + 1

    pattern_size = len(pattern)

    print("The number of moves required : ", pattern_size//4, 'moves')
    pp.pprint(pattern)