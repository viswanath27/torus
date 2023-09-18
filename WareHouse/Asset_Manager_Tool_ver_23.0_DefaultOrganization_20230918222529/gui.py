'''
This file contains the GUI class for the Fund Performance application.
'''
import tkinter as tk
import requests
import matplotlib.pyplot as plt
from datetime import datetime
from bs4 import BeautifulSoup
class FundPerformanceGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Fund Performance")
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
        self.submit_button = tk.Button(root, text="Submit", command=self.get_fund_performance)
        self.submit_button.pack()
        self.graph_button = tk.Button(root, text="Show Graph", command=self.show_graph)
        self.graph_button.pack()
        self.output_text = tk.Text(root, height=10, width=50)
        self.output_text.pack()
        self.fund_data = None
    def get_fund_performance(self):
        product_name = self.product_entry.get()
        fund_name = self.fund_entry.get()
        start_date = self.start_date_entry.get()
        end_date = self.end_date_entry.get()
        url = f"https://bajajallianzlifeonline.co.in/online/portal/logon/getNavHistory.do?product={product_name}&fund={fund_name}&fromDate={start_date}&toDate={end_date}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        table = soup.find("table", {"class": "table"})
        rows = table.find_all("tr")
        self.fund_data = []
        for row in rows[1:]:
            columns = row.find_all("td")
            date = datetime.strptime(columns[0].text, "%d-%b-%Y")
            nav = float(columns[1].text)
            self.fund_data.append((date, nav))
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, "Fund performance data retrieved successfully.\n")
        for data in self.fund_data:
            self.output_text.insert(tk.END, f"Date: {data[0].strftime('%Y-%m-%d')}, NAV: {data[1]}\n")
    def show_graph(self):
        if self.fund_data is None:
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, "Please retrieve fund performance data first.")
            return
        dates = [data[0] for data in self.fund_data]
        navs = [data[1] for data in self.fund_data]
        plt.plot(dates, navs)
        plt.xlabel("Date")
        plt.ylabel("NAV")
        plt.title("Fund Performance")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()