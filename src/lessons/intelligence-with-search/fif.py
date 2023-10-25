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
