# Informed Search

_Estimated time to finish: 90 - 180 minutes_

In our previous lessons, we learned about the breadth-first search and depth-first search algorithms. Both of these algorithms are blind search algorithms, which means that they do not use any additional information to guide their search. The technical term for blind search algorithms is **uninformed** search algorithms.

Using uninformed search algorithms can be inefficient and computationally expensive because they do not use any additional information to guide their search. We saw that when we applied BFS to the 15-Puzzle problem. We waited for a long time for the algorithm to find the solution and sometimes it was not able to find the solution at all.

In this lesson, we will learn about the greedy best-first and the A\* search algorithms, which are **informed** search algorithms.

Informed search algorithms use additional information to guide their search. This should make them more efficient and less computationally expensive than uninformed search algorithms. We will use the A\* search algorithm to solve the 15-Puzzle problem and the car path problem and compare its performance with uninformed search algorithms.

## Informed Search

To get a sense of how informed search algorithms work, let's consider our car example. Take a look at this image:

<p align="center">
  <img src="../../images/car-state-decision.png" alt="Car State Decision" width="400">
</p>

If the car is at position `(2,1)` , as humans, we can easily determine that the next step should be to move to `(2,2)`. The `(1,1)` cell will take us further away from the goal state. This is the kind of information that we can use to guide our search algorithm making it more efficient.

## Greedy best-first search

Greedy best-first search is an informed search algorithm that uses a heuristic function to guide its search.

A **heuristic function** is a function that assesses alternatives in search algorithms at each branching step, utilizing available information to determine which branch to follow (which next state to explore).

In our previous car example, if we can inform the algorithm to prioritize the point `(2,2)` as it is closer to the goal state than `(1,1)` , then the algorithm will be able to make a better decision. In a grid world, we can use the direct line distance between the goal state and each state as a heuristic function. Let's modify our car example to use the greedy best-first search algorithm and see how it performs.

## Solving the 15-Puzzle Problem with Greedy Best-First Search

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


def greedy_best_first_search(initial_board, goal_board):
  visited = set()
  queue = []
  board_states = {}
  paths = {}

  def add_to_queue(board, path):
    id = len(board_states)
    board_states[id] = board
    paths[id] = path
    heappush(queue, (manhattan_distance(board, goal_board), id))

  add_to_queue(initial_board, [])

  while queue:
    _, id = heappop(queue)
    board = board_states[id]
    path = paths[id]

    if board == goal_board:
      return path

    visited.add(tuple(board))

    for move in MOVES.keys():
      next_board = make_move(board, move)
      if next_board and tuple(next_board) not in visited:
        add_to_queue(next_board, path + [move])

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

  solution = greedy_best_first_search(initial_board, goal_board)

  print("\nGreedy Best-First Search Solution:")
  if solution:
    print_solution(initial_board, solution)
  else:
    print("No solution found with Greedy Best-First Search")

```

### Different Heuristic Functions

Based on the nature of the problem, we can design different heuristic functions. For instance, in our car example, we can use the direct line distance between the goal state and each state as a heuristic function. In the 15-Puzzle problem, we can use the number of misplaced tiles as a heuristic function. Let's modify the 15-Puzzle problem to use the A\* search algorithm and see how it performs.
