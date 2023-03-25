from transaction import Transaction


def test_add():
    t1 = Transaction()
    (t1.add({'amount': 100, 'category': 'food', 'date': '2019-01-01', 'description': 'groceries'}))
    print("t1", t1.show_all())
    ans1 = {'amount': 100, 'category': 'food', 'date': '2019-01-01', 'description': 'groceries'}
    assert ans1 == t1