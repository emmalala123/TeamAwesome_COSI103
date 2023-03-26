# test_transactions.py
import sqlite3
import os
from transaction import Transaction

# Test the Transaction class
class TestTransaction:

    @classmethod
    def teardown_class(self):
        self.transaction = Transaction()
        self.transaction.delete_all()

    def setup_method(self):
        # Create a new Transaction instance for each test
        self.transaction = Transaction()

        # must refresh database for tests to be accurate
        self.transaction.delete_all()

    def test_add_transaction(self):
        # Test adding a transaction
        item = {'amount': 100, 'category': 'food', 'date': '2023-03-25', 'description': 'groceries'}
        self.transaction.add(item)
        result = self.transaction.show_all()
        assert result[0]['amount'] == item['amount']
        assert result[0]['amount'] == item['amount']
        assert result[0]['category'] == item['category']
        assert result[0]['date'] == item['date']
        assert result[0]['description'] == item['description']

    def test_delete_transaction(self):
        # Test deleting a transaction
        item = {'amount': 100, 'category': 'food', 'date': '2023-03-25', 'description': 'groceries'}
        self.transaction.add(item)
        result = self.transaction.show_all()
        assert len(result) == 1
        num = result[0]['item_num']
        self.transaction.delete(num)
        result = self.transaction.show_all()
        assert len(result) == 0

    def test_summarize_by_day(self):
        # Test summarizing transactions by day
        item1 = {'amount': 100, 'category': 'food', 'date': '2023-03-25', 'description': 'groceries'}
        item2 = {'amount': 200, 'category': 'clothing', 'date': '2023-03-25', 'description': 'new shirt'}
        self.transaction.add(item1)
        self.transaction.add(item2)
        result = self.transaction.summarize_by_day('25')
        assert len(result) == 2
        assert result[0]['amount'] == item1['amount']
        assert result[1]['amount'] == item2['amount']

    def test_summarize_by_month(self):
        # Test summarizing transactions by month
        item1 = {'amount': 100, 'category': 'food', 'date': '2023-03-25', 'description': 'groceries'}
        item2 = {'amount': 200, 'category': 'clothing', 'date': '2023-03-30', 'description': 'new shirt'}
        self.transaction.add(item1)
        self.transaction.add(item2)
        result = self.transaction.summarize_by_month('03')
        assert len(result) == 2
        assert result[0]['amount'] == item1['amount']
        assert result[1]['amount'] == item2['amount']

    def test_summarize_by_year(self):
        # Test summarizing transactions by year
        item1 = {'amount': 100, 'category': 'food', 'date': '2022-03-25', 'description': 'groceries'}
        item2 = {'amount': 200, 'category': 'clothing', 'date': '2021-03-30', 'description': 'new shirt'}
        item3 = {'amount': 200, 'category': 'food', 'date': '2023-03-25', 'description': 'groceries'}
        item4 = {'amount': 300, 'category': 'clothing', 'date': '2023-03-30', 'description': 'new shirt'}
        self.transaction.add(item1)
        self.transaction.add(item2)
        self.transaction.add(item3)
        self.transaction.add(item4)
        result = self.transaction.summarize_by_year('2023')
        assert len(result) == 2
        assert result[0]['amount'] == item3['amount']
        assert result[1]['amount'] == item4['amount']

    def test_summarize_by_category(self):
        # Test summarizing transactions by category
        item1 = {'amount': 100, 'category': 'food', 'date': '2022-03-25', 'description': 'groceries'}
        item2 = {'amount': 200, 'category': 'clothing', 'date': '2021-03-30', 'description': 'new shirt'}
        item3 = {'amount': 200, 'category': 'food', 'date': '2023-03-25', 'description': 'groceries'}
        item4 = {'amount': 300, 'category': 'clothing', 'date': '2023-03-30', 'description': 'new shirt'}
        self.transaction.add(item1)
        self.transaction.add(item2)
        self.transaction.add(item3)
        self.transaction.add(item4)
        result = self.transaction.summarize_by_category('clothing')
        assert len(result) == 2
        assert result[0]['category'] == item2['category']
        assert result[1]['category'] == item4['category']