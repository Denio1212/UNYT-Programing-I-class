#here is the add expense funion/ code section of the expense tracker app
from xml.dom.minidom import NamedNodeMap

from Basic_Features.error_handling import does_file_exist
from Basic_Features.error_handling import valid_date
from Basic_Features.error_handling import valid_amount
from Basic_Features.error_handling import clean_text


# This function adds a new expense to the text file.
# It receives the date, category, amount, and description from the GUI.
def add_expense(file_name, date, category, amount, description):

    does_file_exist(file_name)

    date = clean_text(date)
    category = clean_text(category)
    description = clean_text(description)

    if not valid_date(date):
        return 'Invalid date. Please use the format YYYY-MM-DD.'

    if category == '':
        return 'Category cannot be empty.'

    if not valid_amount(amount):
        return 'Invalid amount. Please enter a positive number.'

    if description == '':
        return 'Description cannot be empty.'

    amount = str(round(float(amount), 2))

    file = open(file_name, 'a')
    file.write(date + ',' + category + ',' + amount + ',' + description + '\n')
    file.close()

    return 'Expense added successfully.'
