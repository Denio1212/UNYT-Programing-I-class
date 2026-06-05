"""
The GUI interface for the Project. Will display initial welcome message.
Afterwards it will ask for an input which will determine which function it will use.
If Advanced is typed, it will open another GUI window with the advanced settings.
Functions will be extracted from files as imports. (WIP)
"""
import os
import datetime
import sys

from numpy import dtype

current_dir = os.path.dirname(os.path.abspath(__file__))
programing_1_project_dir = os.path.abspath(os.path.join(current_dir, "../"))

sys.path.insert(0, programing_1_project_dir)
sys.path.insert(0, os.path.join(programing_1_project_dir, "Advanced_Features"))

import PySimpleGUI as psg
from Advanced_Features.Export_to_CSV_JSON import convert_to_csv, convert_to_json
import Basic_Features
from Basic_Features.add_expense import add_expense
from Basic_Features.delete_expense import delete_expense
from Basic_Features.view_expenses import view_expenses
from Basic_Features.error_handling import *
from Basic_Features.search_expenses import search_expenses
from Basic_Features.update_expense import update_expense
from Advanced_Features.Monthly_Expense_Summary import monthly_expense_summary
from Advanced_Features.Budgeting_Feature import budgeting
from Advanced_Features.Sorting_Feature import sort_expenses
# ------- Base GUI ------- #
def GUI():
    """
    Home of the GUI
    """
    layout = [
        [psg.Text("Welcome to the Project GUI, the following options are available:")],
        [psg.Text("-- To add an expense, type: 1")],
        [psg.Text("-- To delete an expense, type: 2")],
        [psg.Text("-- To view all current expenses, type: 3")],
        [psg.Text("-- To search for a specific expense, type: 4")],
        [psg.Text("-- To update an expense, type: 5")],
        [psg.Text("-- For Advanced Features, type: 6")],
        [psg.Text("Your Input: "), psg.Input(key="-IN-")],
        [psg.Exit(), psg.Button("Confirm", bind_return_key=True)],
    ]
    window = psg.Window("Project GUI", layout, finalize=True)

    while True:
        event, values = window.read()
        if event == "Confirm":
            file_name = "../expenses.txt"
            limit = 0
            if not limit == 0:
                budgeting(file_name, limit)
            if values["-IN-"] == "1":
                window.disappear()
                layout_add_expense = [
                    [psg.Text("Enter the category of the expense "), psg.Input(key="category")],
                    [psg.Text("Enter the amount of the expense($): "), psg.Input(key="amount")],
                    [psg.Text("Enter a brief description of the expense:"), psg.Input(key="description")],
                    [psg.Text("Enter the date of the expense (YYYY-MM-DD): "), psg.Input(key="date")],
                    [psg.Exit(), psg.Button("Confirm", bind_return_key=True)]
                ]
                add_window = psg.Window("Add Expense", layout_add_expense, finalize=True)
                event_add, values_add = add_window.read()
                if event_add == psg.WIN_CLOSED or event_add == "Exit":
                    break
                if event_add == "Confirm":
                    try:
                        float(values_add["amount"])
                    except ValueError:
                        raise ValueError("Amount must be a number.")
                    add_expense(file_name, values_add["date"], values_add['category'],
                                values_add["amount"], values_add['description'])
                    print("Expense added successfully!")
                    view_expenses(file_name)
                    break

            if values["-IN-"] == "2":
                window.close()
                view_expenses(file_name)
                del_layout = [
                    [psg.Text("Enter the expense number to delete: "), psg.Input(key="del_expense")],
                    [psg.Exit(), psg.Button("Confirm", bind_return_key=True)]
                ]
                del_window = psg.Window("Delete Expense", del_layout, finalize=True)
                event_del, values_del = del_window.read()
                if event_del == psg.WIN_CLOSED or event_del == "Exit":
                    break
                elif event_del == "Confirm":
                    del_expense_number = values_del["del_expense"]
                    if not del_expense_number.isdigit():
                        raise ValueError("Invalid expense number.")
                    del_expense_number = int(del_expense_number)
                    delete_expense(file_name, del_expense_number)
                    print("Expense deleted successfully!")

            if values["-IN-"] == "3":
                window.close()
                view_expenses("../expenses.txt")


            if values["-IN-"] == "4":
                window.close()
                search_term_2 = ''
                search_type = input("Enter the type of search (date, category, amount_range, date_range): ")
                if search_type not in ["date", "category", "amount_range", "date_range"]:
                    raise ValueError("Invalid search type. Please enter date, category, amount_range, or date_range.")
                elif search_type in ["date_range", "amount_range"]:
                    search_term = input("Enter the first search term (The lower bound of the range): ")
                    search_term_2 = input("Enter the second search term (The upper bound of the range): ")
                else:
                    search_term = input("Enter the search term (e.g If date was used as search type, enter the date in YYYY-MM-DD format): ")
                search_expenses("../expenses.txt", search_type, search_term, search_term_2)
                break

            if values["-IN-"] == "5":
                window.close()
                view_expenses("../expenses.txt")
                layout_update = [
                    [psg.Text("Enter expense number to update: "), psg.Input(key="new_expense")],
                    [psg.Text("Enter new date (YYYY-MM-DD): "), psg.Input(key="new_date")],
                    [psg.Text("Enter new category: "), psg.Input(key="new_category")],
                    [psg.Text("Enter new amount: "), psg.Input(key="new_amount")],
                    [psg.Text("Enter new description: "), psg.Input(key="new_description")],
                    [psg.Exit(), psg.Button("Continue", bind_return_key=True)],
                ]
                window_update = psg.Window("Update Expense", layout_update, finalize=True)
                event_update, values_update = window_update.read()
                if event_update == psg.WIN_CLOSED or event_update == "Exit":
                    break
                if not valid_date(values_update["new_date"]):
                    raise ValueError("Invalid date. Please use YYYY-MM-DD.")
                if values_update["new_category"] == '':
                    raise ValueError("Category cannot be empty.")
                if not valid_amount(values_update["new_amount"]):
                    raise ValueError("Invalid amount. Please enter a positive number.")
                if values_update["new_description"] == '':
                    raise ValueError("Description cannot be empty.")
                update_expense("../expenses.txt", values_update["new_expense"], values_update["new_date"], values_update["new_category"], values_update["new_amount"], values_update["new_description"])
                print("Expense updated successfully!")
                view_expenses("../expenses.txt")
                break

            elif values["-IN-"] == "6":
                window.close()
                layout = [
                    [psg.Text("Welcome to the Advanced Features, the following options are available:")],
                    [psg.Text("-- For Monthly Expense Summary, press 1")],
                    [psg.Text("WIP")],
                    [psg.Text("-- For Exporting to JSON/CSV, press 3")],
                    [psg.Text("WIP")],
                    [psg.Text("-- For Budgeting Feature, press 5")],
                    [psg.Text("your Input: "), psg.Input(key="-IN-")],
                    [psg.Exit(), psg.Button("Confirm", bind_return_key=True)],
                ]
                window_advanced = psg.Window("Advanced Features", layout, finalize=True)
                event_advanced, values_advanced = window_advanced.read()
                if event_advanced == psg.WIN_CLOSED or event_advanced == "Exit":
                    break

                if values_advanced["-IN-"] == "1":
                    window_advanced.close()
                    monthly_expense_summary("../expenses.txt")
                    break

                if values_advanced["-IN-"] == "2":
                    window_advanced.close()
                    sort_layout = [
                        [psg.Text("Please enter the type of sort: Supported keywords are 'Date', 'Category' and 'Amount'.\n"), psg.Input(key="sort_type")],
                        [psg.Text("Ascending or Descending? (Defaults to Descending)"), psg.Input(key="asc_desc")],
                        [psg.Exit(), psg.Button("Confirm", bind_return_key=True)],
                    ]
                    sort_window = psg.Window("Sorting Expenses", sort_layout, finalize=True)
                    event_sort, values_sort = sort_window.read()
                    if values_sort["asc_desc"] in "Ascending".lower():
                        asc_desc = True
                    elif values_sort["asc_desc"] in "Descending".lower():
                        asc_desc = False
                    else:
                        raise ValueError("Invalid input. Please enter either Ascending or Descending.")
                    if event_sort == psg.WIN_CLOSED or event_sort == "Exit":
                        break
                    if event_sort == "Confirm":
                        sort_expenses("../expenses.txt", values_sort["sort_type"], asc_desc)
                        break

                if values_advanced["-IN-"] == "3":
                    choice = input("Do you want to export to JSON, CSV or exit?: ")
                    if choice.lower() == "json":
                        convert_to_json("../expenses.txt", "../expenses.json")
                        print("JSON file has been created successfully!")
                        break
                    elif choice.lower() == "csv":
                        convert_to_csv("../expenses.txt", "../expenses.csv")
                        print("CSV file has been created successfully!")
                        break
                    else:
                        raise ValueError("Invalid choice. Please enter JSON or CSV.")

                if values_advanced["-IN-"] == "5":
                    window_advanced.close()
                    budget_layout = [
                        [psg.Text("Please enter the budget limit: "), psg.Input(key="budget_limit")],
                        [psg.Exit(), psg.Button("Confirm", bind_return_key=True)],
                    ]
                    budget_window = psg.Window("Budgeting", budget_layout, finalize=True)
                    event_budget, values_budget = budget_window.read()
                    if event_budget == psg.WIN_CLOSED or event_budget == "Exit":
                        break
                    if event_budget == "Confirm":
                        limit = float(values_budget["budget_limit"])
                        budgeting("../expenses.txt", limit)
                        print("Your current budget limit is ${0}".format(limit))
                        break

        elif event == psg.WIN_CLOSED or event == "Exit":
            print("Goodbye!")
            break


GUI()
