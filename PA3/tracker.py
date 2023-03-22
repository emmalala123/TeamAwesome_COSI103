from transaction import Transaction

def tracker(): 

    db = Transaction()
    (db.add({'amount': 100, 'category': 'food', 'date': '2019-01-01', 'description': 'groceries'}))
    print(db.show_all())

tracker()