import tkinter as tk
from GomokuSample.GUI import BoardFrame


if __name__ == '__main__':
    window = tk.Tk()
    window.wm_title('gomoku')
    gui_board = BoardFrame(window)
    gui_board.pack()
    window.mainloop()

