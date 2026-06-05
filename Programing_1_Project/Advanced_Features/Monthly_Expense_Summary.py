"""
This file will be used to calculate:
- The monthly expense summary
- The highest expense
"""
import pandas as pd

file_path = "../expenses.txt"
def monthly_expense_summary(file_path):
    """
    calculate the monthly expense summary
    The monthly expense summary is the total number of expenses and the highest expense of the month
    :param file_path: The file path of the expenses.txt file
    :return: The monthly expense summary
    """
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()
    df["Amount"] = pd.to_numeric(df["Amount"])
    total_expenses = df["Amount"].sum()
    highest_spending = df["Amount"].max()
    return print(f"Total Expenses amount to: ${total_expenses:,.2f}"), print(f"The highest spending of the month was: ${highest_spending:,.2f}")
