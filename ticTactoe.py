import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.master.geometry("670x450")
        self.master.resizable(False, False)
        title_label = tk.Label(self.master, text="Welcome to Tic Tac Toe", font=("Cambria", 20, "bold"), fg="#990F4B")
        title_label.pack()
        self.canvas = tk.Canvas(self.master, width=300, height=300, bg="#990F4B")
        self.canvas.pack()
        self.symbol = ''
        self.board = [' '] * 9
        self.user_wins = 0
        self.computer_wins = 0
        self.draw_board()

        self.canvas.bind("<Button-1>", self.user_click)

        # Labels to display scores
        self.user_score = tk.Label(self.master, text="User: 0", font=("Cambria", 15, "bold"), fg="#990F4B")
        self.user_score.pack(side=tk.LEFT, padx=50, pady=15)
        self.computer_score = tk.Label(self.master, text="Computer: 0", font=("Cambria", 15, "bold"), fg="#990F4B")
        self.computer_score.pack(side=tk.RIGHT, padx=50, pady=15)

        # Buttons for symbol selection
        self.select_x_button = tk.Button(self.master, text="Select X", command=lambda: self.select_symbol('X'),
                                         font=("Cambria", 15, "bold"), fg="#990F4B")
        self.select_x_button.pack(side=tk.LEFT, padx=35, pady=15)

        self.select_o_button = tk.Button(self.master, text="Select O", command=lambda: self.select_symbol('O'),
                                         font=("Cambria", 15, "bold"), fg="#990F4B")
        self.select_o_button.pack(side=tk.RIGHT, padx=15, pady=15)

    def draw_board(self):
        self.canvas.delete("all")
        cell_size = 100
        for i in range(3):
            for j in range(3):
                x1, y1 = j * cell_size, i * cell_size
                x2, y2 = x1 + cell_size, y1 + cell_size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="white")
                player = self.board[i * 3 + j]
                if player in ['X', 'O']:
                    self.canvas.create_text((x1 + x2) // 2, (y1 + y2) // 2, text=player, font=("Cambria", 40),
                                            fill="white")

    def user_click(self, event):
        if self.symbol == '':
            messagebox.showerror("Error", "Please select your symbol (X or O) first!")
            return
        x, y = event.x // 100, event.y // 100
        if self.board[y * 3 + x] == ' ':
            self.board[y * 3 + x] = self.symbol
            self.draw_board()
            if self.check_winner(self.board, self.symbol):
                self.user_wins += 1
                self.update_scoreboard()
                response = messagebox.askyesno("Game Over",
                                               f"Congratulations! You win with {self.symbol}. Do you want to play again?")
                if response:
                    self.reset_board()
                else:
                    self.master.destroy()
                return
            elif ' ' not in self.board:
                response = messagebox.askyesno("Game Over", "It's a draw! Do you want to play again?")
                if response:
                    self.reset_board()
                else:
                    self.master.destroy()
                return
            self.computer_move()

    def computer_move(self):
        empty_cells = [i for i, cell in enumerate(self.board) if cell == ' ']
        cell = random.choice(empty_cells)
        self.board[cell] = 'O' if self.symbol == 'X' else 'X'
        self.draw_board()
        if self.check_winner(self.board, 'X' if self.symbol == 'O' else 'O'):
            self.computer_wins += 1
            self.update_scoreboard()
            response = messagebox.askyesno("Game Over", "Computer wins! Do you want to play again?")
            if response:
                self.reset_board()
            else:
                self.master.destroy()
            return
        elif ' ' not in self.board:
            response = messagebox.askyesno("Game Over", "It's a tie! Do you want to play again?")
            if response:
                self.reset_board()
            else:
                self.master.destroy()
            return

    def check_winner(self, board, symbol):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in winning_combinations:
            if board[combo[0]] == board[combo[1]] == board[combo[2]] == symbol:
                return True
        return False

    def select_symbol(self, symbol):
        self.symbol = symbol
        if symbol == 'X':
            self.select_x_button.config(state=tk.NORMAL)
            self.select_o_button.config(state=tk.DISABLED)
        elif symbol == 'O':
            self.select_o_button.config(state=tk.NORMAL)
            self.select_x_button.config(state=tk.DISABLED)

    def reset_board(self):
        self.board = [' '] * 9
        self.draw_board()
        self.symbol = ''  # Reset the symbol selection
        self.select_x_button.config(state=tk.NORMAL)
        self.select_o_button.config(state=tk.NORMAL)

    def update_scoreboard(self):
        self.user_score.config(text=f"User: {self.user_wins}")
        self.computer_score.config(text=f"Computer: {self.computer_wins}")

def main():
    root = tk.Tk()
    ttt = TicTacToe(root)
    root.mainloop()

if __name__ == "__main__":
    main()
