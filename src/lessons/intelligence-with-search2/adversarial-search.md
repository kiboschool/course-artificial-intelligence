[DRAFT]: # "Lesson is being edited"

# Adversarial Search

So far, the problems we have examined have been single-agent problems. In other words, there is only one agent (such as a car or a player of a 15-puzzle game) attempting to solve the problem, such as finding a path to a goal point or rearranging the tiles to the correct order. However, in many problems, especially games like tic-tac-toe, there are two agents trying to solve the problem, each one acting against the other. In this lesson, we will explore how to address such problems.

## Adversarial Scenarios

In a [pacman](https://en.wikipedia.org/wiki/Pac-Man) game, the pacman agent is trying to eat all the food pellets while avoiding the ghosts. The ghosts are trying to eat the pacman. In a [chess](https://en.wikipedia.org/wiki/Chess) game, the white player is trying to checkmate the black player, while the black player is trying to checkmate the white player. In a [tic-tac-toe](https://en.wikipedia.org/wiki/Tic-tac-toe) game, the two players are trying to get three of their pieces in a row before the other player does. In all of these games, the two agents are trying to solve the same problem, but they are acting against each other. This is called an adversarial search problem. Adversarial search is not just limited to games. It can be applied to any problem where there are two agents trying to solve the same problem, but each one is acting against the other. Examples include automated trading,multi-robot motion planning, and even politics.

### Solving Adversarial Search Problems

Let's dig deeper into how to solve adversarial search problems. Let's start with the tic-tac-toe game.

In a tic-tac-toe game like the one shown below, if you are the X player, what would be your next move and why?

<p align="center">
<img src ="../../images/tic-tac-toe1.png" >
</p>

I bet you choose to place X at position 5. Why? Because it is the move to prevent the O player from winning.

<p align="center">
<img src ="../../images/tic-tac-toe2.png" >
</p>
What about this game? if you are the X player, What would be your next move and why?

<p align="center">
<img src ="../../images/tic-tac-toe3.png" >
</p>
The right move here is to place X at position 1. Why? Because it is the move to make you win.

<p align="center">
<img src ="../../images/tic-tac-toe4.png" >
</p>
We know this because we are humans and we have played this game many times. But how can we teach a computer to play this game? Fortunately, scientists have come up with many strategies to solve it. One of these strategies is called the **minimax** strategy. Let's explore it in the next section.

## Minimax Algorithm

The minimax algorithm is a strategy used in decision making, particularly in game theory and artificial intelligence, for minimizing the possible loss while maximizing the potential gain. It's often applied in two-player games like chess or tic-tac-toe. Here's how it works:

In a game, there are two players. One is the maximizer, who tries to get the highest score possible, while the other is the minimizer, who tries to do the opposite and minimize the score.

In a tic-tac-toe game, the maximizer for example is the player who has the `X` symbol and the minimizer is the player who has the `O` symbol. When `X` makes a move, it tries to **maximize** the score, while `O` tries to **minimize** it.

Considing the 3 possible outcomes of the game, `X` can either win, lose, or draw. If `X` wins, it gets a score of `1`. If `X` loses, it gets a score of `-1`. If the game ends in a draw, both players get a score of `0`. During the game, the minimizer tries to minimize the score of the maximizer.

To illustrate this, let's consider the game shown below.

<p align="center">
<img src ="../../images/tic-tac-toe6.png" width = "350px">
</p>

It is player `O`'s turn to make a move. `O` has two possible moves, either place `O` at position 1 or position 8. The algorithm will look ahead and examine the consequences of each possible move. If `O` places its symbol at position 1, the player `X` will put its symbol at position `8` leading to a game score of `1` . If `O` places its symbol at position 8, the player `X` will put its symbol at position `1` leading to a game score of `0`. Because `O` is a minimizer, it will choose the move that minimizes the score so the minimizer `O` will choose to place O at position 8.

<p align="center">
<img src ="../../images/tic-tac-toe7.png" >
</p>

In an early stage of the game, there are many possible moves. Each move leads to a different game state. Before each move, the algorithm will look ahead and examine the consequences of each possible move. It will assume that the other player is also playing optimally. In other words, it will assume that the other player is also trying to maximize its score. The algorithm will compute the score of each possible move and return the move with the highest score. You might have guessed that the algorithm is recursive. It will keep looking ahead until it reaches a terminal state. In other words, it will keep looking ahead until it reaches a state where one of the players wins or the board is full.

Watch this video to learn more about the minimax algorithm.

<iframe width="100%" height="450" src="https://www.youtube.com/embed/6ELUvkSkCts?si=w2vL7Gk9lUwoJPCm&amp;start=378" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### Minimax Tree Traversal Example

[TBD]

### Minimax Pseudocode

```
function mini_max(state)
    if state is terminal #win or draw
        return utility(state) # 1 , -1 or 0
    if state is maximizer's turn
        max_value = -infinity
        for each child of state
            eval = mini_max(child) # recursive call
            max_value = max(max_value, eval)
        return max_value
    if state is minimizer's turn
        min_value = +infinity
        for each child of state
            eval = mini_max(child) # recursive call
            min_value = min(min_value, eval)
        return min_value
```

### Minimax Implementation

```python
print("Welcome to Tic-Tac-Toe")
print("Here is our playing board:")

# Constants
EMPTY_CELL = ' '
BOARD_SIZE = 3

# The play board
play_board = [[EMPTY_CELL for _ in range(BOARD_SIZE)]
              for _ in range(BOARD_SIZE)]


def evaluate(board):
  # Checking for Rows for X or O victory.
  for row in range(BOARD_SIZE):
    if board[row][0] == board[row][1] == board[row][2]:
      if board[row][0] == 'O':
        return 1
      elif board[row][0] == 'X':
        return -1

  # Checking for Columns for X or O victory.
  for col in range(BOARD_SIZE):
    if board[0][col] == board[1][col] == board[2][col]:
      if board[0][col] == 'O':
        return 1
      elif board[0][col] == 'X':
        return -1

  # Checking for Diagonals for X or O victory.
  if board[0][0] == board[1][1] == board[2][2]:
    if board[0][0] == 'O':
      return 1
    elif board[0][0] == 'X':
      return -1

  if board[0][2] == board[1][1] == board[2][0]:
    if board[0][2] == 'O':
      return 1
    elif board[0][2] == 'X':
      return -1

  # Else if none of them have won then return 0
  return 0


def minimax(board, depth, is_maximizing):
  score = evaluate(board)

  if score == 1:  # AI wins
    return score
  if score == -1:  # Player wins
    return score
  if is_board_full():  # Tie
    return 0

  if is_maximizing:
    best = -1000
    for i in range(BOARD_SIZE):
      for j in range(BOARD_SIZE):
        if board[i][j] == EMPTY_CELL:
          board[i][j] = 'O'  # Assuming AI is 'O'
          best = max(best, minimax(board, depth + 1, not is_maximizing))
          board[i][j] = EMPTY_CELL
    return best
  else:
    best = 1000
    for i in range(BOARD_SIZE):
      for j in range(BOARD_SIZE):
        if board[i][j] == EMPTY_CELL:
          board[i][j] = 'X'  # Assuming human is 'X'
          best = min(best, minimax(board, depth + 1, not is_maximizing))
          board[i][j] = EMPTY_CELL
    return best


def find_best_move(board):
  best_val = -1000
  best_move = (-1, -1)

  for i in range(BOARD_SIZE):
    for j in range(BOARD_SIZE):
      if board[i][j] == EMPTY_CELL:
        board[i][j] = 'O'  # AI makes a move
        move_val = minimax(board, 0, False)
        board[i][j] = EMPTY_CELL  # Undo the move

        if move_val > best_val:
          best_move = (i, j)
          best_val = move_val

  return best_move


# Prints the board
def print_board():
  print("   1  2  3")
  for i in range(BOARD_SIZE):
    print(i + 1, end=" ")
    for j in range(BOARD_SIZE):
      print("[" + play_board[i][j] + "]",
            end="")  # print elements without new line
    print()  # print empty line after each row
  print('--------------')


# Check for a win
def check_win():
  for i in range(BOARD_SIZE):
    # Check all rows and columns
    if play_board[i][0] == play_board[i][1] == play_board[i][2] != EMPTY_CELL:
      return play_board[i][0]
    if play_board[0][i] == play_board[1][i] == play_board[2][i] != EMPTY_CELL:
      return play_board[0][i]

  # Check diagonals
  if play_board[0][0] == play_board[1][1] == play_board[2][2] != EMPTY_CELL:
    return play_board[1][1]
  if play_board[2][0] == play_board[1][1] == play_board[0][2] != EMPTY_CELL:
    return play_board[1][1]

  return None


# Check for a full board
def is_board_full():
  return all(EMPTY_CELL not in row for row in play_board)


print_board()


def get_player_input(player):
  while True:
    try:
      position = input(f'{player}, Enter play position (i.e. 1,1): ')
      x, y = map(int, position.split(','))
      if x in range(1, BOARD_SIZE + 1) and y in range(1, BOARD_SIZE + 1):
        return x, y
      else:
        print(
            "Invalid input. Please enter row and column numbers between 1 and 3."
        )
    except ValueError:
      print(
          "Invalid input. Please enter row and column numbers between 1 and 3."
      )


def play(player, row, col, zero_based=True):
  if zero_based:
    if play_board[row][col] == EMPTY_CELL:
      play_board[row][col] = player
      print_board()
      return True
    else:
      print("Position is not empty. Please try again.")
      return False
  else:
    return play(player, row - 1, col - 1, True)


while True:
  # Player X's turn
  while True:
    pos_x, pos_y = get_player_input('X')
    if play('X', pos_x, pos_y, False):  # False for not zero_based
      break

  winner = check_win()
  if winner:
    print(f"{winner} wins")
    break
  if is_board_full():
    print("The game is a tie!")
    break

  # AI (Player O's) turn
  pos_O_x, pos_O_y = find_best_move(play_board)
  play('O', pos_O_x, pos_O_y)  # AI uses zero-based indexing

  winner = check_win()
  if winner:
    print(f"{winner} wins")
    break
  if is_board_full():
    print("The game is a tie!")
    break

```

## More resrouces with Demos

if you feel you don't understand the algorithm yet, here are a few more resources to help you understand it better.

- [Coding Unbeatable Tic Tac Toe AI in Python](https://www.youtube.com/watch?v=Bk9hlNZc6sE)

  - [Code](https://github.com/AlejoG10/python-tictactoe-ai-yt)

- [Tic Tac Toe AI with Minimax Algorithm](https://youtu.be/trKjYdBASyQ?si=Bi4jLj00dSC9J9PE&t=109)
- [MIT Search Lecture 6: Adversarial Search](https://www.youtube.com/watch?v=STjW3eH0Cik)

## Test Your Understanding

- What is an adversarial search problem? How is it different from a single-agent search problem?
- [TBD]
