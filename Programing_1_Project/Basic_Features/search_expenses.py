#here is the search expenses function/ code section for the expense tracker app

from Basic_Features.error_handling import read_expenses
from Basic_Features.error_handling import valid_date
from Basic_Features.error_handling import valid_amount
from Basic_Features.error_handling import clean_text
from Basic_Features.error_handling import format_expense_list


# This function searches expenses by date, category, amount range, or date range.
# The search_type should be: 'date', 'category', 'amount_range', or 'date_range'.
def search_expenses(file_name, search_type, first_value, second_value=''):

    expenses = read_expenses(file_name)

    if len(expenses) == 0:
        return 'No expenses found.'

    search_type = clean_text(search_type)
    first_value = clean_text(first_value)
    second_value = clean_text(second_value)

    found = []

    if search_type == 'date':

        if not valid_date(first_value):
            return 'Invalid date. Please use YYYY-MM-DD.'

        for expense in expenses:
            if expense['Date'] == first_value:
                found.append(expense)

    elif search_type == 'category':

        if first_value == '':
            return 'Category cannot be empty.'

        for expense in expenses:
            if expense['Category'].lower() == first_value.lower():
                found.append(expense)

    elif search_type == 'amount_range':

        if not valid_amount(first_value) or not valid_amount(second_value):
            return 'Invalid amount range.'

        minimum = float(first_value)
        maximum = float(second_value)

        if minimum > maximum:
            return 'Minimum amount cannot be greater than maximum amount.'

        for expense in expenses:

            amount = float(expense['Amount'])

            if amount >= minimum and amount <= maximum:
                found.append(expense)

    elif search_type == 'date_range':

        if not valid_date(first_value) or not valid_date(second_value):
            return 'Invalid date range. Please use YYYY-MM-DD.'

        if first_value > second_value:
            return 'Start date cannot be after end date.'

        for expense in expenses:
            if expense['Date'] >= first_value and expense['Date'] <= second_value:
                found.append(expense)

    else:
        return 'Invalid search type.'

    if len(found) == 0:
        return 'No matching expenses found.'

    output = '--- Search Results ---\n\n'
    output += format_expense_list(found)

    return output
