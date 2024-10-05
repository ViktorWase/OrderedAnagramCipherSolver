import heapq
from LATIN_FREQS import LAT_4_NO_JW

from utils import *

# Define a Node class to store the necessary data for each state
class Node:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state        # Current state (e.g., ciphertext configuration)
        self.parent = parent      # Pointer to the parent node
        self.g = g                # Cost from the start to this node
        self.h = h                # Heuristic estimate to the goal
        self.f = g + h            # Total estimated cost (f = g + h)

    def __lt__(self, other):
        return self.f < other.f   # Comparison function for priority queue


def reconstruct_path(node):
    """Helper function to reconstruct the path from start to goal."""
    path = []
    while node is not None:
        path.append(node.state)
        node = node.parent
    return path[::-1]  # Return the reversed path


def get_successors(history, cipherList):
    choices = getAllChoices(history, cipherList)
    costs = [objFunc(history, c, cipherList) for c in choices]
    successors = [list(history) + [c] for c in choices]  # TODO: Det här gör att minnet går åt väldigt snabbt.
    return successors, costs


def is_solved(history, cipherList):
    assert len(history) <= len(cipherList)
    return len(history) == len(cipherList)


def heuristic(x, cipherList):
    return 300*(1.0 - len(x) / len(cipherList))
    return 0.0  # TODO: Gör något smart.


def a_star(start_state, heuristic, cipherList):
    # Priority queue to store the nodes to explore, ordered by 'f'
    open_list = []
    heapq.heappush(open_list, Node(start_state, g=0, h=heuristic(start_state, cipherList)))

    # Set to track visited nodes (optional, depending on the problem)
    closed_set = set()

    counter = 0
    while open_list:
        # Get the node with the lowest f-score (g + h)
        current_node = heapq.heappop(open_list)
        if counter % 1000 == 0:
            print(counter, "".join([cipherList[h] for h in current_node.state]))
        counter += 1
        # Check if we have reached the goal
        if is_solved(current_node.state, cipherList):
            print(print("".join([cipherList[h] for h in current_node.state])))
            return current_node.state
            # return reconstruct_path(current_node)  # Found a solution, reconstruct the path

        # Add the current node's state to the closed set
        closed_set.add(tuple(current_node.state))

        # Generate the possible next states (successors)
        successors, costs = get_successors(current_node.state, cipherList)
        for i in range(len(costs)):
            successor = successors[i]
            cost = costs[i]
            if tuple(successor) in closed_set:
                continue  # Skip states we've already processed

            # Calculate the cost to reach the successor (g)
            g = current_node.g + cost
            h = heuristic(successor, cipherList)
            new_node = Node(successor, parent=current_node, g=g, h=h)

            # Add the successor to the open list to be explored
            heapq.heappush(open_list, new_node)

    # If we exit the loop without finding the goal, return None (no solution)
    return None


if __name__ == '__main__':
    text_ = "facioliberosexliberislibrislibraque"
    #text_ = "facileprinceps"
    CIPHER = []
    while len(text_) > 0:
        l_ = text_[0]
        CIPHER = CIPHER + [l_ for _ in range(text_.count(l_))]
        text_ = text_.replace(l_, "")
    print("".join(CIPHER))
    print(a_star([], heuristic, CIPHER))
