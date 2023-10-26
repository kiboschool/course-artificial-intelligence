from queue import PriorityQueue


class Puzzle:
    def __init__(self, board, moves=0, previous=None):
        self.board = board
        self.moves = moves
        self.previous = previous
        self.goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def __lt__(self, other):
        return (self.moves + self.heuristic()) < (other.moves + other.heuristic())

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(str(self.board))

    def heuristic(self):
        count = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != self.goal[i][j]:
                    count += 1
        return count

    def get_moves(self):
        moves = []
        i, j = self.get_blank_position()
        if i > 0:
            moves.append((-1, 0))
        if i < 2:
            moves.append((1, 0))
        if j > 0:
            moves.append((0, -1))
        if j < 2:
            moves.append((0, 1))
        return moves

    def get_blank_position(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return i, j

    def make_move(self, move):
        i, j = self.get_blank_position()
        x, y = move
        new_board = [row[:] for row in self.board]
        new_board[i][j], new_board[i+x][j +
                                        y] = new_board[i+x][j+y], new_board[i][j]
        return Puzzle(new_board, self.moves+1, self)

    def get_path(self):
        path = []
        node = self
        while node:
            path.append(node)
            node = node.previous
        return path[::-1]


def solve_puzzle(start):
    queue = PriorityQueue()
    queue.put(start)
    visited = set()
    while not queue.empty():
        node = queue.get()
        if node.board == node.goal:
            return node.get_path()
        visited.add(node)
        for move in node.get_moves():
            child = node.make_move(move)
            if child not in visited:
                queue.put(child)
    return None


# Example usage:
start = Puzzle([[1, 2, 3], [4, 5, 6], [0, 7, 8]])
path = solve_puzzle(start)
if path:
    for node in path:
        print(node.board)
        print()
else:
    print("No solution found.")
