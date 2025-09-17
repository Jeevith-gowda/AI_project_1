import heapq
import math

class PuzzleNode:
    """A node in the search tree for the 8-puzzle problem."""
    def __init__(self, state, parent=None, action=None, g=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.g = g  # Cost from start to current node
        self.h = 0  # Heuristic cost (estimated cost to goal)
        self.f = 0  # Total cost: f = g + h

    def __lt__(self, other):
        return self.f < other.f

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(tuple(map(tuple, self.state)))

def get_successors(node):
    """Generate all possible successor states from the current state."""
    successors = []
    state = node.state
    zero_pos = None
    for r in range(3):
        for c in range(3):
            if state[r][c] == 0:
                zero_pos = (r, c)
                break
        if zero_pos:
            break
    
    r, c = zero_pos
    moves = [(-1, 0, 'Up'), (1, 0, 'Down'), (0, -1, 'Left'), (0, 1, 'Right')]

    for dr, dc, action in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            new_state = [row[:] for row in state]
            new_state[r][c], new_state[nr][nc] = new_state[nr][nc], new_state[r][c]
            successors.append(PuzzleNode(new_state, parent=node, action=action, g=node.g + 1))
            
    return successors

def misplaced_tiles(state, goal_state):
    """Heuristic h1: Counts the number of misplaced tiles."""
    misplaced = 0
    for r in range(3):
        for c in range(3):
            if state[r][c] != goal_state[r][c] and state[r][c] != 0:
                misplaced += 1
    return misplaced

def manhattan_distance(state, goal_state):
    """Heuristic h2: Calculates the sum of Manhattan distances for all tiles."""
    distance = 0
    goal_positions = {goal_state[r][c]: (r, c) for r in range(3) for c in range(3)}
    
    for r in range(3):
        for c in range(3):
            tile = state[r][c]
            if tile != 0:
                goal_r, goal_c = goal_positions[tile]
                distance += abs(r - goal_r) + abs(c - goal_c)
    return distance

def is_solvable(state):
    """Checks if the 8-puzzle instance is solvable using inversion count."""
    inversions = 0
    flat_state = [tile for row in state for tile in row if tile != 0]
    for i in range(len(flat_state)):
        for j in range(i + 1, len(flat_state)):
            if flat_state[i] > flat_state[j]:
                inversions += 1
    return inversions % 2 == 0

def a_star_search(initial_state, goal_state, heuristic_func):
    """Performs A* search to find the shortest path to the goal."""
    if not is_solvable(initial_state):
        # Return three values for consistency, even on failure
        return None, 0, 0

    start_node = PuzzleNode(initial_state, g=0)
    start_node.h = heuristic_func(initial_state, goal_state)
    start_node.f = start_node.g + start_node.h
    
    open_list = [start_node]
    closed_set = set()
    nodes_expanded = 0
    nodes_generated = 1  # Start with 1 for the initial node

    while open_list:
        current_node = heapq.heappop(open_list)
        
        if current_node.state == goal_state:
            path = []
            while current_node:
                path.append((current_node.state, current_node.action))
                current_node = current_node.parent
            # Return all three metrics on success
            return path[::-1], nodes_expanded, nodes_generated
        
        closed_set.add(current_node)
        nodes_expanded += 1

        successors = get_successors(current_node)
        nodes_generated += len(successors) # Track generated nodes

        for successor in successors:
            if successor in closed_set:
                continue

            successor.h = heuristic_func(successor.state, goal_state)
            successor.f = successor.g + successor.h
            
            if all(successor.state != item.state for item in open_list) or successor.f < sum(item.f for item in open_list if item.state == successor.state):
                heapq.heappush(open_list, successor)
                
    # Return three values for consistency, even on path not found
    return None, nodes_expanded, nodes_generated

def print_puzzle(state):
    """Prints the 3x3 puzzle state nicely."""
    for row in state:
        print(" ".join(map(str, row)).replace('0', '_'))
    print()

def main():
    """Main function to run the 8-puzzle solver."""
    print("Enter the initial state (3x3 grid, use 0 for empty space):")
    initial_state = []
    for _ in range(3):
        row = list(map(int, input().split()))
        initial_state.append(row)
        
    print("\nEnter the goal state (3x3 grid, use 0 for empty space):")
    goal_state = []
    for _ in range(3):
        row = list(map(int, input().split()))
        goal_state.append(row)

    # --- SOLVE WITH HEURISTIC 1 ---
    print("\n--- Solving with h1: Misplaced Tiles Heuristic ---")
    # THE FIX: Unpack all THREE returned values
    path1, expanded1, generated1 = a_star_search(initial_state, goal_state, misplaced_tiles)
    
    if path1:
        print(f"Path found in {len(path1) - 1} moves.")
        print(f"Nodes Generated: {generated1}")
        print(f"Nodes Expanded: {expanded1}")
        # Uncomment the block below to print the full path
        # for state, action in path1:
        #     if action:
        #         print(f"Action: {action}")
        #     print_puzzle(state)
    else:
        print("This puzzle is not solvable.")

    # --- SOLVE WITH HEURISTIC 2 ---
    print("\n--- Solving with h2: Manhattan Distance Heuristic ---")
    # THE FIX: Unpack all THREE returned values
    path2, expanded2, generated2 = a_star_search(initial_state, goal_state, manhattan_distance)

    if path2:
        print(f"Path found in {len(path2) - 1} moves.")
        print(f"Nodes Generated: {generated2}")
        print(f"Nodes Expanded: {expanded2}")
    else:
        # This message will likely not be seen if the first check passed
        print("This puzzle is not solvable.")
        
if __name__ == "__main__":
    main()