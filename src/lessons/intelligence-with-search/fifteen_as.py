from queue import PriorityQueue


def solve_puzzle(board):
    goal = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
    moves = 0
    previous = None
    frontier = PriorityQueue()
    frontier.put((0, board, moves, previous))
    explored = set()

    while not frontier.empty():
        _, current_board, moves, previous = frontier.get()
        if current_board == goal:
            return (moves, previous)
        if str(current_board) in explored:
            continue
        explored.add(str(current_board))
        i, j = get_blank_position(current_board)
        for move in get_moves(i, j):
            new_board = make_move(current_board, move, i, j)
            if str(new_board) not in explored:
                new_moves = moves + 1
                frontier.put((new_moves + heuristic(new_board),
                             new_board, new_moves, current_board))

    return None


def get_blank_position(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return (i, j)


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

# def heuristic(board):
#     count = 0
#     for i in range(4):
#         for j in range(4):
#             if board[i][j] != 0 and board[i][j] != (4*i + j + 1):
#                 count += 1
#     return count


# from queue import PriorityQueue


# def solve_puzzle(board):
#     goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
#     moves = 0
#     previous = None
#     frontier = PriorityQueue()
#     frontier.put((0, board, moves, previous))
#     explored = set()

#     while not frontier.empty():
#         _, current_board, moves, previous = frontier.get()
#         if current_board == goal:
#             return (moves, previous)
#         if str(current_board) in explored:
#             continue
#         explored.add(str(current_board))
#         i, j = get_blank_position(current_board)
#         for move in get_moves(i, j):
#             new_board = make_move(current_board, move, i, j)
#             if str(new_board) not in explored:
#                 new_moves = moves + 1
#                 frontier.put((new_moves + heuristic(new_board),
#                              new_board, new_moves, current_board))

#     return None


# def get_blank_position(board):
#     for i in range(3):
#         for j in range(3):
#             if board[i][j] == 0:
#                 return (i, j)


# def get_moves(i, j):
#     moves = []
#     if i > 0:
#         moves.append((-1, 0))
#     if i < 2:
#         moves.append((1, 0))
#     if j > 0:
#         moves.append((0, -1))
#     if j < 2:
#         moves.append((0, 1))
#     return moves


# def make_move(board, move, i, j):
#     new_board = [row[:] for row in board]
#     di, dj = move
#     new_board[i][j], new_board[i+di][j +
#                                      dj] = new_board[i+di][j+dj], new_board[i][j]
#     return new_board


# def heuristic(board):
#     count = 0
#     for i in range(3):
#         for j in range(3):
#             if board[i][j] != 0 and board[i][j] != (3*i + j + 1):
#                 count += 1
#     return count

board = [[1, 2, 6, 4], [5, 3, 7, 9], [8, 10, 11, 12], [13, 0, 14, 15]]
print(solve_puzzle(board))
