## A\* Search Algorithm

The A\* search algorithm is an informed search algorithm. Beside using a heuristic function, like the greedy best-first search algorithm, it also uses the cost of the path from the start state to the current state to guide its search. The cost of the path is also known as the **g-value**. As a function. it is denoted as `g(n)`. The heuristic function is denoted as `h(n)`. The A\* search algorithm uses the following function to guide its search:

`f(n) = g(n) + h(n)`

<div style="position: relative; padding-bottom: 56.25%; height: 0;">
<iframe src="https://www.youtube.com/embed/" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

## Solving the 15-Puzzle Problem with A\* Search

```python
from collections import deque
from heapq import heappush, heappop

# Board dimension
N = 4

# Board move directions
MOVES = {'up': -N, 'down': N, 'left': -1, 'right': 1}


# Manhattan Distance Heuristic
def manhattan_distance(board, goal_board):
  distance = 0
  for i in range(N * N):
    if board[i] is not None:
      goal_index = goal_board.index(board[i])
      current_row, current_col = divmod(i, N)
      goal_row, goal_col = divmod(goal_index, N)
      distance += abs(current_row - goal_row) + abs(current_col - goal_col)
  return distance


def is_valid_move(pos, move):
  if move == 'up' and pos < N:
    return False
  if move == 'down' and pos >= N * (N - 1):
    return False
  if move == 'left' and pos % N == 0:
    return False
  if move == 'right' and (pos + 1) % N == 0:
    return False
  return True


def make_move(board, move):
  empty_pos = board.index(None)
  if is_valid_move(empty_pos, move):
    new_board = board[:]
    target_pos = empty_pos + MOVES[move]
    new_board[empty_pos], new_board[target_pos] = new_board[
        target_pos], new_board[empty_pos]
    return new_board
  return None


def a_star_search(initial_board, goal_board):
    visited = set()
    queue = []
    board_states = {}
    paths = {}
    path_costs = {}

    def add_to_queue(board, path, cost):
        id = len(board_states)
        board_states[id] = board
        paths[id] = path
        path_costs[id] = cost
        total_cost = cost + manhattan_distance(board, goal_board)
        heappush(queue, (total_cost, id))

    add_to_queue(initial_board, [], 0)

    while queue:
        _, id = heappop(queue)
        board = board_states[id]
        path = paths[id]
        cost = path_costs[id]

        if board == goal_board:
            return path

        visited.add(tuple(board))

        for move in MOVES.keys():
            next_board = make_move(board, move)
            if next_board and tuple(next_board) not in visited:
                add_to_queue(next_board, path + [move], cost + 1)

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
    print(board[i * N:i * N + N])
  print()


if __name__ == "__main__":

  goal_board = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None]
  initial_board = [2, 4, 3, 1, 9, 10, 11, 12, 15, 14, 13, None, 6, 7, 5, 8]

  solution = a_star_search(initial_board, goal_board)

  print("\nGreedy Best-First Search Solution:")
  if solution:
    print_solution(initial_board, solution)
  else:
    print("No solution found with Greedy Best-First Search")

```

# Summary

Heuristic functions are a crucial topic in AI as they significantly impact the performance of search algorithms. We will delve into various heuristic functions in the upcoming lesson. For now, contemplate other heuristic functions that can be applied to our car and 15-puzzle examples.

Note:
The design of effective heuristic functions holds great importance in AI, as it profoundly influences the performance of search algorithms. In the next lesson, we will explore different heuristic functions. For now, consider alternative heuristic functions that can be utilized in our car and 15-puzzle examples.
