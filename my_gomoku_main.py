import tkinter as tk
from Gomoku.GUI import BoardFrame


if __name__ == '__main__':
    window = tk.Tk()
    board = BoardFrame(window)
    board.pack()
    window.mainloop()
