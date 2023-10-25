from collections import deque

initial_state = [
    [6, 11, 3, 13],
    [5, 1, 14, 8],
    [9, None, 2, 12],
    [4, 7, 15, 10]
]

goal_state = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, None]
]


def transition_model(state, action):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] is None:
                none_tile_position = (i, j)
                new_state = [row[:]
                             for row in state]  # Create a copy of the state

                if action == "up" and none_tile_position[0] > 0:
                    new_state[i][j], new_state[i -
                                               1][j] = new_state[i-1][j], new_state[i][j]
                    return new_state

                if action == "down" and none_tile_position[0] < 3:
                    new_state[i][j], new_state[i +
                                               1][j] = new_state[i+1][j], new_state[i][j]
                    return new_state

                if action == "left" and none_tile_position[1] > 0:
                    new_state[i][j], new_state[i][j -
                                                  1] = new_state[i][j-1], new_state[i][j]
                    return new_state

                if action == "right" and none_tile_position[1] < 3:
                    new_state[i][j], new_state[i][j +
                                                  1] = new_state[i][j+1], new_state[i][j]
                    return new_state
    return None  # Return None if the action is invalid


def check_goal(state):
    return state == goal_state


def dfs(initial_state, goal_state):
    stack = [(initial_state, [])]
    visited = set()
    visited.add(tuple(map(tuple, initial_state)))

    while stack:
        current_state, path = stack.pop()
        if check_goal(current_state):
            return path

        for action in ["up", "down", "left", "right"]:
            new_state = transition_model(
                [row[:] for row in current_state], action)
            if new_state:  # Check if new_state is not None
                new_state_tuple = tuple(map(tuple, new_state))
                if new_state_tuple not in visited:
                    stack.append((new_state, path + [action]))
                    visited.add(new_state_tuple)

    return None


def bfs(initial_state, goal_state):
    queue = deque([(initial_state, [])])
    visited = set()
    visited.add(tuple(map(tuple, initial_state)))

    while queue:
        current_state, path = queue.popleft()
        if check_goal(current_state):
            return path

        for action in ["up", "down", "left", "right"]:
            new_state = transition_model(
                [row[:] for row in current_state], action)
            if new_state:  # Check if new_state is not None
                new_state_tuple = tuple(map(tuple, new_state))
                if new_state_tuple not in visited:
                    queue.append((new_state, path + [action]))
                    visited.add(new_state_tuple)


def print_path(path):
    """Prints the solution path in a user-friendly format."""
    if path:
        print(" -> ".join(path))
    else:
        print("No solution found!")


def main():
    # print("Testing DFS:")
    # dfs_path = dfs(initial_state, goal_state)
    # print_path(dfs_path)

    print("\nTesting BFS:")
    bfs_path = bfs(initial_state, goal_state)
    print_path(bfs_path)


if __name__ == "__main__":
    main()
