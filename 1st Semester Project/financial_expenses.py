from expense import Expense
from expensedb import ExpenseDB

expense1 = Expense(title="Groceries", amount=50.75)
expense2 = Expense(title="Rent", amount=1200.00)
expense3 = Expense(title="Internet Bill", amount=60.00)
expense4 = Expense(title="Transportation", amount=25.50)
expense5 = Expense(title="Gym Membership", amount=40.00)

ExpenseDB.add_expense(expense1)
ExpenseDB.add_expense(expense2)
ExpenseDB.add_expense(expense3)
ExpenseDB.add_expense(expense4)
ExpenseDB.add_expense(expense5)

print(ExpenseDB.to_dict())