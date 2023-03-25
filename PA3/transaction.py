import sqlite3 
import os

def toDict(t):
    ''' t is a tuple (rowid, amount, category, date, description)'''
    todo = {'item_num':t[0], 'amount':t[1], 'category':t[2], 'date':t[3], 'description':t[4]}
    return todo

class Transaction(): 

    def __init__(self): 
        self.runQuery('''CREATE TABLE IF NOT EXISTS transactions 
        (amount int, category text, date text, description text)''',())

    def add(self,item):
        ''' create a todo item and add it to the todo table '''
        return self.runQuery("INSERT INTO transactions VALUES(?,?,?,?)",(item['amount'],item['category'],item['date'],item['description']))

    def show_all(self):
        ''' create a todo item and add it to the todo table '''
        return self.runQuery("SELECT rowid,amount,category,date,description FROM transactions",())
    
    def delete(self,num):
        '''delete a item from the table'''
        return self.runQuery("DELETE FROM transactions WHERE rowid = ?",(num,))
    
    def summarize_by_day(self,day):
        '''summarize the transactions by date'''
        return self.runQuery("SELECT rowid,* FROM transactions WHERE STRFTIME('%d', date) = ?",(day,))
    
    def summarize_by_month(self,month):
        '''summarize the transactions by month'''
        return self.runQuery("SELECT rowid,* FROM transactions WHERE STRFTIME('%m', date) = ?",(month,))
    
    def runQuery(self,query,tuple):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        con= sqlite3.connect('transaction.db')
        cur = con.cursor() 
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [toDict(t) for t in tuples]



