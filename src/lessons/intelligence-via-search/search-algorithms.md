# Search Algorithms

_Estimated Time: 90 minutes_

Now that we understand how to model a problem as a search problem, we can begin to explore how to solve it. In this lesson, we will examine some of the most common search algorithms used to solve search problems.

## Search Tree

Starting from an initial state, there are typically several actions that can be taken to transition to a new state. From that new state, there are again several actions that can be taken to move to yet another state, and so on. This process repeats until a goal state is reached. Here is a simple example. Suppose we have an 8-puzzle game, and we want to find a path from the initial state to the goal state. The initial state might be something like this:

<p align="center">
<img src="../../images/8-puzzle-1.png" />
</p>

From this state (node), we can move the tiles 2,8,4, and 6. Each of these moves will result in a new state (node) like this.

<p align="center">
<img src="../../images/8-puzzle-2.png" />
</p>

From each new state, we can again move different tiles. Each of these moves will result in a new state (node) until we reach the goal state.

<p align="center">
<img src="../../images/8-puzzle-3.jpeg" />
</p>

As we see, this process can be visualized as a tree, where each node represents a state, and each edge represents an action. This is called a search tree. The complete tree can be very large, and it is not possible to visualize the entire tree, but you get the idea.

## Search Tree Car Example

In our car example, the starting state is the point `(1, 0)` on our modeled grid.

<p align="center">
<img src="../../images/car-state-1.png" width = "350px"/>
</p>

From this point, the car can move to points `(0, 0), (2, 0), or (1, 1`).

<p align="center">
<img src="../../images/car-state-2.png" />
</p>

From the point `(2, 0)`, the car can move to point `(2, 1)` or `(3, 0)` . Similarly, from the point `(1, 1)`, the car can move to points `(0, 1), (2, 1), or (1, 2)`, and so on.

<p align="center">
<img src="../../images/car-state-3.png" />
</p>

As you can see, the tree is growing as we move from one state to another. This is called a search tree.

## Modeling Search Trees in Code

As you probably know from your DSA class, a tree is a special type of graph. It is a non-linear data structure that consists of nodes connected by edges. Each node can have zero or more child nodes. We can use the same data structures to represent our search tree. There are two common ways to represent a graph in code: adjacency lists and adjacency matrices. Below is an example of an adjacency list representation of the search tree for our car example.

```python
# adjacency list representation of the search tree
search_tree = {
    (1, 0): [(0, 0), (2, 0), (1, 1)],
    (0, 0): [(0, 1), (1, 0)],
    (2, 0): [(1, 0), (2, 1), (3, 0)],
    (1, 1): [(0, 1), (1, 2), (1, 0), (2, 1)],
    (0, 1): [(0, 2), (1, 1), (0, 0)],
    (2, 1): [(1, 1), (2, 2), (2, 0), (3, 1)],
    (1, 2): [(0, 2), (1, 1), (2, 2)],
    (0, 2): [(0, 3), (1, 2), (0, 1)],
    (2, 2): [(1, 2), (2, 3), (2, 1), (3, 2)],
    (0, 3): [(0, 4), (1, 3), (0, 2)],
    (2, 3): [(1, 3), (2, 4), (2, 2), (3, 3)],
    (0, 4): [(0, 5), (1, 4), (0, 3)],
    (2, 4): [(1, 4), (2, 5), (2, 3), (3, 4)],
}
```

# Solving Search Problems

You are also likely familiar with some algorithms that can be employed to traverse a tree. Two of the most common traversal algorithms are depth-first search (DFS) and breadth-first search (BFS). We can use these algorithms to traverse the search tree and find a path from the starting state to the goal state.

For a refresher on these algorithms, you can refer to the following resources:

TODO: Add links below

- [Depth-First Search](https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/)
- [Breadth-First Search](https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/)
- [Depth-First Search vs Breadth-First Search](https://www.geeksforgeeks.org/difference-between-bfs-and-dfs/)

Here is also a video that explains both of them applied to a search problem:

TODO: Add video

## Car Example Solution

Following the same approach, we can use DFS or BFS to find a path from the starting state to the goal state in our car example problem.

Here is the code for the car example using DFS and BFS. A video explaining the code is also provided below.

```python
from collections import deque

class CarPath():
    def __init__(self):
        self.start_state = (1,0)
        self.goal_state = (6,6)

        self.state_space = []
        self.visited = []
        self.blocked_cells = [(1,2),(1,3),(1,4),(1,5), (3,1), (3, 2), (3, 3), (3, 4), (5,1),(5,2),(5, 3),(3,6),(4,6),(5,6)]

        for i in range(7):
            for j in range(7):
                if (i, j) in self.blocked_cells:
                    self.state_space.append(0)
                else:
                    self.state_space.append(1)
    def find_path_bfs(self):
       pass

    def find_path_dfs(self):
        pass

    def get_neighbors(self, state):
        neighbors = []
        if state[0] > 0:
            neighbors.append((state[0] - 1, state[1]))
        if state[0] < 6:
            neighbors.append((state[0] + 1, state[1]))
        if state[1] > 0:
            neighbors.append((state[0], state[1] - 1))
        if state[1] < 6:
            neighbors.append((state[0], state[1] + 1))
        return neighbors


road = CarRoad()
path_found = road.find_path_bfs()
print(path_found , road.visited)

```

You can try to complete the code above yourself before watching the video below.

TODO: Add video

### Solution

```python
from collections import deque

class CarPath():
    def __init__(self):
        self.start_state = (1,0)
        self.goal_state = (6,6)

        self.state_space = []
        self.visited = []
        self.blocked_cells = [(1,2),(1,3),(1,4),(1,5), (3,1), (3, 2), (3, 3), (3, 4), (5,1),(5,2),(5, 3),(3,6),(4,6),(5,6)]

        for i in range(7):
            for j in range(7):
                if (i, j) in self.blocked_cells:
                    self.state_space.append(0)
                else:
                    self.state_space.append(1)
    def find_path_bfs(self):
        stack = deque()
        stack.append(self.start_state)

        while len(stack) > 0:
            #print(stack)
            current_state = stack.popleft()

            if current_state == self.goal_state:
                return True

            if current_state in self.blocked_cells:
                continue #ignore it

            if current_state not in self.visited:
                #print("visited ", current_state)
                self.visited.append(current_state)
            else:
                continue

            neighbors = self.get_neighbors(current_state)

            for neighbor in neighbors:
                stack.append(neighbor)

    def find_path_dfs(self):
        stack = []
        stack.append(self.start_state)

        while len(stack) > 0:
            current_state = stack.pop(0)

            if current_state == self.goal_state:
                return True

            if current_state in self.blocked_cells:
                continue #ignore it

            if current_state not in self.visited:
                self.visited.append(current_state)
            else:
                continue

            neighbors = self.get_neighbors(current_state)
            for neighbor in neighbors:
                stack.append(neighbor)

    def get_neighbors(self, state):
        neighbors = []
        if state[0] > 0:
            neighbors.append((state[0] - 1, state[1]))
        if state[0] < 6:
            neighbors.append((state[0] + 1, state[1]))
        if state[1] > 0:
            neighbors.append((state[0], state[1] - 1))
        if state[1] < 6:
            neighbors.append((state[0], state[1] + 1))
        return neighbors


road = CarRoad()
path_found = road.find_path_bfs()
print(path_found , road.visited)

#True [(1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (1, 6), (0, 6), (0, 5), (0, 4), (0, 3), (0, 2), (0, 1), (0, 0), (3, 5), (4, 5), (4, 4), (4, 3), (4, 2), (4, 1), (4, 0), (5, 0), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)]
#True [(1, 0), (0, 0), (2, 0), (1, 1), (0, 1), (3, 0), (2, 1), (0, 2), (4, 0), (2, 2), (0, 3), (5, 0), (4, 1), (2, 3), (0, 4), (6, 0), (4, 2), (2, 4), (0, 5), (6, 1), (4, 3), (2, 5), (0, 6), (6, 2), (4, 4), (3, 5), (2, 6), (1, 6), (6, 3), (5, 4), (4, 5), (6, 4), (5, 5), (6, 5)]

```

We can modify the code above to keep track of, and print, tha path the car took to reach the goal state.

```python
from collections import deque

class CarPath():
    def __init__(self):
        self.start_state = (1, 0)
        self.goal_state = (6, 6)

        self.state_space = []
        self.visited = []
        self.blocked_cells = [(1, 2), (1, 3), (1, 4), (1, 5), (3, 1), (3, 2), (3, 3), (3, 4), (5, 1), (5, 2), (5, 3), (3, 6), (4, 6), (5, 6)]

        for i in range(7):
            for j in range(7):
                if (i, j) in self.blocked_cells:
                    self.state_space.append(0)
                else:
                    self.state_space.append(1)

    def find_path_bfs(self):
        queue = deque()
        queue.append((self.start_state, []))  # Store the state and the path to this state

        while queue:
            current_state, current_path = queue.popleft()

            if current_state == self.goal_state:
                return current_path + [current_state]

            if current_state in self.blocked_cells:
                continue  # Ignore it

            if current_state not in self.visited:
                self.visited.append(current_state)

            neighbors = self.get_neighbors(current_state)

            for neighbor in neighbors:
                if neighbor not in self.visited:
                    queue.append((neighbor, current_path + [current_state]))

    def find_path_dfs(self):
        stack = []
        stack.append((self.start_state, []))  # Store the state and the path to this state

        while stack:
            current_state, current_path = stack.pop()

            if current_state == self.goal_state:
                return current_path + [current_state]

            if current_state in self.blocked_cells:
                continue  # Ignore it

            if current_state not in self.visited:
                self.visited.append(current_state)

            neighbors = self.get_neighbors(current_state)

            for neighbor in neighbors:
                if neighbor not in self.visited:
                    stack.append((neighbor, current_path + [current_state]))

    def get_neighbors(self, state):
        neighbors = []
        if state[0] > 0:
            neighbors.append((state[0] - 1, state[1]))
        if state[0] < 6:
            neighbors.append((state[0] + 1, state[1]))
        if state[1] > 0:
            neighbors.append((state[0], state[1] - 1))
        if state[1] < 6:
            neighbors.append((state[0], state[1] + 1))
        return neighbors


road = CarPath()
path_found = road.find_path_dfs()
if path_found:
    print("Path found:", path_found)
else:
    print("No path found")
```

## Understanding Our Objective

In our previous examples, our primary objective was to find **a path** from the starting state to the goal state. However, it's important to note that not all paths are equal; some paths are better than others. Later this week, we will explore how to find the shortest path from the starting state to the goal state.
