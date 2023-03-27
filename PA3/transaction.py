''' This class represents a database of transactions. It can add, show, and delete
    transactions. It can also summarize transactions by day, month, year, and category.'''

import sqlite3

def to_dict(transactions):
    ''' t is a tuple (rowid, amount, category, date, description)'''
    t_dict = {'item_num':transactions[0], 'amount':transactions[1],
            'category':transactions[2], 'date':transactions[3], 'description':transactions[4]}
    return t_dict

class Transaction():
    ''' class to manage the transaction table'''
    def __init__(self, db_name = 'transaction.db'):
        ''' initialize the database'''
        self.db_name = db_name
        self.run_query('''CREATE TABLE IF NOT EXISTS transactions
        (amount int, category text, date text, description text)''',())

    def add(self,item):
        ''' create a todo item and add it to the todo table '''
        return self.run_query("INSERT INTO transactions VALUES(?,?,?,?)",(item['amount'],
                            item['category'],item['date'],item['description']))

    def show_all(self):
        ''' create a todo item and add it to the todo table '''
        return self.run_query("SELECT rowid,amount,category,date,description FROM transactions",())

    def delete(self,num):
        '''delete a item from the table'''
        return self.run_query("DELETE FROM transactions WHERE rowid = ?",(num,))

    def summarize_by_day(self,day):
        '''summarize the transactions by date'''
        return self.run_query("SELECT rowid,* FROM transactions WHERE STRFTIME('%d', date) = ?",
                             (day,))

    def summarize_by_month(self,month):
        '''summarize the transactions by month'''
        return self.run_query("SELECT rowid,* FROM transactions WHERE STRFTIME('%m', date) = ?",
                             (month,))

    def summarize_by_year(self,year):
        '''summarize the transactions by year'''
        return self.run_query("SELECT rowid,* FROM transactions WHERE STRFTIME('%Y', date) = ?",
                             (year,))

    def summarize_by_category(self,category):
        '''summarize the transactions by category'''
        return self.run_query("SELECT rowid,* FROM transactions WHERE category = ?", (category,))

    def delete_all(self):
        '''delete all items from the table'''
        return self.run_query("DELETE FROM transactions", ())

    def run_query(self, query, tup):
        ''' run the sql query and return the results as a dictionary.'''
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        cur.execute(query, tup)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [to_dict(t) for t in tuples]
