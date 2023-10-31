from collections import deque


class Node:
    """A node in a search tree. Contains a pointer to the parent (the node
    that this is a successor of) and to the actual state for this node. Note
    that if a state is arrived at by two paths, then there are two nodes with
    the same state. Also includes the action that got us to this state, and
    the total path_cost (also known as g) to reach the node."""

    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action_to_self = action

    def __repr__(self):
        return str(self.state)

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __hash__(self):
        return hash(self.state)


class Graph:
    def __init__(self):
        self.graph = {}  # dictionary of node -> list of connected vertices

    def add_node(self, node: Node):
        self.graph.setdefault(node, [])

    def add_edge(self, node1: Node, node2: Node, weight: int):
        if node1 not in self.graph:
            self.add_node(node1)
        if node2 not in self.graph:
            self.add_node(node2)
        if (node2, weight) not in self.graph[node1]:  # Prevent duplicate edges
            self.graph[node1].append((node2, weight))

    def get_neighbors(self, node: Node):
        return self.graph.get(node, None)

    def __str__(self):
        return "\n".join(f"{node.state}: {', '.join([f'{v.state} ({w})' for v, w in edges])}" for node, edges in self.graph.items())


def build_maze_graph(blocked_cells):
    graph = Graph()

    for i in range(6):
        for j in range(6):
            if (i, j) not in blocked_cells:
                current_node = Node((i, j), None, None)
                graph.add_node(current_node)

                # Check and add right neighbor
                if j < 5 and (i, j+1) not in blocked_cells:
                    right_node = Node((i, j+1), None, None)
                    graph.add_edge(current_node, right_node, 1)

                # Check and add bottom neighbor
                if i < 5 and (i+1, j) not in blocked_cells:
                    bottom_node = Node((i+1, j), None, None)
                    graph.add_edge(current_node, bottom_node, 1)

                # Check and add left neighbor
                if j > 0 and (i, j-1) not in blocked_cells:
                    left_node = Node((i, j-1), None, None)
                    graph.add_edge(current_node, left_node, 1)

                # Check and add top neighbor
                if i > 0 and (i-1, j) not in blocked_cells:
                    top_node = Node((i-1, j), None, None)
                    graph.add_edge(current_node, top_node, 1)

    return graph


def bfs(graph, start_state, goal_state):
    start = Node(start_state, None, None)
    goal = Node(goal_state, None, None)
    frontier = deque([start])
    explored = set()

    while frontier:
        current_node = frontier.popleft()

        if current_node == goal:
            # reconstruct the path
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]

        explored.add(current_node)

        for neighbor, _ in graph.get_neighbors(current_node) or []:
            if neighbor not in frontier and neighbor not in explored:
                neighbor.parent = current_node
                frontier.append(neighbor)

    return None


def dfs(graph, start_state, goal_state):
    start = Node(start_state, None, None)
    goal = Node(goal_state, None, None)
    stack = [start]
    explored = set()

    while stack:
        current_node = stack.pop()

        if current_node == goal:
            # reconstruct the path
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]

        explored.add(current_node)

        for neighbor, _ in graph.get_neighbors(current_node) or []:
            if neighbor not in stack and neighbor not in explored:
                neighbor.parent = current_node
                stack.append(neighbor)

    return None


blocked_cells = [(1, 2), (1, 3), (1, 4), (1, 5), (3, 1), (3, 2),
                 (3, 3), (3, 4), (5, 1), (5, 2), (5, 3), (3, 6), (4, 6), (5, 6)]
maze_graph = build_maze_graph(blocked_cells)

# Using BFS
path_bfs = bfs(maze_graph, (0, 1), (5, 5))
print("Path using BFS:", path_bfs)

# Using DFS
path_dfs = dfs(maze_graph, (0, 1), (5, 5))
print("Path using DFS:", path_dfs)
