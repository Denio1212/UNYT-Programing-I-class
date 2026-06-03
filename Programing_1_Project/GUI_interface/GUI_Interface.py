"""
The GUI interface for the Project. Will display initial welcome message.
Afterwards it will ask for an input which will determine which function it will use.
If Advanced is typed, it will open another GUI window with the advanced settings.
Functions will be extracted from files as imports. (WIP)
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

# ------- Base GUI ------- #
def GUI():
    """
    Home of the GUI
    """
    layout = [
        [psg.Text("Welcome to the Project GUI, the following options are available:")],
        [psg.Text("-- To add an expense, type: 1")],
        [psg.Text("-- To delete an expense, type: 2")],
        [psg.Text("- WIP")],
        [psg.Text("- WIP")],
        [psg.Text("- WIP")],
        [psg.Text("- WIP")],
        [psg.Text("-- For Advanced Features, type: 7")],
        [psg.Text("Your Input: "), psg.Input(key="-IN-")],
        [psg.Exit(), psg.Button("Confirm")],
    ]
    window = psg.Window("Project GUI", layout)

    while True:
        event, values = window.read()
        if event == "Confirm":
            file_name = "../expenses.txt"
            if values["-IN-"] == "1":
                window.close()
                date = datetime.datetime.now().strftime("%Y-%m-%d")
                category = input("Enter the category of the expense (e. g. Food, Transport): ")
                try:
                    expense_amount = int(input("Enter the amount of the expense($): "))
                    if expense_amount < 0:
                        raise ValueError("Amount must be a positive number.")
                except ValueError:
                    raise ValueError("The expense must be a positive number.")
                description = input("Enter a brief description of the expense: ")
                add_expense(file_name, date, category, expense_amount, description)
                print("Expense added successfully!")
                window.refresh()

            elif values["-IN-"] == "7":
                window.close()
                layout = [
                    [psg.Text("Welcome to the Advanced Features, the following options are available:")],
                    [psg.Text("WIP")],
                    [psg.Text("WIP")],
                    [psg.Text("For Exporting to JSON/CSV, press 3")],
                    [psg.Text("WIP")],
                    [psg.Text("WIP")],
                    [psg.Text("your Input: "), psg.Input(key="-IN-")],
                    [psg.Exit(), psg.Button("Confirm")],
                ]
                window_advanced = psg.Window("Advanced Features", layout)
                event_advanced, values_advanced = window_advanced.read()
                if event_advanced == psg.WIN_CLOSED or event_advanced == "Exit":
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
                        print("Invalid choice. Please enter JSON or CSV.")
                        window_advanced.reappear()
            elif event == psg.WIN_CLOSED or event == "Exit":
                print("Goodbye!")
                break
            else:
                break
GUI()
