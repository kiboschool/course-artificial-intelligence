# Informed Search

In our previous lessons, we learned about the breadth-first search and depth-first search algorithms. Both of these algorithms are blind search algorithms, which means that they do not use any additional information to guide their search. The technical term for blind search algorithms is **uninformed** search algorithms.

Using uninformed search algorithms can be inefficient and computationally expensive because they do not use any additional information to guide their search. We saw that when we applied BFS to the 15-Puzzle problem. We waited for a long time for the algorithm to find the solution and sometimes it was not able to find the solution at all.

In this lesson, we will learn about the A\* search algorithm, which is an **informed** search algorithm. Informed search algorithms use additional information to guide their search. This should make them more efficient and less computationally expensive than uninformed search algorithms. We will use the A\* search algorithm to solve the 15-Puzzle problem and the car path problem and compare its performance with uninformed search algorithms.

## Informed Search

To get a sense of how informed search algorithms work, let's consider our car example. Take a look at this image:

<p align="center">
  <img src="../../images/car-state-decision.png" alt="Car State Decision" width="400">
</p>

If the car is at position `(2,1)` , as humans, we can easily determine that the next step should be to move to `(2,2)`. The `(1,1)` cell will take us further away from the goal state. This is the kind of information that we can use to guide our search algorithm making it more efficient.

## Greedy best-first search

Greedy best-first search is an informed search algorithm that uses a heuristic function to guide its search.

A **heuristic function** is a function that assesses alternatives in search algorithms at each branching step, utilizing available information to determine which branch to follow (which next state to explore).

In our previous car example, if we can inform the algorithm to prioritize the point `(2,2)` as it is closer to the goal state than `(1,1)` , then the algorithm will be able to make a better decision. In a grid world, we can use the direct line distance between the goal state and each state as a heuristic function. Let's modify our car example to use the greedy best-first search algorithm and see how it performs.

## Solving the Car Path Problem with Greedy Best-First Search

```python

```

## Solving the 15-Puzzle Problem with Greedy Best-First Search

```python

```


## A\* Search Algorithm

The A\* search algorithm is an informed search algorithm. Beside using a heuristic function, like the greedy best-first search algorithm, it also uses the cost of the path from the start state to the current state to guide its search. The cost of the path is also known as the **g-value**. As a function. it is denoted as `g(n)`. The heuristic function is denoted as `h(n)`. The A\* search algorithm uses the following function to guide its search:

`f(n) = g(n) + h(n)`


### Different Heuristic Functions

Based on the nature of the problem, we can design different heuristic functions. For instance, in our car example, we can use the direct line distance between the goal state and each state as a heuristic function. In the 15-Puzzle problem, we can use the number of misplaced tiles as a heuristic function. Let's modify the 15-Puzzle problem to use the A\* search algorithm and see how it performs.

## Solving the 15-Puzzle Problem with A\* Search

TODO - Add the 15-Puzzle problem with A\* search

# Summary

Heuristic functions are a crucial topic in AI as they significantly impact the performance of search algorithms. We will delve into various heuristic functions in the upcoming lesson. For now, contemplate other heuristic functions that can be applied to our car and 15-puzzle examples.

Note:
The design of effective heuristic functions holds great importance in AI, as it profoundly influences the performance of search algorithms. In the next lesson, we will explore different heuristic functions. For now, consider alternative heuristic functions that can be utilized in our car and 15-puzzle examples.