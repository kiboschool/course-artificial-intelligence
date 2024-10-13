# Agents and Environments


## What is AI?
Last week, we learned about the definition of intelligence and the different types of intelligence. We also learned about the history of AI and the different approaches to AI.

To recall, below are some definitions of AI:

- The science of making machines do things that would require intelligence if done by humans. (Marvin Minsky)

- The science of building systems that can think and act rationally.

- The field concerned with understanding and building intelligent entities that can act effectively and safely in a wide range of situations. (Stuart Russell and Peter Norvig)


- Alan Turing proposed a test of AI that measures the machine's ability to engage in natural language conversation, store and represent knowledge, and reason.

## Agents and Environments
In AI, the term agent refers to anything that can act intelligently in an environment. Most of the time when we talk about agents, we are referring to computer programs.However, agents can also be humans or robots. 

Russell and Norvig define an agent as anything that can perceive its environment through sensors and act upon that environment through actuators.

Examples of agents:
- A human playing chess
- A robot vacuum cleaner
- A computer program that plays tic-tac-toe
- A computer program that recommends movies
- A computer program that controls a self-driving car

## Agent Performance
We measure the performance of an agent by its performance measure, which is a function that measures how well the agent is doing in the environment. The performance measure is different for different types of agents. For example, the performance measure for a chess-playing agent might be the percentage of games won, while the performance measure for a movie recommendation agent might be the percentage of movies recommended that the user likes.


An **intelligent/rational** agent should select an action that is expected to maximize its utility (performance measure), given the evidence provided by the percept sequence and whatever built-in knowledge the agent has.

The environment is the part of the world that is relevant to the agent. The environment includes everything that the agent operates within.

Environments can be classified along several dimensions:

- Fully observable vs. partially observable
- Deterministic vs. stochastic
- Episodic vs. sequential
- Static vs. dynamic
- Discrete vs. continuous
- Single-agent vs. multi-agent

<aside>

The enviroments we worked with in the previous week were fully observable, deterministic, sequential, static, discrete, and single-agent.

- Fully observable means we have access to the complete state of the environment at each point in time.
- Deterministic means the next state of the environment is completely determined by the current state and the action executed by the agent. There is no guessing or randomness involved.
- Sequential means the current decision could affect all future decisions.
- Static means the environment does not change while the agent is deliberating.

</aside>


### AI Assistant Tip
Get a glance at the different types of agents and environments by asking ChatGPT to explain the above terms. You can use simple prompts like:

- Explain "TEXT_HERE"
- Explain with real-world examples "TEXT_HERE".

<p style=" align:center;font-size:160%;font-family:courier; color:orange;">
  💬 Share with your peers what you learned from ChatGPT and discuss any questions you have. <a target = "_blank" href="https://discord.com/channels/1018949047626760252/1224018834952814602">here</a>.
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

