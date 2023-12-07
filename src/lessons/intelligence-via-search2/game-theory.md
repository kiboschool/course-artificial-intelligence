# Game Theory
Mathematical game theory, a branch of economics, views any multiagent environment as a game, provided that the impact of each agent on the others is "significant," regardless  of whether the agents are cooperative or competitive. In AI, the most common games are of a rather specialized kind——what game theorists call deterministic, turn-taking, two-player, ZERO-SUM GAMES zero-sum games of perfect information (such as chess). (Russle and Norvig)

In our terminology, this means deterministic, fully observable environments in which two agents act alternately and in which the utility values at the end of the game are always equal and opposite. For example, if one player wins a game of chess, the other player necessarily loses. It is this opposition between the agents’ utility functions that makes the situation adversarial. (Russle and Norvig)


A zero-sum game is (confusingly) defined as one where the total payoff to all players is the same for every instance of the game. Chess is zero-sum because every game has payoff of either 0+1, 1+0 or 1
2 + 12 . “Constant-sum” would have been a better term, but zero-sum is traditional and makes sense if you imagine each player is charged an entry fee of 12 .

## Game Playing




game playing progress
different types of games 
limitations of game search algos 
