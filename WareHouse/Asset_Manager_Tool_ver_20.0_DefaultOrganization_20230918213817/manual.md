# Flask Application with Apple Stock Data

## Introduction

This Flask application is designed to display Apple stock data using various chart types, including Candlestick chart, Bar chart, Line chart, and Figure chart. The application also includes a default navigation bar with options and a StateStreet logo.

## Installation

To install the required dependencies for this application, please follow the steps below:

1. Make sure you have Python installed on your system. You can download Python from the official website: [Python.org](https://www.python.org/downloads/)

2. Clone the repository or download the source code files from [GitHub](https://github.com/your-repo-link).

3. Open a terminal or command prompt and navigate to the project directory.

4. Create a virtual environment (optional but recommended) by running the following command:

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

6. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

## Usage

To run the Flask application and view the Apple stock data, follow the steps below:

1. Make sure you have activated the virtual environment (if created) as mentioned in the installation steps.

2. In the terminal or command prompt, navigate to the project directory.

3. Run the following command to start the Flask application:

   ```
   python main.py
   ```

4. Open a web browser and visit [http://localhost:5000](http://localhost:5000) to access the application.

5. The home page will display the Apple stock data along with the charts. The navigation bar will have three options: Option 1, Option 2, and Option 3.

6. You can explore the different chart types by clicking on the respective options in the navigation bar.

## Customization

If you want to customize the application, you can modify the following files:

- `main.py`: This file contains the Flask routes and data retrieval logic. You can update the date range or modify the stock data retrieval process.

- `home.html`: This file contains the HTML template for the home page. You can modify the layout, add additional charts, or update the navigation bar options.

- `style.css`: This file contains the CSS styling for the application. You can modify the colors, fonts, or layout as per your requirements.

- `static/images/`: This folder contains the images used in the application. You can replace the existing images with your own or add new images.

- `static/css/style.css`: This file contains additional CSS styling for the application. You can modify it to customize the appearance of the charts or other elements.

## Conclusion

This Flask application provides a simple and interactive way to view Apple stock data using different chart types. You can customize the application as per your requirements and explore other functionalities by extending the existing codebase.

If you have any questions or need further assistance, please feel free to reach out to our support team.