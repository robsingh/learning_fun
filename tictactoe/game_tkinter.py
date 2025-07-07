"""A tic-tac-toe game built with Python and Tkinter."""

import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self, root, board, buttons, current_player, game_over):
        '''
        root -> reference to the Tkinter root window.
        board -> 2D list to store current board state("X", "O", "").
        buttons -> 2D list to store button widgets.
        current_player -> tracks whose turn it is.
        game_over -> boolean flag to prevent clicks after the game.
        '''
        self.root = root
        self.board = board
        self.buttons = buttons
        self.current_player = current_player
        self.game_over = game_over
        self.status_label = tk.Label(text="Player X's turn", font=("Arial", 16))
        self.status_label.grid(row=4, column=0, columnspan=3)

    
    def create_board(self):
        # create a 3X3 button grid, bind them to on_click()
        self.root.title("Tic-Tac-Toe")
        rows = 3
        columns = 3
        for row in range(rows):
            for col in range(columns):
                button = tk.Button(
                    self.root,
                    width=5,
                    height=2,
                    font=("Arial", 24),
                    command=lambda r=row,c=col: self.on_click(r,c)
                )
                # lambda would allow us to send multiple data through the call back function (on_click)
                self.buttons[row][col] = button
                button.grid(row=row, column=col)
        
        reset_button = tk.Button(
            self.root,
            text="Reset Game",
            font=("Arial", 24),
            command=self.reset_game
        )

        reset_button.grid(row=3, column=0, columnspan=3, pady=10)
        
    
    def on_click(self, row, col):
        # Handle a player move when a button is clicked
        if self.board[row][col] == "" and not self.game_over:
            #record the move
            button = self.buttons[row][col]
            button.config(text = self.current_player)
            self.board[row][col] = self.current_player
            player = self.current_player

            if self.check_winner(player):
                messagebox.showinfo("Game Over", f"Player {player} wins!")
                self.game_over = True
            
            elif all(cell != "" for row in self.board for cell in row):
                messagebox.showinfo("Game Over", "It's a draw!")
                self.game_over = True
            
            else:
                #only switch turn if no winner
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.config(text=f"Player {self.current_player}'s turn")


    def check_winner(self, player):
        #check all rows
        for row in self.board:
            if all(cell == player for cell in row):
                return True
    
        #check all columns
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True

        #check diagonals
        if all(self.board[i][i] == player for i in range(3)):
            return True
        
        if all(self.board[i][2-i] == player for i in range(3)):
            return True
    
        return False


    def reset_game(self):
        # reset the game state and UI
        self.board = [[""] * 3 for _ in range(3)]
        self.current_player = "X"
        self.game_over = False
        self.status_label.config(text="Player X's turn")

        for row in range(3):
            for col in range(3):
                button = self.buttons[row][col]
                button.config(text="")
        

def main():
    root = tk.Tk()
    game = TicTacToeGUI(root, board=[[""]*3 for _ in range(3)], buttons=[[None]*3 for _ in range(3)], current_player="X", game_over=False)
    game.create_board()
    root.mainloop()
    # mainloop() is a method that starts the infinite event loop (that waits for events to occur) of the Tkinter application.
    

if __name__ == "__main__":
    main()
