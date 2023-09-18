# Asset Manager User Manual

## Introduction

The Asset Manager is a web application developed in Python that allows users to manage their assets. This user manual provides detailed instructions on how to install the necessary dependencies and how to use the application.

## Installation

To install the Asset Manager, follow these steps:

1. Make sure you have Python 3.9.7 installed on your system.

2. Clone the repository or download the source code files.

3. Open a terminal or command prompt and navigate to the project directory.

4. Create a virtual environment (optional but recommended) by running the following command:

   ```
   python -m venv env
   ```

5. Activate the virtual environment by running the appropriate command for your operating system:

   - For Windows:

     ```
     env\Scripts\activate
     ```

   - For macOS/Linux:

     ```
     source env/bin/activate
     ```

6. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

## Usage

Once you have installed the Asset Manager, you can use it to manage your assets. The main functions of the application are described below:

### Add Asset

To add a new asset, follow these steps:

1. Open the `main.py` file in a text editor.

2. Locate the `add_asset` function.

3. Inside the function, add the following code to create a new asset:

   ```python
   asset = Asset(name)
   assets.append(asset)
   ```

   Replace `name` with the name of the asset you want to add.

4. Save the `main.py` file.

5. Run the `main.py` file using the following command:

   ```
   python main.py
   ```

6. A dialog box will appear indicating that the asset has been added successfully.

### View Assets

To view all the assets in the list, follow these steps:

1. Open the `main.py` file in a text editor.

2. Locate the `view_assets` function.

3. Save the `main.py` file.

4. Run the `main.py` file using the following command:

   ```
   python main.py
   ```

5. A dialog box will appear displaying the names of all the assets in the list.

## Conclusion

Congratulations! You have successfully installed and learned how to use the Asset Manager web application. You can now manage your assets efficiently using this application. If you have any further questions or need assistance, please refer to the documentation or contact our support team.