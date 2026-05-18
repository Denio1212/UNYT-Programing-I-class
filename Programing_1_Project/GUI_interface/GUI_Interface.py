"""
The GUI interface for the Project. Will display initial welcome message.
Afterwards it will ask for an input which will determine which function it will use.
If Advanced is typed, it will open another GUI window with the advanced settings.
Functions will be extracted from files as imports. (WIP)
"""
import PySimpleGUI as psg
import sys
sys.path.insert(0, "../Advanced_Features")
import Export_to_CSV_JSON

# ------- Base GUI ------- #
def welcome():
    """
    Home of the GUI
    """
    layout = [
        [psg.Text("Welcome to the Project GUI, the following options are available:")],
        [psg.Text("- WIP")],
        [psg.Text("- WIP")],
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
        print(event, values)
        if event == psg.WIN_CLOSED or event == "Exit":
            break
        elif event == "Confirm":
            if values["-IN-"] == "7":
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
                while True:
                    event_advanced, values_advanced = window_advanced.read()
                    if event_advanced == psg.WIN_CLOSED or event_advanced == "Exit":
                        break
                    if values_advanced["-IN-"] == "3":
                        psg.popup_error("Under Construction, thank you for your patience.")
                window_advanced.close()

welcome()
