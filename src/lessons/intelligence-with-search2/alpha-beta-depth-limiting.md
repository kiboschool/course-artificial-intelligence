# Alpha-Beta and Depth-Limiting

As we saw in our previous lesson, the minimax algorithm is a great way to find the best move in a two-player, zero-sum game. However, it has one major drawback: it is very slow. In fact, it is so slow that it is not practical to use it in most games. In this lesson, we will look at two ways to speed up the minimax algorithm: alpha-beta pruning and depth-limiting.


## Alpha-Beta Pruning
The idea behind alpha-beta pruning is that we can stop evaluating a move as soon as we know that it is worse than a move that we have already evaluated. 

Watch this video to see how alpha-beta pruning works:


Connect 4 with alpha-beta pruning


Test your understanding by answering the following questions:

Pruning allows us to ignore portions of the search tree that make no difference to the final choice, and heuristic evaluation functions allow us to approximate the true utility of a state without doing a complete search. (Russle and Norvig)

## Depth-Limiting
The second way to speed up the minimax algorithmm, or any DFS-based algorithm, is to limit the depth of the search. In other words, we can stop searching after a certain number of moves.

Watch this video to see how depth-limiting works:



Test your understanding by answering the following questions:





A foprmal reperesentation of a game is called a game tree. (Russle and Norvig)

ng elements:
• S0: The initial state, which specifies how the game is set up at the start.
• PLAYER(s): Defines which player has the move in a state.
• ACTIONS(s): Returns the set of legal moves in a state.
• RESULT(s, a): The transition model, which defines the result of a move.
TERMINAL TEST • TERMINAL-TEST(s): A terminal test, which is true when the game is over and false
TERMINAL STATES otherwise. States where the game has ended are called terminal states.
• UTILITY(s, p): A utility function (also called an objective function or payoff function),
defines the final numeric value for a game that ends in terminal state s for a player p. In
chess, the outcome is a win, loss, or draw, with values +1, 0, or 1
2 . Some games have a
wider variety of possible outcomes; the payoffs in backgammon range from 0 to +192.