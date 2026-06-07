"""
The GUI interface for the Project. Will display an initial welcome message.
Afterwards, it will ask for an input which will determine which function it will use.
If Advanced is typed, it will open another GUI window with the advanced settings.
Functions will be extracted from files as imports.
"""
import os
import datetime
import sys

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
from Advanced_Features.Visualization import visualize_data

# ------- Base GUI ------- #
def GUI(limit=0.0):
    """
    Home of the GUI
    """
    limit_file = "GUI_Interface/budget_limit.txt"
    if os.path.exists(limit_file):
        with open(limit_file, "r") as file:
            try:
                limit = float(file.read().strip())
            except ValueError:
                limit = 0.0
    else:
        with open(limit_file, "w") as file:
            file.write("0.0")
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
            if values["-IN-"].lower() == "Exit".lower():
                print("Goodbye!")
                break
            file_name = "expenses.txt"
            if values["-IN-"] == "1":
                window.close()
                while True:
                    layout_add_expense = [
                        [psg.Text("Enter the category of the expense "), psg.Input(key="category")],
                        [psg.Text("Enter the amount of the expense($): "), psg.Input(key="amount")],
                        [psg.Text("Enter a brief description of the expense:"), psg.Input(key="description")],
                        [psg.Text("Enter the date of the expense (YYYY-MM-DD): "), psg.Input(key="date")],
                        [psg.Exit(), psg.Button("Confirm", bind_return_key=True)]
                    ]
                    add_window = psg.Window("Add Expense", layout_add_expense, finalize=True)
                    event_add, values_add = add_window.read()
                    add_window.close()
                    if event_add == psg.WIN_CLOSED or event_add == "Exit":
                        break
                    elif event_add == "Confirm":
                        try:
                            float(values_add["amount"])
                        except ValueError:
                            psg.popup_error("Invalid amount. Please enter a valid number.")
                            continue
                        add_expense(file_name, values_add["date"], values_add['category'],
                        values_add["amount"], values_add['description'])
                        print("Expense added successfully!")
                        view_expenses(file_name)
                        budgeting(file_name, limit)
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
                    budgeting(file_name, limit)
                    break

            if values["-IN-"] == "3":
                window.close()
                view_expenses(file_name)
                budgeting(file_name, limit)

            if values["-IN-"] == "4":
                window.close()
                search_term_2 = ""
                search_layout = [
                    [psg.Text("Enter the type of search: Supported keywords are 'date', 'category', 'amount_range', 'date_range'."), psg.Input(key="search_type")],
                    [psg.Exit(), psg.Button("Confirm", bind_return_key=True)]
                ]
                search_window = psg.Window("Search Expenses", search_layout, finalize=True)
                event_search, values_search = search_window.read()
                search_type = values_search["search_type"]
                if event_search == psg.WIN_CLOSED or event_search == "Exit":
                    break

                elif event_search == "Confirm":
                    search_window.close()
                    if search_type not in ["date", "category", "amount_range", "date_range"]:
                        raise ValueError("Invalid search type. Please enter date, category, amount_range, or date_range.")
                    elif search_type in ["date_range", "amount_range"]:
                        range_layout = [
                            [psg.Text("Enter the lower bound of the range: "), psg.Input(key="lower_bound")],
                            [psg.Text("Enter the upper bound of the range: "), psg.Input(key="upper_bound")],
                            [psg.Exit(), psg.Button("Confirm", bind_return_key=True)]
                        ]
                        range_window = psg.Window("Search Range", range_layout, finalize=True)
                        event_range, values_range = range_window.read()
                        if event_range == psg.WIN_CLOSED or event_range == "Exit":
                            break
                        if event_range == "Confirm":
                            search_term = values_range["lower_bound"]
                            search_term_2 = values_range["upper_bound"]
                    else:
                        term_layout = [
                            [psg.Text("Enter the search term (e.g if Date was entered, enter the date in YYYY-MM-DD format): "), psg.Input(key="search_term")],
                            [psg.Exit(), psg.Button("Confirm", bind_return_key=True)]
                        ]
                        term_window = psg.Window("Search Term", term_layout, finalize=True)
                        event_term, values_term = term_window.read()
                        if event_term == psg.WIN_CLOSED or event_term == "Exit":
                            break
                        if event_term == "Confirm":
                            search_term = values_term["search_term"]
                search_expenses(file_name, search_type, search_term, search_term_2)
                break

            if values["-IN-"] == "5":
                window.close()
                view_expenses(file_name)
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
                update_expense(file_name, values_update["new_expense"], values_update["new_date"], values_update["new_category"], values_update["new_amount"], values_update["new_description"])
                print("Expense updated successfully!")
                view_expenses(file_name)
                budgeting(file_name, limit)
                break

            elif values["-IN-"] == "6":
                window.close()
                layout = [
                    [psg.Text("Welcome to the Advanced Features, the following options are available:")],
                    [psg.Text("-- For Monthly Expense Summary, press 1")],
                    [psg.Text("-- To Sort Expenses, press 2")],
                    [psg.Text("-- For Exporting to JSON/CSV, press 3")],
                    [psg.Text("-- For Graph Visualization, press 4")],
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
                    monthly_expense_summary(file_name)
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
                    if values_sort["asc_desc"].lower() in "Ascending".lower():
                        asc_desc = True
                    elif values_sort["asc_desc"].lower() in "Descending".lower():
                        asc_desc = False
                    else:
                        raise ValueError("Invalid input. Please enter either Ascending or Descending.")
                    if event_sort == psg.WIN_CLOSED or event_sort == "Exit":
                        break
                    if event_sort == "Confirm":
                        sort_expenses(file_name, values_sort["sort_type"], asc_desc)
                        break

                if values_advanced["-IN-"] == "3":
                    window_advanced.close()
                    choice_layout = [
                        [psg.Text("Please select the format you would like to export to: Supported keywords are 'JSON' and 'CSV'."), psg.Input(key="choice")],
                        [psg.Exit(), psg.Button("Confirm", bind_return_key=True)],
                    ]
                    choice_window = psg.Window("Export Format", choice_layout, finalize=True)
                    event_choice, values_choice = choice_window.read()
                    choice = values_choice["choice"]
                    choice_window.close()
                    if choice.lower() in "json":
                        convert_to_json(file_name, "expenses.json")
                        print("JSON file has been created/updated successfully!")
                        break
                    elif choice.lower() in "csv":
                        convert_to_csv(file_name, "expenses.csv")
                        print("CSV file has been created/updated successfully!")
                        break
                    else:
                        raise ValueError("Invalid choice. Please enter JSON or CSV.")

                if values_advanced["-IN-"] == "4":
                    window_advanced.close()
                    visualize_data(file_name)
                    break

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
                        with open(limit_file, "w") as file:
                            file.write(str(limit))
                        budgeting(file_name, limit)
                        print("Your current budget limit is ${0}".format(limit))
                        break

        elif event == psg.WIN_CLOSED or event == "Exit":
            print("Goodbye!")
            break
