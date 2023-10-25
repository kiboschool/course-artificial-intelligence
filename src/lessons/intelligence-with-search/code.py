from collections import deque

class Graph:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.graph = [[0 for _ in range(cols)] for _ in range(rows)]
        self.visited_cells = 0  # Initialize the visited cells counter

    def add_edge(self, start, end):
        self.graph[start[0]][start[1]] = 1
        self.graph[end[0]][end[1]] = 1

    def is_valid_move(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols and self.graph[x][y] != 1

    def find_path_bfs(self, start, end):
        visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        queue = deque([(start, [])])

        while queue:
            current, path = queue.popleft()
            x, y = current

            if current == end:
                return path + [current]

            if not self.is_valid_move(x, y) or visited[x][y]:
                continue

            visited[x][y] = True
            self.visited_cells += 1  # Increment the visited cells counter

            # Explore neighbors
            neighbors = [(x + 1, y), (x, y + 1)]
            for neighbor in neighbors:
                if self.is_valid_move(*neighbor):
                    queue.append((neighbor, path + [current]))

        return None


    def find_path_dfs(self, start, end, path=[]):
        if start == end:
            return path + [end]

        x, y = start
        if not self.is_valid_move(x, y):
            return None

        if path is None:
            path = []

        path.append(start)

        # Increment the visited cells counter
        self.visited_cells += 1

        # Explore neighbors
        if self.is_valid_move(x + 1, y):
            if self.find_path_dfs((x + 1, y), end, path):
                return path

        if self.is_valid_move(x, y + 1):
            if self.find_path_dfs((x, y + 1), end, path):
                return path

        # If no path is found, backtrack
        path.pop()
        return None
    
# Create the graph
rows, cols = 8, 8
g = Graph(rows, cols)

# Add blocked cells to the graph
blocked_cells = [(2, 3), (2, 4), (3, 2), (3, 3), (3, 4)]
for cell in blocked_cells:
    g.graph[cell[0]][cell[1]] = 1

# Find and print the path from (0, 0) to (7, 7) using DFS
start_node = (1, 0)
end_node = (7, 7)
path = g.find_path_bfs(start_node, end_node)

if path:
    print("Path from (0, 0) to (7, 7):")
    for node in path:
        print(node)
    print("Number of visited cells:", g.visited_cells)
else:
    print("No path found.")
