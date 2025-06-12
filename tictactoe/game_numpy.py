from time import sleep
import random
import numpy as np
'''
Still working on it.

'''
class TicTacToe:
    def __init__(self):
        self.board = None

    def create_board(self):
        '''create a 3x3 board.'''
        self.board = np.zeros((3, 3), dtype=int)
        print(self.board)

    def player_move(self):
        '''
        ask the current player to enter a row/column number and choose a symbol: X or O. 
        Only X and O are allowed input characters.
        mark the place if it is empty. (I guess that it means by being valid.)
        print the board after every move.
        '''
        pass

    def checker(self):
        '''
        check for 3-in-a-row (rows, columns, diagonals)
        check if the board is full
        '''
        pass

if __name__ == "__main__":
    game = TicTacToe()
    game.create_board()
    while True:
        game.player_move()
        game.checker()
