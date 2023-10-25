## A\* Search Algorithm

In our previous lesson, we learned about the breadth-first search and depth-first search algorithms. Both of these algorithms are blind search algorithms, which means that they do not use any additional information to guide their search. The technical term for blind search algorithms is **uninformed** search algorithms. Using uninformed search algorithms can be inefficient and computationally expensive because they do not use any additional information to guide their search. We saw that when we applied BFS to the 15-Puzzle problem. We waited for a long time for the algorithm to find the solution and sometimes it was not able to find the solution at all.

In this lesson, we will learn about the A\* search algorithm, which is an **informed** search algorithm. Informed search algorithms use additional information to guide their search. This should make them more efficient and less computationally expensive than uninformed search algorithms. We will use the A\* search algorithm to solve the 15-Puzzle problem and the car path problem and compare its performance with uninformed search algorithms.

## Informed Search

To get a sense of how informed search algorithms work, let's consider our car example from the previous lesson. Take a look at this image:

<p align="center">
  <img src="../../images/car-state-decision.png" alt="Car State Decision" width="400">
</p>

If the car is at position `(2,1)` , as humans, we can easily determine that the next step should be to move to `(2,2)` and the `(1,1)` cell will take us further away from the goal state. This is the kind of information that we can use to guide our search algorithm making it more efficient.

## A\* Search Algorithm

The A\* search algorithm is an informed search algorithm that uses a heuristic function to guide its search.

## Heuristic Function

A heuristic function is a function that assesses alternatives in search algorithms at each branching step, utilizing available information to determine which branch to follow (which next state to explore).

In our previous example, if we can inform the algorithm to prioritize the point `(2,2)` as it is closer to the goal state than `(1,1)` , then the algorithm will be able to make a better decision. This is the kind of information that a heuristic function can provide.

### Different Heuristic Functions

Based on the nature of the problem, we can design different heuristic functions. For instance, in our car example, we can use the direct line distance between the goal state and each state as a heuristic function. In the 15-Puzzle problem, we can use the number of misplaced tiles as a heuristic function. Let's modify the 15-Puzzle problem to use the A\* search algorithm and see how it performs.

# Summary

Heuristic functions are a crucial topic in AI as they significantly impact the performance of search algorithms. We will delve into various heuristic functions in the upcoming lesson. For now, contemplate other heuristic functions that can be applied to our car and 15-puzzle examples.

Note:
The design of effective heuristic functions holds great importance in AI, as it profoundly influences the performance of search algorithms. In the next lesson, we will explore different heuristic functions. For now, consider alternative heuristic functions that can be utilized in our car and 15-puzzle examples.

<!--
## Manhattan distance

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

    def find_path_astar(self):
        open_list = []
        open_set = set()
        closed_set = set()

        # Each element in the open_list is a tuple: (f_value, g_value, state, path)
        open_list.append((self.manhattan_distance(self.start_state, self.goal_state), 0, self.start_state, []))
        open_set.add(self.start_state)

        while open_list:
            open_list.sort()  # Sort by f_value to prioritize lower values
            _, g_value, current_state, current_path = open_list.pop(0)

            if current_state == self.goal_state:
                return current_path + [current_state]

            open_set.remove(current_state)
            closed_set.add(current_state)

            neighbors = self.get_neighbors(current_state)

            for neighbor in neighbors:
                if neighbor in closed_set:
                    continue  # Skip already explored states

                tentative_g_value = g_value + 1  # Assuming uniform cost

                if neighbor not in open_set or tentative_g_value < g_value:
                    open_set.add(neighbor)
                    open_list.append((
                        tentative_g_value + self.manhattan_distance(neighbor, self.goal_state),
                        tentative_g_value,
                        neighbor,
                        current_path + [current_state]
                    ))

    def manhattan_distance(self, state1, state2):
        return abs(state1[0] - state2[0]) + abs(state1[1] - state2[1])

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

```
