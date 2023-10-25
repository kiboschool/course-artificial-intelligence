# Solving the 15 Puzzle Problem

<img src="../../images/15-puzzle.gif"/>

The 15 Puzzle, also known as the 15-Puzzle, is an exemplary sliding puzzle game comprising a 4x4 grid with 15 numbered tiles and one empty space. The tiles can be moved horizontally or vertically into the empty space to reposition them. The objective is to arrange the tiles in ascending order, typically with the empty space in the lower-right corner.

Given the problem above, let's define the search problem and solve it.

**State Space:**
Encompasses all potential configurations of the puzzle board.

**Initial State:** Represents the starting configuration of the puzzle, which may initially be a scrambled arrangement of the tiles.

**Goal State:** The desired configuration where the tiles are arranged in ascending order.

**Actions:** Moving a tile into the empty space, either horizontally or vertically.

**Transition Model:** This model defines the outcome of applying an action to a given state, resulting in a new state.

## Modeling this in Python

```python
# an unoptimized incompelte model for the 15 puzzle problem

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
    # Find the position of the None tile
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] is None:
                none_tile_position = (i, j)
                new_state = [row[:] for row in state]  # Create a copy of the state
                if action == "up" and none_tile_position[0] > 0:
                    new_state[i][j] = state[i-1][j]
                    new_state[i-1][j] = None
                    return new_state
                # Implement similar logic for other directions
    return None  # Return None if the action is invalid

# the goal test can be implemented link that
def check_goal(state):
    return state == goal_state

```

## Solving the 15 Puzzle Problem using DFS

````python
def dfs(initial_state, goal_state):
    stack = [(initial_state, [])]
    visited = set()

    while stack:
        current_state, path = stack.pop()
        if check_goal(current_state, goal_state):
            return path
        visited.add(tuple(map(tuple, current_state))

        for action in ["up", "down", "left", "right"]:
            new_state = transition_model(list(map(list, current_state)), action)
            if new_state is not None and tuple(map(tuple, new_state)) not in visited:
                stack.append((new_state, path + [action]))

    return None
    ```

## Solving the 15 Puzzle Problem using BFS

```python

def bfs(initial_state, goal_state):
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        current_state, path = queue.popleft()
        if check_goal(current_state, goal_state):
            return path
        visited.add(tuple(map(tuple, current_state))

        for action in ["up", "down", "left", "right"]:
            new_state = transition_model(list(map(list, current_state)), action)
            if new_state is not None and tuple(map(tuple, new_state)) not in visited:
                queue.append((new_state, path + [action]))

    return None
````

## Additional resources

https://medium.com/nerd-for-tech/ai-search-algorithms-with-examples-54772c6d973a

```python
from collections import deque

class PuzzleSolver:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0)

    def solve(self):
        queue = deque()
        queue.append((self.initial_state, []))  # Store the current state and the path to this state

        while queue:
            current_state, current_path = queue.popleft()

            if current_state == self.goal_state:
                return current_path + [current_state]

            empty_index = current_state.index(0)
            row, col = empty_index // 4, empty_index % 4

            neighbors = self.get_neighbors(row, col)

            for neighbor in neighbors:
                new_state = list(current_state)
                neighbor_index = neighbor[0] * 4 + neighbor[1]
                new_state[empty_index], new_state[neighbor_index] = new_state[neighbor_index], new_state[empty_index]

                if tuple(new_state) not in current_path:
                    queue.append((tuple(new_state), current_path + [current_state]))

    def get_neighbors(self, row, col):
        neighbors = []
        if row > 0:
            neighbors.append((row - 1, col))
        if row < 3:
            neighbors.append((row + 1, col))
        if col > 0:
            neighbors.append((row, col - 1))
        if col < 3:
            neighbors.append((row, col + 1))
        return neighbors

# Example usage:
initial_state = (1, 2, 3, 4, 5, 6, 0, 7, 8, 9, 10, 11, 13, 14, 15, 12)
solver = PuzzleSolver(initial_state)
solution = solver.solve()

if solution:
    print("Solution found:")
    for step in solution:
        for i in range(0, 16, 4):
            print(step[i:i + 4])
        print("\n")
else:
    print("No solution found")

```

## Solving the 8 Puzzle Problem using DFS

```python
from collections import deque

# Board dimension
N = 3

# Board move directions
MOVES = {
    'up': -N,
    'down': N,
    'left': -1,
    'right': 1
}

def is_valid_move(pos, move):
    if move == 'up' and pos < N:
        return False
    if move == 'down' and pos >= N * (N-1):
        return False
    if move == 'left' and pos % N == 0:
        return False
    if move == 'right' and (pos+1) % N == 0:
        return False
    return True

def make_move(board, move):
    empty_pos = board.index(None)
    if is_valid_move(empty_pos, move):
        new_board = board[:]
        target_pos = empty_pos + MOVES[move]
        new_board[empty_pos], new_board[target_pos] = new_board[target_pos], new_board[empty_pos]
        return new_board
    return None

def bfs(initial_board, goal_board):
    visited = set()
    queue = deque([(initial_board, [])])

    while queue:
        board, path = queue.popleft()

        if board == goal_board:
            return path

        visited.add(tuple(board))

        for move in MOVES.keys():
            next_board = make_move(board, move)
            if next_board and tuple(next_board) not in visited:
                queue.append((next_board, path + [move]))

    return None

def print_solution(board, solution):
    print("Initial board:")
    print_board(board)
    for move in solution:
        board = make_move(board, move)
        print(f"\nMove {move}:")
        print_board(board)

def print_board(board):
    for i in range(N):
        print(board[i*N:i*N+N])
    print()

if __name__ == "__main__":
    goal_board = [1, 2, 3, 4, 5, 6, 7, 8, None]
    initial_board = [1, 2, 3, 4, None, 6, 7, 5, 8]

    bfs_solution = bfs(initial_board, goal_board)

    print("\nBFS Solution:")
    if bfs_solution:
        print_solution(initial_board, bfs_solution)
    else:
        print("No solution found with BFS")


```
