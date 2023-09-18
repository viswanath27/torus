# ChatDev Flask Application User Manual

## Introduction

Welcome to the user manual for the ChatDev Flask Application. This manual will guide you through the installation process, introduce the main functions of the software, and provide instructions on how to use it.

## Installation

To install the ChatDev Flask Application, please follow the steps below:

1. Make sure you have Python installed on your system. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Clone the ChatDev repository from GitHub using the following command:

   ```
   git clone https://github.com/ChatDev/ChatDev-Flask-Application.git
   ```

3. Navigate to the project directory:

   ```
   cd ChatDev-Flask-Application
   ```

4. Create a virtual environment to isolate the project dependencies:

   ```
   python -m venv venv
   ```

5. Activate the virtual environment:

   - For Windows:

     ```
     venv\Scripts\activate
     ```

   - For macOS and Linux:

     ```
     source venv/bin/activate
     ```

6. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

7. Start the Flask application:

   ```
   python main.py
   ```

8. Open your web browser and go to [http://localhost:5000](http://localhost:5000) to access the ChatDev Flask Application.

## Main Functions

The ChatDev Flask Application provides the following main functions:

1. Home Page: The home page of the application displays a welcome message and serves as the starting point for navigation.

2. Fund Performance Report: The fund performance report page displays the performance data for the BajajAlliance Mutual Fund. It includes yearly and monthly performance metrics.

3. Navigation Bar: The navigation bar at the top of the application allows you to switch between the home page and the fund performance report page.

## How to Use

To use the ChatDev Flask Application, follow these steps:

1. Open your web browser and go to [http://localhost:5000](http://localhost:5000).

2. The home page will be displayed by default. You can navigate to the fund performance report page by clicking on the "Fund Performance" option in the navigation bar.

3. On the fund performance report page, you will see the fund name, yearly performance metrics, and monthly performance metrics.

4. To customize the application, you can modify the HTML templates in the `templates` folder and the CSS styling in the `static/css` folder.

## Conclusion

Congratulations! You have successfully installed and learned how to use the ChatDev Flask Application. If you have any further questions or need assistance, please don't hesitate to contact our support team. Enjoy using the application!