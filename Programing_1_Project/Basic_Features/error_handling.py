#here is the add expense funion/ code section of the expense tracker app

CATEGORIES = 'Date,Category,Amount,Description\n'


# This function checks if the expense file exists.
# If the file does not exist, it creates it with the correct categories.
def does_file_exist(file_name):

    try:
        file = open(file_name, 'r')
        file.close()

    except FileNotFoundError:
        file = open(file_name, 'w')
        file.write(CATEGORIES)
        file.close()


# This function checks if the date is in the format YYYY-MM-DD.
# Example of a correct date: 2025-03-20
def valid_date(date):

    if len(date) != 10:
        return False

    if date[4] != '-' or date[7] != '-':
        return False

    year = date[0:4]
    month = date[5:7]
    day = date[8:10]

    if not year.isdigit() or not month.isdigit() or not day.isdigit():
        return False

    month = int(month)
    day = int(day)

    if month < 1 or month > 12:
        return False

    if day < 1 or day > 31:
        return False

    return True


# This function checks if the amount is a valid positive number.
def valid_amount(amount):

    try:
        amount = float(amount)

        if amount <= 0:
            return False

        return True

    except ValueError:
        return False


# This function removes extra spaces from text.
# It also removes commas because commas are used to separate data in the text file.
def clean_text(text):

    text = text.strip()
    text = text.replace(',', ' ')

    return text


# This function reads all expenses from the text file.
# It returns the expenses as a list of dictionaries.
def read_expenses(file_name):

    does_file_exist(file_name)

    expenses = []

    file = open(file_name, 'r')
    lines = file.readlines()
    file.close()

    for i in range(len(lines)):

        line = lines[i].strip()

        if line == '':
            continue

        if i == 0:
            continue

        parts = line.split(',')

        if len(parts) >= 4:

            expense = {
                'Date': parts[0],
                'Category': parts[1],
                'Amount': parts[2],
                'Description': parts[3]
            }

            expenses.append(expense)

    return expenses


# This function writes all expenses back into the text file.
# It is mainly used after updating or deleting an expense.
def write_expenses(file_name, expenses):

    file = open(file_name, 'w')
    file.write(CATEGORIES)

    for expense in expenses:

        line = expense['Date'] + ',' + expense['Category'] + ',' + expense['Amount'] + ',' + expense['Description'] + '\n'

        file.write(line)

    file.close()


# This function converts one expense into readable text.
# This is useful for displaying expenses in the GUI.
def expense_to_text(number, expense):

    text = ''
    text += 'Expense Number: ' + str(number) + '\n'
    text += 'Date: ' + expense['Date'] + '\n'
    text += 'Category: ' + expense['Category'] + '\n'
    text += 'Amount: ' + expense['Amount'] + '\n'
    text += 'Description: ' + expense['Description'] + '\n'

    return text


# This function formats a list of expenses into one large text output.
# It is used by the view and search functions.
def format_expense_list(expenses):

    if len(expenses) == 0:
        return 'No expenses found.'

    output = ''

    for i in range(len(expenses)):

        output += expense_to_text(i + 1, expenses[i])
        output += '------------------------------\n'

    return output
