Hi everyone, we are Team 42 in COSI 103a Software Entrepreneurship and this is our submission for PA3. Our team is Nina Zhang, Emma Barash, James Wang, and William Messenger. In this transcript, we will be showing the result of running pylint and pytest on our code and demonstrating the functionality of our application.

Our team used pylint to ensure that our code has no errors and complies with Python standards. The following is the result of running pylint on tracker.py:


WM@Williams-MBP pa3 % pylint tracker.py

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)


The following is the result of running pylint on transaction.py:


WM@Williams-MBP pa3 % pylint transaction.py

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)


Our team was able to implement all suggestions from pylint and achieve a 10/10 pylint score for both of our scripts.

In addition, we tested our code using pytest. After constructing tests in the test_transaction.py file, the following was the result of running pytest:


WM@Williams-MBP pa3 % pytest
===================== test session starts ======================
platform darwin -- Python 3.9.6, pytest-7.2.1, pluggy-1.0.0
rootdir: /Users/WM/Documents/COSI103a/TeamAwesome_COSI103/PA3
plugins: anyio-3.6.2
collected 6 items                                              

test_transaction.py ......                               [100%]

====================== 6 passed in 0.05s =======================


Our code passed all tests and proved to have no errors or bugs.

Our application is designed to track, store, and summarize transactions that are inputted by the user. Upon running tracker.py, our application starts up and shows the user a menu of functions. Below this menu is a command line where the user can select which function they would like to use.

The first function is “quit”. In order to quit the app, the user can either type 0 or “quit”.

The next method, “show transactions”, runs a SQL query on a table called “transactions”. The query retrieves all rows in the table and selects the “rowid”, “amount”, “category”, “date”, and “description” columns for each row. Overall, the method retrieves and returns all available transactions in the table as a result set. To use this method to display all existing transactions in the database, the user enters “1” as the command at the “command>” prompt.

The method “add transaction” provides a way to insert new transactions into the transactions table in the database. It takes a dictionary representing a new transaction as input, constructs an INSERT query with the transaction details, and executes the query using the “runQuery” method. These details are values for the “amount”, “category”, “date”, and “description” columns taken from the corresponding values in the item dictionary. The “?” placeholders in the query string represent parameters that will be filled in with the values provided in the second argument of the “runQuery” method call. In order to add transactions to the database, the user must enter “2” followed by the item’s “amount”, “category”, and “description”. The user does not need to enter the date, which is grabbed from an imported python “time” library to create an accurate timestamp for each transaction.

The “delete transaction” method provides a way to remove transactions from the transactions table in the database based on their “rowid”. The method takes a “rowid” as input, constructs a DELETE query for the corresponding row, and executes the query using the runQuery method. To use this the number “3” must be entered into the “command>” prompt in tracker.py, followed by the item number (or “rowid”) that the user wishes to delete from the database. This will delete the corresponding transaction.

The next few functions allow the user to get summaries of the data based on day, month, year, or category. The “summarize transaction by date” allows the user to get a list of all transactions that occurred on a specified day. Type 4 in the command line, followed by the date you want summarized in DD format. The “summarize transaction by month” allows the user to get a summary of all transactions that occurred in a specified month. Type 5 in the command line, followed by the month you want summarized in MM format. The “summarize transaction by year” allows the user to get the summary of all transactions by the year they were done. Type 6 in the command line, followed by the year you want summarized in YYYY format. The “summarize transaction by category” allows the user to get the summary of transactions by the category they’re in. Type 7 in the command line, followed by the category you want summarized. 

The final function “print this menu” will print the usage menu again. To activate this menu, the user can simply type “8”. In addition, any time the user presses enter without typing a command, or enters a command that the program does not recognize, the application will automatically re-print the usage menu and prompt the user for another command. This will continue until the user submits a valid command or quits the application.
