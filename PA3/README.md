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
