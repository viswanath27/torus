from stock_data import StockData
from gui import GUI
if __name__ == "__main__":
    stock_data = StockData()
    gui = GUI(stock_data)
    gui.create_widgets()