from queue import PriorityQueue
import pygame


def h(p1, p2):
    # applies cab
    # distance to estimate the distance from any node to end node
    x1, y1 = p1
    x2, y2 = p2
    return abs(x2 - x1) + abs(y2 - y1)


def reconstruct_path(start_node, previous_node, current_path, draw):
    while current_path in previous_node:
        current_path = previous_node[current_path]
        current_path.make_path()
    start_node.make_start()
    draw()


def path_finder_algo(draw, start_node, end_node, grid):
    nodes_under_consideration = PriorityQueue()
    # can't check if a node is in a priority queue
    nodes_under_consideration_hash = {start_node}
    # nodes_under_consideration.put((f_score,node))
    nodes_under_consideration.put((0, start_node))
    previous_node = {}
    # all nodes
    node_table = {node: [float("inf"), float("inf")] for rows in grid for node in rows}
    # unvisited_queue_hash[node] = [g_score,f_score,previous_node]
    node_table[start_node][0] = 0
    node_table[start_node][1] = node_table[start_node][0] + h(
        start_node.get_pos(), end_node.get_pos()
    )
    # unvisited_queue.

    while not nodes_under_consideration.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # if user clickes quit, exit out.
                pygame.quit()
        # remove item with most priority
        current_node = nodes_under_consideration.get()[1]
        nodes_under_consideration_hash.remove(current_node)

        # tag every node visited as visited
        current_node.make_visited()

        if current_node == end_node:
            # color the end node back it's original color
            start_node.make_start()
            end_node.make_end()
            # current node is end node
            reconstruct_path(start_node, previous_node, current_node, draw)
            return True

        for neighbour in current_node.get_neighbours(grid):

            g_score_of_current_node = node_table[current_node][0]
            # g_score is distance from start node to current node
            # g_score needed to get to current node plus amount
            # of work needed to be done to get to neighbour(next node).
            g_score = g_score_of_current_node + 1
            f_score = g_score + h(neighbour.get_pos(), end_node.get_pos())

            if f_score < node_table[neighbour][1]:
                # if fscore is smaller than current f_Score
                # means new shortest path has been found
                # update g_Score
                node_table[neighbour][0] = g_score
                # update f_Score
                node_table[neighbour][1] = f_score
                # update provious node

                # if neighbour is not a node under consideration
                # and neighbour has not been visited before
                # wouldn't want to visit an already visited Node
                if (
                    neighbour not in nodes_under_consideration_hash
                    and not neighbour.is_visited()
                ):
                    previous_node[neighbour] = current_node
                    # add neighbour to nodes under consideration
                    nodes_under_consideration.put((f_score, neighbour))
                    nodes_under_consideration_hash.add(neighbour)
                    # make open simply indicates i've tried this part
                    neighbour.make_possible_path()

        draw()

    # if all possible path have been considered, return no possible path found.
    return False
