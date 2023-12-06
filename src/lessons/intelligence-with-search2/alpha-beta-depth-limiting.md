# Alpha-Beta and Depth-Limiting

As we saw in our previous lesson, the minimax algorithm is a great way to find the best move in a two-player, zero-sum game. However, it has one major drawback: it is very slow. In fact, it is so slow that it is not practical to use it in most games. In this lesson, we will look at two ways to speed up the minimax algorithm: alpha-beta pruning and depth-limiting.


## Alpha-Beta Pruning
The idea behind alpha-beta pruning is that we can stop evaluating a move as soon as we know that it is worse than a move that we have already evaluated. 

Watch this video to see how alpha-beta pruning works:


Connect 4 with alpha-beta pruning


Test your understanding by answering the following questions:


## Depth-Limiting
The second way to speed up the minimax algorithmm, or any DFS-based algorithm, is to limit the depth of the search. In other words, we can stop searching after a certain number of moves.

Watch this video to see how depth-limiting works:



Test your understanding by answering the following questions:





