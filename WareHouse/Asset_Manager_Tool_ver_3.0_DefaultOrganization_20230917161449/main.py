'''
This is the main file that runs the program and handles the GUI.
'''
import tkinter as tk
import requests
from datetime import datetime, ValueError
import json
try:
    import matplotlib.pyplot as plt
except ImportError:
    print("Error: Matplotlib library not found. Please install matplotlib using 'pip install matplotlib'.")
class FundPerformanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fund Performance App")
        self.product_label = tk.Label(root, text="Product Name:")
        self.product_label.pack()
        self.product_entry = tk.Entry(root)
        self.product_entry.pack()
        self.fund_label = tk.Label(root, text="Fund Name:")
        self.fund_label.pack()
        self.fund_entry = tk.Entry(root)
        self.fund_entry.pack()
        self.start_date_label = tk.Label(root, text="Start Date (YYYY-MM-DD):")
        self.start_date_label.pack()
        self.start_date_entry = tk.Entry(root)
        self.start_date_entry.pack()
        self.end_date_label = tk.Label(root, text="End Date (YYYY-MM-DD):")
        self.end_date_label.pack()
        self.end_date_entry = tk.Entry(root)
        self.end_date_entry.pack()
        self.submit_button = tk.Button(root, text="Submit", command=self.get_fund_data)
        self.submit_button.pack()
        self.graph_button = tk.Button(root, text="Show Graph", command=self.show_graph)
        self.graph_button.pack()
        self.status_label = tk.Label(root, text="")
        self.status_label.pack()
        self.fund_data = None
    def get_fund_data(self):
        product_name = self.product_entry.get()
        fund_name = self.fund_entry.get()
        start_date = self.start_date_entry.get()
        end_date = self.end_date_entry.get()
        try:
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            end_date = datetime.strptime(end_date, '%Y-%m-%d')
        except ValueError:
            self.status_label.config(text="Invalid date format. Please enter dates in YYYY-MM-DD format.")
            return
        if start_date > end_date:
            self.status_label.config(text="Start date cannot be greater than end date.")
            return
        url = f"https://bajajallianzlifeonline.co.in/online/portal/logon/getNavHistory.do?productName={product_name}&fundName={fund_name}&startDate={start_date}&endDate={end_date}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                try:
                    self.fund_data = response.json()
                    self.status_label.config(text="Fund data retrieved successfully.")
                except json.JSONDecodeError:
                    self.status_label.config(text="Error parsing fund data.")
            else:
                self.status_label.config(text="Error retrieving fund data.")
        except requests.RequestException:
            self.status_label.config(text="Error retrieving fund data.")
    def show_graph(self):
        if self.fund_data:
            dates = []
            nav_values = []
            for data in self.fund_data:
                date_str = data['date']
                date = datetime.strptime(date_str, '%d-%b-%Y')
                dates.append(date)
                nav_values.append(float(data['nav']))
            plt.plot(dates, nav_values)
            plt.xlabel('Date')
            plt.ylabel('NAV Value')
            plt.title('Fund Performance')
            plt.xticks(rotation=45)
            plt.show()
        else:
            self.status_label.config(text="No fund data available.")
if __name__ == "__main__":
    root = tk.Tk()
    app = FundPerformanceApp(root)
    root.mainloop()