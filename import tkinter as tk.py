import tkinter as tk
from tkinter import messagebox

class sannmoku:
    def __init__(self, master):
        self.master = master
        self.master.title("三目並べ")
        self.canvas = tk.Canvas(master, width=300, height=300, bg="white")
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.click_handler)
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'O'
        self.draw_board()

    def draw_board(self):
        for i in range(1, 3):
            self.canvas.create_line(i * 100, 0, i * 100, 300)
            self.canvas.create_line(0, i * 100, 300, i * 100)

    def click_handler(self, event):
        row = event.y // 100
        col = event.x // 100
        if self.board[row][col] == '':
            self.board[row][col] = self.current_player
            self.draw_move(row, col)
            if self.check_winner(row, col):
                messagebox.showinfo("勝者", f"{self.current_player}の勝ち！")
                self.reset_board()
            elif self.check_draw():
                messagebox.showinfo("引き分け", "引き分けです。")
                self.reset_board()
            else:
                self.current_player = 'X' if self.current_player == 'O' else 'O'

    def draw_move(self, row, col):
        x = col * 100 + 50
        y = row * 100 + 50
        if self.current_player == 'O':
            self.canvas.create_oval(x - 40, y - 40, x + 40, y + 40, outline="blue", width=2)
        else:
            self.canvas.create_line(x - 40, y - 40, x + 40, y + 40, fill="red", width=2)
            self.canvas.create_line(x + 40, y - 40, x - 40, y + 40, fill="red", width=2)

    def check_winner(self, row, col):
        # Check row
        if all(self.board[row][i] == self.current_player for i in range(3)):
            return True
        # Check column
        if all(self.board[i][col] == self.current_player for i in range(3)):
            return True
        # Check diagonals
        if all(self.board[i][i] == self.current_player for i in range(3)) or \
           all(self.board[i][2 - i] == self.current_player for i in range(3)):
            return True
        return False

    def check_draw(self):
        return all(self.board[i][j] != '' for i in range(3) for j in range(3))

    def reset_board(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.canvas.delete("all")
        self.draw_board()
        self.current_player = 'O'

def main():
    root = tk.Tk()
    game = sannmoku(root)
    root.mainloop()

if __name__ == "__main__":
    main()