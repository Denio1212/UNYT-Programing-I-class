"""
Basic File to understand GUI interfaces using PySimpleGUI
"""
import PySimpleGUI as psg

psg.set_options(font=("Calibri", 14))
layout = [
    [psg.Text("Welcome to PySimpleGUI, please enter name: "),psg.Input()],
    [psg.Text("Address to:"), psg.Input()],
    [psg.Ok(), psg.Cancel()]
]
window = psg.Window("PySimpleGUI", layout=layout)
while True:
    event, values = window.read()
    if event == psg.WIN_CLOSED or event == "Cancel":
        break
    print(event, values)
window.close()

# Ok GUI is ready to go when we get there