"""
Asks the user if they want to repeat the program. Will be used in the main function.
"""
import PySimpleGUI as psg
from GUI_interface.GUI_Interface import GUI

def repetition():
    """
    Asks the user if they want to run the program again
    """
    repetition_layout = [
        [psg.Text("Do you want to run the program again? (Y/N)"), psg.Input(key="repetition")],
        [psg.Exit(), psg.Button("Confirm", bind_return_key=True)],
    ]
    repetition_window = psg.Window("Another go?", repetition_layout, finalize=True)
    event_repetition, values_repetition = repetition_window.read()
    repetition_window.close()
    if event_repetition == "Confirm":
        if values_repetition["repetition"].lower() in "yes".lower():
            GUI()
            repetition()
        elif values_repetition["repetition"].lower() in "no".lower():
            pass
        else:
            psg.popup_error("Invalid input. Please enter either 'Yes' or 'No' (Y/N).")
            repetition()