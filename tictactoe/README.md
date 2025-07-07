# Tic-Tac-Toe
### Purpose of the Project

It is one of my favorite game, tic-tac-toe!
Goal is to write this in Python, also my favorite. Personal goal is to solidify the fundamentals.

### Structure of the Project

Phase 1: Game Board Basics
Goal: Display and update a 3x3 board.

1. Display the board
    - Represent a 3x3 grid using a list or list of lists.
    - Print it neatly to the console.

2. Update the board with a move
    - Ask the user to enter a position (e.g., 1–9 or row & column).
    - Update the board at that position with "X" or "O".

Phase 2: Game Mechanics
Goal: Alternate turns and enforce valid moves.

3. Switch turns between players
    - Use a variable to keep track of the current player ("X" or "O").

4. Reject invalid moves
    - If the cell is already taken, show an error and ask again.

5. End the game after 9 turns
    - If no winner is found after 9 moves, declare a draw.

Phase 3: Win Conditions
Goal: Detect when a player wins.

6. Check rows, columns, and diagonals for a win
    - Write a function check_winner(board) that returns "X", "O", or None.

7. Announce the winner
    - End the game early if there's a winner.
    - Show the final board and who won.

Phase 4: Polishing
Goal: Make the game clean and interactive.

8. Clearer board formatting
    - Make the grid look more like a real board:
    ```
        X | O | X
        ---+---+---
        O | X | O
        ---+---+---
        X |   |  
    ```

9. Play again option
    - After a win or draw, ask if the user wants to play again.

10. Optional: Let user choose who starts first
    - Ask: “Do you want to be X or O?” or “Who plays first?”

Bonus Challenges (For Later)
- Keep a scoreboard for multiple games.
- Add an AI opponent (even a dumb one that picks random moves).

# Variations

Since the goal is to solidify the fundamentals, I am going to implement this game in different ways.
* First variation, is just playing the game on command line. The script is found [here](./game_cmd.py).

* Second variation, is implementing tic-tac-toe using Numpy. The script is found [here](./game_numpy.py).

* Third variation, is implementing the game in Tkinter. A more visual touch to the game. The script is found [here](./game_tkinter.py).
