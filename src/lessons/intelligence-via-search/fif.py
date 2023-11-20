from collections import deque
import heapq
# Board dimension
N = 4


def tiles_out_of_place(board, goal_board):
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


def greedy_best_first_search(initial_board, goal_board):
  visited = set()
  priority_queue = []

  heapq.heappush(priority_queue, (0, (initial_board, [])))

  while priority_queue:
    _, (board, path) = heapq.heappop(priority_queue)
    #print((board, path))
    if board == goal_board:
      return path

    visited.add(tuple(board))

    for move in ['up', 'down', 'left', 'right']:
      next_board = make_move(board, move)
      if next_board and tuple(next_board) not in visited:
        heuristic = tiles_out_of_place(next_board, goal_board)
        if heuristic is not None:
          heapq.heappush(priority_queue,
                         (heuristic, (next_board, path + [move])))

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
  initial_board = [2,11,1,9,15,5,6,13,8,7,12,4,10,0,3,14]

  bfs_solution = greedy_best_first_search(initial_board, goal_board)

  print("\nBFS Solution:")
  if bfs_solution:
    print_solution(initial_board, bfs_solution)
  else:
    print("No solution found with BFS")
