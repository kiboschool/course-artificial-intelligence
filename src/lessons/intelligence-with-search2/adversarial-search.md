[DRAFT]: # "Lesson is being edited"

# Adversarial Search

So far, the problems we have examined have been single-agent problems. In other words, there is only one agent (such as a car or a player of a 15-puzzle game) attempting to solve the problem, such as finding a path to a goal point or rearranging the tiles to the correct order. However, in many problems, especially games like tic-tac-toe, there are two agents trying to solve the problem, each one acting against the other. In this lesson, we will explore how to address such problems.

## Adversarial Scenarios

In a [pacman](https://en.wikipedia.org/wiki/Pac-Man) game, the pacman agent is trying to eat all the food pellets while avoiding the ghosts. The ghosts are trying to eat the pacman. In a [chess](https://en.wikipedia.org/wiki/Chess) game, the white player is trying to checkmate the black player, while the black player is trying to checkmate the white player. In a [tic-tac-toe](https://en.wikipedia.org/wiki/Tic-tac-toe) game, the two players are trying to get three of their pieces in a row before the other player does. In all of these games, the two agents are trying to solve the same problem, but they are acting against each other. This is called an adversarial search problem.

### Solving Adversarial Search Problems

In a tic-tac-toe game like the one shown below, if you are the X player, what would be your next move and why?

![Tic-Tac-Toe](../../images/tic-tac-toe.png)

I bet you choose to place X at position 5. Why? Because it is the move to prevent the O player from winning. In other words, you are trying to minimizing the score of the O player.

What about this game? if you are the X player, What would be your next move and why?
![Tic-Tac-Toe](../../images/tic-tac-toe2.png)

The right move here is to place X at position 1. Why? Because it is the move to make you win. In other words, you are trying to maximize your score.
We know this because we are humans and we have played this game many times. But how can we teach a computer to play this game? Thinking about the problem this way will help us formalize the algorithm. We will discuss the **minimax** strategy in the next section which is one way to help us solve adversarial search problems(teaching a computer to play similar games).

## Minimax Algorithm

The minimax algorithm is a strategy used in decision making, particularly in game theory and artificial intelligence, for minimizing the possible loss while maximizing the potential gain. It's often applied in two-player games like chess or tic-tac-toe. Here's how it works:

In a game, there are two players. One is the maximizer, who tries to get the highest score possible, while the other is the minimizer, who tries to do the opposite and minimize the score.

In a tic-tac-toe game, the maximizer for example is the player who has the X symbol and the minimizer is the player who has the O symbol. When X makes a move, it tries to maximize the score, while O tries to minimize it.

To illustrate this, let's only consider the next two moves of the game shown below. The maximizer (X) has two possible moves, either place X at position 1 or position 5. If X places its symbol at position 1, the minimizer (O) has two possible moves, either place O at position 2 or position 5. If X places its symbol at position 5, the minimizer (O) has two possible moves, either place O at position 2 or position 4. The minimizer (O) will choose the move that minimizes the score of the maximizer (X). In other words, the minimizer (O) will choose the move that is worst for the maximizer (X). In this case, the minimizer (O) will choose to place O at position 2. This is the first level of the tree.

![Tic-Tac-Toe](../../images/tic-tac-toe3.png)

This explains how the mini-max algorithm works. It is a recursive algorithm that computes the best move for the maximizer by assuming that the minimizer is also playing optimally. In other words, it assumes that the minimizer is trying to minimize the score of the maximizer. The algorithm computes the score of each possible move and returns the move with the highest score.

### if you feel you don't understand the algorithm yet, here are two videos that explains the algorithm in 2 different ways:

[![Minimax Algorithm](https://img.youtube.com/vi/l-hh51ncgDI/0.jpg)](https://www.youtube.com/watch?v=l-hh51ncgDI)

[![Minimax Algorithm](https://img.youtube.com/vi/6ELUvkSkCts/0.jpg)](https://www.youtube.com/watch?v=6ELUvkSkCts)

Let's formulate the problem as we did before in the previous lesson. We will use the same notation as before.

- **Initial State**: As in any search problem, the game has an initial state. In the tic-tac-toe game, the initial state is the empty board. One difference between this problem and the previous search problems is that the initial state is known and fixed. This is how many games work. The initial state is known and fixed, and the two players take turns making moves until the game is over.
- **Actions**: The actions in this problem are the possible moves that the players can make. To address this correctly, we need to know the player who is making the move next. So we need to keep track of the current player.
- **Current Player**: This is a function that at any given point in the game, returns the player who is making the next move.
- **Transition Model**: This is a function that takes the current state and the player, and returns the next play. This function must be supported by another function that calculates the best move to make.
- **Utility Function**: This is a function that takes a state and returns a score.
- **Terminal Test**: This is a function that checks if the game is over. In other words, it checks if the game has reached a terminal state. In the tic-tac-toe game, the game is over when one of the players wins or when the board is full.

### Minimax Pseudocode

#### Minimax Implementation

### Demo
