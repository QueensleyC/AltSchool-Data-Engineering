from expense import Expense

class ExpenseDB():

    expenses: Expense = []

    @classmethod
    def add_expense(cls, expense):
        cls.expenses.append(expense)

    @classmethod
    def remove_expenses(cls, expense_id):
        cls.expenses = [exp for exp in cls.expenses if exp.id != expense_id]

    @classmethod
    def get_expense_by_id(cls, expense_id):
        return next((exp for exp in cls.expenses if exp.id == expense_id), None)

    @classmethod
    def get_expense_by_title(cls, expense_title):
        return next((exp for exp in cls.expenses if exp.title == expense_title), None)

    @classmethod
    def to_dict(cls):
        return [exp.to_dict() for exp in cls.expenses]

