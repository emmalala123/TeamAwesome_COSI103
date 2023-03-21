from transaction import Transaction

def tracker(): 

    db = Transaction()
    db.add({'item_num': 1, 'amount': 100, 'category': 'food', 'date': '2019-01-01', 'description': 'groceries'})
    

tracker()