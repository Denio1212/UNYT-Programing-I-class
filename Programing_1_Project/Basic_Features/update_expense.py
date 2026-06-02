#here is the update expenses function/ code section for the expense tracker app

from Basic_Features.error_handling import read_expenses
from Basic_Features.error_handling import write_expenses
from Basic_Features.error_handling import valid_date
from Basic_Features.error_handling import valid_amount
from Basic_Features.error_handling import clean_text


# This function updates an existing expense.
# The expense is selected by its expense number.
def update_expense(file_name, expense_number, new_date, new_category, new_amount, new_description):

    expenses = read_expenses(file_name)

    if len(expenses) == 0:
        return 'No expenses found.'

    expense_number = str(expense_number)

    if not expense_number.isdigit():
        return 'Invalid expense number.'

    expense_number = int(expense_number)

    if expense_number < 1 or expense_number > len(expenses):
        return 'Expense number does not exist.'

    new_date = clean_text(new_date)
    new_category = clean_text(new_category)
    new_amount = clean_text(new_amount)
    new_description = clean_text(new_description)

    if not valid_date(new_date):
        return 'Invalid date. Please use YYYY-MM-DD.'

    if new_category == '':
        return 'Category cannot be empty.'

    if not valid_amount(new_amount):
        return 'Invalid amount. Please enter a positive number.'

    if new_description == '':
        return 'Description cannot be empty.'

    index = expense_number - 1

    expenses[index]['Date'] = new_date
    expenses[index]['Category'] = new_category
    expenses[index]['Amount'] = str(round(float(new_amount), 2))
    expenses[index]['Description'] = new_description

    write_expenses(file_name, expenses)

    return 'Expense updated successfully.'
