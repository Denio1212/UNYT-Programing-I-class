"""
Allows the user to set a budget, displaying a warning if they exceed it.
"""
import pandas as pd

def budgeting(file_path, limit):
    df = pd.read_csv(file_path)
    summary = df["Amount"].sum()
    print(f"Your total spending is: ${summary:,.2f}")
    if summary > limit:
        print(f"You have exceeded your budget by {summary - limit:,.2f}. Please revise your spending, after all, money does not grow on trees.")
    else:
        print("You are currently within your budget. Keep up the good work!")
