import sqlite3 
import os

def toDict(t):
    ''' t is a tuple (rowid,title, desc,completed)'''
    print('t='+str(t))
    todo = {'rowid':t[0], 'title':t[1], 'desc':t[2], 'completed':t[3]}
    return todo

class Transaction(): 

    def __init__(self): 
        self.runQuery('''CREATE TABLE IF NOT EXISTS transactions 
        (item_num int, amount int, category text, date text, description text)''',())

    def add(self,item):
        ''' create a todo item and add it to the todo table '''
        return self.runQuery("INSERT INTO transactions VALUES(?,?,?,?,?)",(item['item_num'],item['amount'],item['category'],item['date'],item['description']))

    def runQuery(self,query,tuple):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        con= sqlite3.connect(os.getenv('HOME')+'/transaction.db')
        cur = con.cursor() 
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [toDict(t) for t in tuples]


