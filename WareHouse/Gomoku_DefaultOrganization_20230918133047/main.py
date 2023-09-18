'''
This is the main file for the Gomoku game.
'''
import tkinter as tk
from game import Game
class GomokuApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gomoku")
        self.geometry("400x400")
        self.game = Game()
        self.canvas = tk.Canvas(self, width=400, height=400, bg="white")
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.on_click)
        self.draw_board()
    def draw_board(self):
        self.canvas.delete("all")
        for row in range(15):
            self.canvas.create_line(0, row * 25, 400, row * 25)
        for col in range(15):
            self.canvas.create_line(col * 25, 0, col * 25, 400)
    def on_click(self, event):
        x = event.x // 25
        y = event.y // 25
        if self.game.is_valid_move(x, y):
            self.game.make_move(x, y)
            self.draw_piece(x, y)
            if self.game.is_winner(x, y):
                self.show_winner()
    def draw_piece(self, x, y):
        color = "black" if self.game.current_player == 1 else "white"
        self.canvas.create_oval(x * 25, y * 25, (x + 1) * 25, (y + 1) * 25, fill=color)
    def show_winner(self):
        winner = "Black" if self.game.current_player == 1 else "White"
        tk.messagebox.showinfo("Game Over", f"{winner} wins!")
        self.reset_game()
    def reset_game(self):
        self.game.reset()
        self.draw_board()
if __name__ == "__main__":
    app = GomokuApp()
    app.mainloop()