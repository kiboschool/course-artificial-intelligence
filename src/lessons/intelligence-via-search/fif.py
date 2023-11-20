from collections import deque

# Board dimension
N = 4


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
  empty_pos = board.index(None)

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


def bfs(initial_board, goal_board):
    visited = set()
    queue = deque([(initial_board, [])])

    while queue:

        board, path = queue.popleft()
        #print(f"Current board: {board}, Path: {path}")  # Debug print

        if board == goal_board:
            return path

        visited.add(tuple(board))

        for move in ['up', 'down', 'left', 'right']:
            next_board = make_move(board, move)
            if next_board and tuple(next_board) not in visited:
                #print(f"Adding move: {move}, Board: {next_board}")  # Debug print
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
    print(board[i * N:i * N + N])
  print()


if __name__ == "__main__":
  # Adjust for a 4x4 board
  goal_board = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None]
  # Provide a valid initial configuration for a 4x4 board

  #initial_board = [8, 3, 1, 7, 2, 6, 5, 4, None, 9, 10, 11, 12, 13, 14, 15]
  initial_board = [1,8, 2, 4,5,7,3,None,9,6,11,12,13,10,14,15] # solvable
  # initial_board = [5,15,9,14,7,11,3,1,2,None,13,4,10,6,12,8] # solvable but takes a long time
  bfs_solution = bfs(initial_board, goal_board)

  print("\nBFS Solution:")
  if bfs_solution:
    print_solution(initial_board, bfs_solution)
  else:
    print("No solution found with BFS")
