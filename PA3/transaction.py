import sqlite3
class Transaction: 

    def __init__(self, filename): 
        self.connect = sqlite3.connect(filename)
        self.connect.commit()
