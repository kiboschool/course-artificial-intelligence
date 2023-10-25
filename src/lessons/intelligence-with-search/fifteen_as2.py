from queue import PriorityQueue


from queue import PriorityQueue


def solve_puzzle(board):
    goal = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
    moves = 0
    previous = None
    frontier = PriorityQueue()
    frontier.put((0, board, moves, previous))
    explored = set()
    path = []
    memo = {}

    while not frontier.empty():
        _, current_board, moves, previous = frontier.get()
        path.append(current_board)
        if current_board == goal:
            return (moves, path)
        if str(current_board) in explored:
            continue
        explored.add(str(current_board))
        memo[str(current_board)] = (moves, previous)
        i, j = get_blank_position(current_board)
        for move in get_moves(i, j):
            new_board = make_move(current_board, move, i, j)
            if str(new_board) not in explored:
                new_moves = moves + 1
                if str(new_board) in memo and memo[str(new_board)][0] <= new_moves:
                    continue
                frontier.put((new_moves + heuristic(new_board),
                             new_board, new_moves, current_board))

    return None


def print_solution(moves, path):
    print(f"Number of moves: {moves}")
    for i, board in enumerate(path[:moves+1]):
        print(f"Step {i}:")
        print_board(board)

    print(f"Number of moves: {moves}")


def get_blank_position(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return (i, j)


def print_board(board):
    for row in board:
        print(" ".join(str(x).rjust(2) for x in row))
    print()


def get_moves(i, j):
    moves = []
    if i > 0:
        moves.append((-1, 0))
    if i < 3:
        moves.append((1, 0))
    if j > 0:
        moves.append((0, -1))
    if j < 3:
        moves.append((0, 1))
    return moves


def make_move(board, move, i, j):
    new_board = [row[:] for row in board]
    di, dj = move
    new_board[i][j], new_board[i+di][j +
                                     dj] = new_board[i+di][j+dj], new_board[i][j]
    return new_board


def heuristic(board):
    distance = 0
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                x, y = divmod(board[i][j] - 1, 4)
                distance += abs(x - i) + abs(y - j)
    return distance


# board = [[7, 5, 3, 4], [2, 1, 6, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
board = [[1, 2, 6, 4], [5, 3, 7, 9], [8, 10, 11, 12], [13, 0, 14, 15]]
moves, path = solve_puzzle(board)
print_solution(moves, path)
