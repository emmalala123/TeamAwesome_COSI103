import sqlite3

class Transaction: 

    def __init__(self, file): 
        self.connect = sqlite3.connect(file)
        self.connect.commit

    #item, amount, category, date, description in an SQL table 