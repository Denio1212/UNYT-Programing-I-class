#here is the delete expenses function/ code section of the expense tracker app

from Basic_Features.error_handling import read_expenses
from Basic_Features.error_handling import write_expenses


# This function deletes an expense from the text file.
# The expense is selected by its expense number.
def delete_expense(file_name, expense_number):

    expenses = read_expenses(file_name)

    if len(expenses) == 0:
        return 'No expenses found.'

    expense_number = str(expense_number)

    if not expense_number.isdigit():
        return 'Invalid expense number.'

    expense_number = int(expense_number)

    if expense_number < 1 or expense_number > len(expenses):
        return 'Expense number does not exist.'

    index = expense_number - 1

    deleted_expense = expenses.pop(index)

    write_expenses(file_name, expenses)

    return 'Expense deleted successfully: ' + deleted_expense['Description']
