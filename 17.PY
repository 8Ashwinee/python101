# chess_game.py

'''class ChessGame:
    def __init__(self):
        self.board = self.create_board()
        self.current_turn = 'white'

    def create_board(self):
        # Create an 8x8 chess board with initial positions
        board = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],  # Black pieces
            ['p'] * 8,  # Black pawns
            ['.'] * 8,  # Empty squares
            ['.'] * 8,
            ['.'] * 8,
            ['.'] * 8,
            ['P'] * 8,  # White pawns
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']   # White pieces
        ]
        return board

    def print_board(self):
        for row in self.board:
            print(' '.join(row))
        print()

    def move_piece(self, start, end):
        start_row, start_col = start
        end_row, end_col = end

        piece = self.board[start_row][start_col]
        if piece == '.':
            print("No piece at the starting position!")
            return False

        if (self.current_turn == 'white' and piece.islower()) or \
           (self.current_turn == 'black' and piece.isupper()):
            print("It's not your turn!")
            return False

        self.board[end_row][end_col] = piece
        self.board[start_row][start_col] = '.'
        self.current_turn = 'black' if self.current_turn == 'white' else 'white'
        return True

    def play(self):
        print("Welcome to Chess!")
        while True:
            self.print_board()
            print(f"{self.current_turn.capitalize()}'s turn")
            try:
                start = tuple(map(int, input("Enter start position (row col): ").split()))
                end = tuple(map(int, input("Enter end position (row col): ").split()))
                if not self.move_piece(start, end):
                    print("Invalid move. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter row and column as numbers between 0 and 7.")

if __name__ == "__main__":
    game = ChessGame()
    game.play()'''

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm

dx, dy = 0.015, 0.05
x = np.arange(-4.0, 4.0, dx)
y = np.arange(-4.0, 4.0, dy)
X, Y = np.meshgrid(x, y)
extent = np.min(x), np.max(x), np.min(y), np.max(y)
z1 = np.add.outer(range(8), range(8)) % 2
plt.imshow(z1, cmap="binary_r", interpolation="nearest", extent=extent, alpha=1)

def chess(x, y):
    return (1 - x / 2 + x ** 5 + y ** 6) * np.exp(-(x ** 2 + y ** 2))
z2 = chess(X, Y)
plt.imshow(z2, alpha=0.7, interpolation="bilinear", extent=extent)
plt.title("Chess Board with Python")
plt.show()