'''
This is the main file of the application.
It imports the necessary modules and starts the GUI.
'''
import tkinter as tk
import yfinance as yf
from stock_analysis import get_stock_data, analyze_stock_data
from stock_display import display_stock_data, display_stock_patterns, plot_stock_data
class StockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Apple Stock Data")
        self.symbol_label = tk.Label(root, text="Symbol:")
        self.symbol_label.pack()
        self.symbol_entry = tk.Entry(root)
        self.symbol_entry.pack()
        self.get_data_button = tk.Button(root, text="Get Data", command=self.get_stock_data)
        self.get_data_button.pack()
        self.stock_data_text = tk.Text(root)
        self.stock_data_text.pack()
        self.plot_data_button = tk.Button(root, text="Plot Data", command=self.plot_stock_data)
        self.plot_data_button.pack()
    def get_stock_data(self):
        symbol = self.symbol_entry.get()
        data = get_stock_data(symbol)
        self.stock_data_text.delete(1.0, tk.END)
        self.stock_data_text.insert(tk.END, data)
        patterns = analyze_stock_data(data)
        display_stock_patterns(patterns)
    def plot_stock_data(self):
        symbol = self.symbol_entry.get()
        data = get_stock_data(symbol)
        plot_stock_data(data)
if __name__ == "__main__":
    root = tk.Tk()
    app = StockApp(root)
    root.mainloop()