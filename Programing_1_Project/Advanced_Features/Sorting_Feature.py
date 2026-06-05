"""
Allows the user to sort expenses by date, ammount and category
"""
import pandas as pd

file_name = ("../expenses.txt")

def sort_expenses(file_name, sort_type, asc_desc = 'False'):
    """
    Sorts expenses by date, amount and category
    :param file_name: The path to expenses.txt file
    :return: The expenses sorted by either date, amount and category
    """
    expenses = pd.read_csv(file_name)
    if sort_type in "Date".lower():
        expense_sort = expenses.sort_values(by=["Date"], ascending=asc_desc)
        return print(expense_sort)

    elif sort_type in "Amount".lower():
        expense_sort = expenses.sort_values(by=["Amount"], ascending=asc_desc)
        return print(expense_sort)

    elif sort_type in "Category".lower():
        expense_sort = expenses.sort_values(by=["Category"])
        return print(expense_sort)

    else:
        raise ValueError("Invalid sort type. Please enter either 'Date', 'Category' or 'Amount'")
