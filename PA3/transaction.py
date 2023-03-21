import sqlite3 
import os

class Transaction(): 

    def __init__(self, filename): 
        self.runQuery('''CREATE TABLE IF NOT EXISTS {filename}
                    (item # int, amount int, category text, date text, description text)''',())
    


