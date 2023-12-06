# Week 1 Review
Before starting this week's lesson, let's review what we learned in Week 1.


## AI
We defined Intelligence as the ability to make rational decisions (decisions grounded in reason, logic, and knowledge).

We defined AI as the science of building systems that can think and act rationally.

Here are a few other related definitions of AI:

- The field concerned with understanding and building intelligent entities that can act effectively and safely in a wide range of situations. (Stuart Russell and Peter Norvig)

- The science of making machines do things that would require intelligence if done by humans. (Marvin Minsky)

- Alan Turing proposed a test of AI that measures the machine's ability to engage in natural language conversation, store and represent knowledge, and reason.

## Agents and Environments
An agent is anything that can perceive its environment through sensors and act upon that environment through actuators (Stuart Russell and Peter Norvig). An agent can be a human, a robot, or a computer program. Examples of agents include:

- A human playing chess
- A robot vacuum cleaner
- A computer program that plays tic-tac-toe
- A computer program that recommends movies
- A computer program that controls a self-driving car

An **intelligent/rational** agent should select an action that is expected to maximize its utility (performance measure), given the evidence provided by the percept sequence and whatever built-in knowledge the agent has.

The environment is the part of the world that is relevant to the agent. The environment includes everything that the agent operates within.

Environments can be classified along several dimensions:

- Fully observable vs. partially observable
- Deterministic vs. stochastic
- Episodic vs. sequential
- Static vs. dynamic
- Discrete vs. continuous
- Single-agent vs. multi-agent

### AI Assistant Tip
Get a glance at the different types of agents and environments by asking ChatGPT to explain the above terms. You can use simple prompts like:

- Explain "TEXT_HERE"
- Explain with real-world examples "TEXT_HERE".

<p style=" align:center;font-size:160%;font-family:courier; color:orange;">
  💬 Share with your peers what you learned from ChatGPT and discuss any questions you have. <a target = "_blank" href="https://discord.com/channels/1167059986019520563/1167060638300913786">here</a>.
  </p>

## Search Problems
A search problem is a specific type of computational problem that involves exploring a set of possible states or configurations (known as the state space) and finding a sequence of actions to achieve a goal within this state space.

### Examples of search problems include:

- Finding the optimal path between two cities on a map
- Finding the best move in a game
- Finding optimal arrangements of components and connections to achieve desired functionality in electronic circuit design
- Robot Navigation

## Search Algorithms
A search algorithm is an algorithm that takes a problem as input and returns a solution to the problem, usually after exploring a set of possible states or configurations (known as the state space).

### Examples of search algorithms include:

- Breadth-first search
- Depth-first search
- Uniform-cost search
- A* search
- Monte Carlo tree search

### Informed Search
Informed search algorithms use problem-specific knowledge to find solutions more efficiently than uninformed search algorithms. This problem-specific knowledge is provided by a heuristic function.

## Heuristic Functions
A heuristic function is a function that estimates the cost of the cheapest path from a given state to the goal state. The heuristic function is problem-specific and is provided by the user. Examples of heuristic functions include:

- The straight-line distance between two cities on a map
- The number of misplaced tiles in a puzzle
- The number of inversions in a puzzle
- The Manhattan distance between two cities on a map


Now that we have reviewed the main concepts from Week 1, let's move on to this week's lesson on adversarial search and game playing.

