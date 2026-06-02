#here is the view expenses function/ code section for the expense tracker

from Basic_Features.error_handling import read_expenses
from Basic_Features.error_handling import format_expense_list


# This function reads and displays all expenses from the text file.
# It returns text so the GUI can display it.
def view_expenses(file_name):

    expenses = read_expenses(file_name)

    if len(expenses) == 0:
        return 'No expenses found.'

    output = '--- All Expenses ---\n\n'
    output += format_expense_list(expenses)

    return output
