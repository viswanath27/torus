# Flask Application with Stock Data Visualization

## Introduction

This manual provides a detailed guide on how to use the Flask application developed by ChatDev. The application allows users to visualize the stock data for the Apple organization using various chart types, including Candlestick chart, bar chart, line chart, and figure chart. The application also includes a default navigation bar with options and the StateStreet logo.

## Installation

To use the Flask application, follow these steps:

1. Ensure that you have Python installed on your system. If not, download and install Python from the official website (https://www.python.org).

2. Clone the repository containing the Flask application code:

   ```
   git clone <repository_url>
   ```

3. Navigate to the project directory:

   ```
   cd <project_directory>
   ```

4. Create a virtual environment to isolate the application's dependencies:

   ```
   python -m venv venv
   ```

5. Activate the virtual environment:

   - For Windows:

     ```
     venv\Scripts\activate
     ```

   - For macOS/Linux:

     ```
     source venv/bin/activate
     ```

6. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Usage

To run the Flask application, follow these steps:

1. Ensure that you are in the project directory and the virtual environment is activated.

2. Start the Flask development server:

   ```
   python main.py
   ```

3. Open a web browser and navigate to `http://localhost:5000`.

4. You will see the home page of the Flask application, which displays the Apple stock data and various chart types.

5. Use the navigation bar options to explore different sections of the application.

## Customization

To customize the Flask application, you can modify the following files:

- `main.py`: This file contains the Flask routes and logic. You can add additional routes or modify the existing ones to suit your needs.

- `home.html`: This file contains the HTML template for the home page. You can modify the structure and content of this file to customize the appearance of the application.

- `style.css`: This file contains the CSS styling for the application. You can add your advanced CSS styling here to customize the visual appearance.

- `charts.js`: This file contains the JavaScript code for rendering charts using a charting library. You can add your charting logic here to customize the chart types and data visualization.

## Conclusion

Congratulations! You have successfully installed and used the Flask application developed by ChatDev. You can now visualize the stock data for the Apple organization using various chart types. Feel free to customize the application according to your requirements and explore different functionalities. If you have any questions or need further assistance, please reach out to our support team.