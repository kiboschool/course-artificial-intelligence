# Search Trees


## Search Tree for Car Example

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

## Modeling Search Trees in Code

There are different ways to model a search tree, which represents our state space, in code. A search tree, like any other tree, is a special type of graph. As you might recall from your DSA class, a graph is a non-linear data structure consisting of nodes connected by edges. Each node can have zero or more child nodes.

Since our state space in this example is quite simple, we can model it as a graph using a graph data structure.

Below is a sample graph representation in Python:

```python
class Node:

  def __init__(self, state, parent=None, attributes=None):
    self.state = state  # for each node to hold its state
    self.parent = parent  # the node to keep track of its parent
    self.attributes = attributes  # to hold any other attributes

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

  def add_edge(self, node1: Node, node2: Node, weight=1):
    if node1 not in self.graph:
      self.add_node(node1)
    if node2 not in self.graph:
      self.add_node(node2)
    if (node2, weight) not in self.graph[node1]:  # Prevent duplicate edges
      self.graph[node1].append((node2, weight))

  def get_neighbors(self, node: Node):
    return self.graph.get(node, None)

  def get_node(self, state):
  # This function should return a node with a given state if it exists in the graph
    for node in self.graph:
        if node.state == state:
            return node
    return None


  def __str__(self):
    return "\n".join(
        f"{node.state}: {', '.join([f'{v.state} ({w})' for v, w in edges])}"
        for node, edges in self.graph.items())

```

### Graphs Refresher

If the above code doesn't look familiar to you, or you need a refresher on Graphs, check out this [lesson](../../refreshers/graphs.md).

Here is a slightly modified version of the code above that will help us model our search tree better:

## Coding the Car Example Search Tree

```python
def build_car_nav_graph(blocked_cells):
  graph = Graph()
  GRID_SIZE = 7
  for i in range(GRID_SIZE):
      for j in range(GRID_SIZE):
          if (i, j) in blocked_cells:
              continue

          current_node = Node((i, j))
          graph.add_node(current_node)

          # Check and add right neighbor
          if j + 1 < GRID_SIZE:
              right_node = Node((i, j + 1))
              if right_node.state not in blocked_cells:
                  graph.add_edge(current_node, right_node)

          # Check and add bottom neighbor
          if i + 1 < GRID_SIZE:
              bottom_node = Node((i + 1, j))
              if bottom_node.state not in blocked_cells:
                  graph.add_edge(current_node, bottom_node)

          # Check and add left neighbor
          if j - 1 >= 0:
              left_node = Node((i, j - 1))
              if left_node.state not in blocked_cells:
                  graph.add_edge(current_node, left_node)

          # Check and add top neighbor
          if i - 1 >= 0:
              top_node = Node((i - 1, j))
              if top_node.state not in blocked_cells:
                  graph.add_edge(current_node, top_node)

  return graph



blocked_cells = [(1,2), (1,3) ,(1,4) ,(1,5), (3,1), (3,2), (3,3), (3,4), (5,1), (5,2),(5,3),(3,6), (4,6), (5,6)]

graph = build_car_nav_graph(blocked_cells)
print(graph)
```
