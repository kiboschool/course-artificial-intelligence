# Search Algorithms

_Estimated Time: 90 - 180 minutes_

<img src="../../images/lets-solve-maze.png" />

Now that we have learned about search problems, It's time to learn how to solve them. In this lesson, we will learn about search algorithms and how to use them to solve search problems.

## Search Algorithm

<aside>

A **search algorithm** takes a search problem as input and returns a solution or indicates that no solution exists.

</aside>

We know from the previous lesson that, in our search problems, we have a starting state and a goal state. We also have a set of actions that we can take to move from one state to another. Each action leads to a new state. If we try to visualize this, we can think of it as a tree where the starting state is the root the actions are the edges that connect the nodes.

<p align="center">
  <img src="../../images/actions-states.png" alt="Search Tree" width="600">
</p>

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

We refer to these trees as **search trees**. They represent our state space in which we search for a solution. Each node in the search tree corresponds to a state in the state space, and each edge corresponds to an action. The root node of the tree represents the initial state.

This mental model of search trees will aid us in finding solutions to our search problems. We can employ various algorithms to navigate the search tree and discover a path from the initial state to the goal state.

## Depth-First Search (DFS)

You are likely familiar with the depth-first search (DFS) and breadth-first search (BFS) algorithms. Here we will employ these algorithms to traverse the search tree and find a path from the starting state to the goal state.

For a refresher on these algorithms, you can refer to this lesson: [DFS and BFS](../../refreshers/search-algorithms.md).

## Solving The Car Journey Example Using BFS

Here is the code for the car example using BFS.

```python

```

## Solving The Car Journey Example Using DFS

Here is the code for the car example using BFS.

```python

```

## Understanding Our Objective

In our previous examples, our primary objective was to find **a path** from the starting state to the goal state. We used BFS and DFS to solve the problem. However, it's important to note that not all paths are equal; some paths are better than others. Later this week, we will explore how to find the optimal path from the starting state to the goal state.

## Evaluating Search Algorithms

When evaluating search algorithms, we typically consider the following criteria:

- Completeness
- Optimality
- Time complexity
- Space complexity

### Completeness

If the algorithm is guaranteed to find a solution if one exists, then we say that the algorithm is complete. **Both BFS and DFS are complete algorithms**.

### Optimality

If the algorithm is guaranteed to find the optimal solution (lowest path code), then we say that the algorithm is optimal. **BFS is optimal, but DFS is not**.

### Time Complexity

Time complexity is the number of nodes that are expanded during the search. We typically use big-O notation to express the time complexity of an algorithm.
The time complexity of a Breadth-First Search (BFS) algorithm is typically **O(V + E)**, where V is the number of vertices and E is the number of edges in the graph being traversed. The time complexity of a Depth-First Search (DFS) algorithm is typically **O(V)** where V is the number of vertices (nodes) in the tree.

### Space Complexity

Space complexity is the maximum number of nodes that are stored in memory during the search. We use big-O notation to express the space complexity as well.
The space complexity of a Breadth-First Search (BFS) algorithm is typically O(V), where V is the number of vertices in the graph being traversed.In the case of an iterative DFS using a stack on a tree, the space complexity is O(h) where "h" is the height of the tree.

A simple indicator for us to use could be the number of nodes expanded during the search(how many nodes we visit during the search until we reach the goal).

## Which one is better?

The choice between Breadth-First Search (BFS) and Depth-First Search (DFS) depends on the specific characteristics of the problem you are trying to solve. Neither one is universally "better" than the other; they each have their own strengths and weaknesses.

Here are some considerations for when to use each search algorithm:

Use **BFS** when:

- You want to find the shortest path or the minimum number of steps to reach a goal. BFS explores nodes level by level, so it is guaranteed to find the shortest path in an unweighted graph.
- You need to visit all nodes at a given level before moving on to the next level.
- The graph has a tree structure, and you want to visit all nodes at the same depth before moving to the next level.
- You want to avoid deep recursion, which can be an issue in DFS on very deep graphs.

Use **DFS** when:

- You are interested in exploring as deeply as possible along a branch before backtracking. DFS is well-suited for tasks like finding paths or cycles.

- You have limited memory resources because, in general, DFS can use less memory (stack space) than BFS.

- You are working with a tree or a graph with a limited depth, and you prefer a simple recursive implementation.

- You want to find multiple solutions or all possible paths from a start node to a goal node.

## More Search Algorithms

There are many other search algorithms ou there.Here is a list of some of them:

- Greedy Best-First Search
- A\* Search
- Iterative Deepening Search
- Bidirectional Search
- Depth-Limited Search
- Iterative Deepening Depth-First Search
- Recursive Best-First Search
- Hill Climbing Search
- Beam Search

In this week, besides BFS and DFS, we will also learn about Greedy Best-First Search and A\* Search algorithm. Next week, we will learn more search algorithms suitable for solving more complex problems.

## Self Assesment:

- Pick a search problem and write a complete solution for it using BFS and DFS. You can use the code above as a starting point. Example problems include:
  - 8-puzzle
  - 8-queens
  - Maze
