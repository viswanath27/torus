'''
This file contains the GUI class which handles displaying the stock data and patterns.
'''
import tkinter as tk
class GUI(tk.Tk):
    def __init__(self, stock_data):
        super().__init__()
        self.stock_data = stock_data
        self.create_widgets()
    def create_widgets(self):
        stock_data = self.stock_data.get_stock_data()
        patterns = self.stock_data.analyze_patterns()
        # Create a main frame
        main_frame = tk.Frame(self)
        main_frame.pack()
        # Create a label to display stock data
        stock_label = tk.Label(main_frame, text=str(stock_data))
        stock_label.pack()
        # Create a label to display patterns
        patterns_label = tk.Label(main_frame, text=str(patterns))
        patterns_label.pack()
        # Run the GUI main loop
        self.mainloop()