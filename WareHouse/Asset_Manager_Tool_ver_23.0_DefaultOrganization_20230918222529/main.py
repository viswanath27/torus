'''
This is the main file that runs the GUI application.
'''
import tkinter as tk
from gui import FundPerformanceGUI
if __name__ == "__main__":
    root = tk.Tk()
    app = FundPerformanceGUI(root)
    root.mainloop()