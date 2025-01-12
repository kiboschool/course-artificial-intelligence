# A\* Search Algorithm

The A\* search algorithm is an informed search algorithm. Besides using a heuristic function, like the greedy best-first search algorithm, it also uses the cost of the path from the start state to the current state to guide its search. The cost of the path is also known as the **g-value**. As a function. it is denoted as `g(n)`. The heuristic function is denoted as `h(n)`. The A\* search algorithm uses the following function to guide its search:

`f(n) = g(n) + h(n)`

<div style="position: relative; padding-bottom: 56.25%; height: 0;">
<iframe src="https://www.youtube.com/embed/6TsL96NAZCo" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

## A\* Search Optimality

A\* search is guaranteed to find the optimal solution if the heuristic function is **admissible** and **consistent**.

An **admissible** heuristic function `h(n)` is one that never overestimates the cost of reaching the goal. In other words, the heuristic function should always be less than or equal to the actual cost of reaching the goal.

A heuristic function `h(n)` is **consistent** if the estimated cost of reaching the goal from the current state is no greater than the step cost of getting to the next state plus the estimated cost of reaching the goal from the next state. So, if I'm at state `n`, and I take an action that costs `c` to get to a successor state` n'`, the estimated cost of reaching the goal from state `n` should be less than or equal to the step cost of getting to state `n'` plus the estimated cost of reaching the goal from state `n'`.

`h(n) <= c + h(n')`

In our next example, we will use the `count_misplaced_tiles` heuristic function to solve the 15-puzzle problem with A\* search. The `count_misplaced_tiles` heuristic function is admissible and consistent for the 15-puzzle problem, so it is guaranteed to find the optimal solution (number of moves to solve the puzzle).

## Solving the 15-Puzzle Problem with A\* Search

To solve the 15-puzzle problem with the A\* search algorithm, we need to modify our algorithm to use both the cost of the path and the heuristic function to guide its search. The additional component we need will be the calculation of `g_value` which is the cost of the path from the start state to the current state.

```python
def a_star_search(initial_board, goal_board):
  visited = set()
  priority_queue = []

  # Initial state with a cost of 0
  heapq.heappush(priority_queue, (0, 0, (initial_board, [])))

  while priority_queue:
    current_cost, _, (board, path) = heapq.heappop(priority_queue)

    if board == goal_board:
      return path

    visited.add(tuple(board))

    for move in ['up', 'down', 'left', 'right']:
      next_board = make_move(board, move)
      if next_board and tuple(next_board) not in visited:
        heuristic = manhattan_distance(next_board, goal_board)
        g_value = current_cost + 1  # Increment the cost
        if heuristic is not None:
          total_cost = heuristic + g_value
          heapq.heappush(priority_queue,
                         (total_cost, g_value, (next_board, path + [move])))

  return None
```

Here is the full code for the 15-Puzzle problem with A\* search:

<iframe src="https://replit.com/@kibocurriculum/15-Puzzle-A-STAR-search?embed=true" width="100%" height="450"></iframe>

<!-- 


```python
from collections import deque
import heapq
# Board dimension
N = 4


def count_misplaced_tiles(board, goal_board):
  out_of_place_tiles_count = 0
  for i in range(N * N):
    if board[i] != goal_board[i]:
      out_of_place_tiles_count += 1
  return out_of_place_tiles_count


def is_valid_move(pos, move):
  row, col = divmod(pos, N)
  if move == 'up' and row == 0:
    return False
  if move == 'down' and row == N - 1:
    return False
  if move == 'left' and col == 0:
    return False
  if move == 'right' and col == N - 1:
    return False
  return True


def make_move(board, move):
  empty_pos = board.index(0)

  if not is_valid_move(empty_pos, move):
    return None

  row, col = divmod(empty_pos, N)
  if move == 'up':
    target_pos = (row - 1) * N + col
  elif move == 'down':
    target_pos = (row + 1) * N + col
  elif move == 'left':
    target_pos = row * N + (col - 1)
  elif move == 'right':
    target_pos = row * N + (col + 1)

  new_board = board[:]
  new_board[empty_pos], new_board[target_pos] = new_board[
      target_pos], new_board[empty_pos]

  return new_board


def a_star_search(initial_board, goal_board):
  visited = set()
  priority_queue = []

  # Initial state with a cost of 0
  heapq.heappush(priority_queue, (0, 0, (initial_board, [])))

  while priority_queue:
    current_cost, _, (board, path) = heapq.heappop(priority_queue)

    if board == goal_board:
      return path

    visited.add(tuple(board))

    for move in ['up', 'down', 'left', 'right']:
      next_board = make_move(board, move)
      if next_board and tuple(next_board) not in visited:
        heuristic = count_misplaced_tiles(next_board, goal_board)
        g_value = current_cost + 1  # Increment the cost
        if heuristic is not None:
          total_cost = heuristic + g_value
          heapq.heappush(priority_queue,
                         (total_cost, g_value, (next_board, path + [move])))

  return None


def print_solution(board, solution):
  print("Initial board:")
  print_board(board)
  for move in solution:
    board = make_move(board, move)
    print(f"\nMove {move}:")
    print_board(board)
  print(len(solution))
  #input()


def print_board(board):
  for i in range(N):
    print(board[i * N:i * N + N])
  print()


if __name__ == "__main__":
  # Adjust for a 4x4 board
  goal_board = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
  # Provide a valid initial configuration for a 4x4 board
  #initial_board = [7, 9, 4, 15, 3, 0, 11, 6, 13, 8, 14, 5, 1, 12, 2, 10]
  #initial_board = [14, 12, 7, 15, 4, 13, 1, 2, 10, 9, 3, 6, 11, 8, 0, 5]
  #initial_board = [4,0,8,1,14,7,10,13,3,6,5,2,11,15,12,9]
  #initial_board = [2, 11, 1, 9, 15, 5, 6, 13, 8, 7, 12, 4, 10, 0, 3, 14]
  initial_board = [0, 5, 6, 3, 9, 1, 2, 4, 10, 7, 11, 15, 13, 14, 12, 8]

  astar_solution = a_star_search(initial_board, goal_board)

  print("\nA* Solution:")
  if astar_solution:
    print_solution(initial_board, astar_solution)
  else:
    print("No solution found with A*")
``` -->

The output of the program is:

```
A* Solution:
# some steps omitted
.....
Move up:
[1, 2, 3, 4]
[5, 6, 11, 7]
[9, 10, 0, 8]
[13, 14, 15, 12]


Move up:
[1, 2, 3, 4]
[5, 6, 0, 7]
[9, 10, 11, 8]
[13, 14, 15, 12]


Move right:
[1, 2, 3, 4]
[5, 6, 7, 0]
[9, 10, 11, 8]
[13, 14, 15, 12]


Move down:
[1, 2, 3, 4]
[5, 6, 7, 8]
[9, 10, 11, 0]
[13, 14, 15, 12]


Move down:
[1, 2, 3, 4]
[5, 6, 7, 8]
[9, 10, 11, 12]
[13, 14, 15, 0]

24
```

Comparing that with the number of steps taken by the greedy best-first search algorithm, we can see that the A\* search algorithm found the optimal solution with 24 steps, while the greedy best-first search algorithm found a solution with 187 steps.

## Variants of A\* Search

A* (A-star) search is a widely used algorithm for finding the shortest path in a graph or solving optimization problems. It uses a heuristic to guide the search, making it more efficient than traditional uninformed search algorithms. There are different variations of A* search, each tailored to specific types of problems or computational constraints. Here are some notable variations:

### Basic A<sup>*</sup> Search:

The standard A<sup>*</sup> algorithm uses a combination of the cost to reach a node (g) and a heuristic estimate of the cost to reach the goal from that node (h). The evaluation function is f(n) = g(n) + h(n). A* expands nodes with the lowest f(n) value.

### Weighted A<sup>*</sup> Search:

Weighted A<sup>*</sup> introduces a weight factor to the heuristic function, influencing the balance between the cost to reach the node and the estimated cost to the goal. This can be useful for adjusting the algorithm's behavior, favoring either optimality or speed.

### Bidirectional A<sup>*</sup> Search:

In bidirectional A<sup>*</sup> search, the search is performed simultaneously from both the start and goal states. The algorithm continues until the two searches meet in the middle. This approach can be more efficient for certain types of graphs, especially when the branching factor is high.

### Real-Time A<sup>*</sup> Search:

Real-Time A* is an extension of A* designed for environments where computation time is limited. It uses an incremental approach, exploring nodes in the order of their estimated cost until the available time runs out, returning the best solution found.

These variations address different challenges and requirements, making A<sup>*</sup> adaptable to a wide range of problem domains and computational constraints. The choice of a specific variation depends on the characteristics of the problem, available resources, and the desired trade-offs between optimality and efficiency.

# Summary

The A* search algorithm is an informed search algorithm that uses both the cost of the path and the heuristic function to guide its search. The A* search algorithm is guaranteed to find the optimal solution if the heuristic function is admissible and consistent.
