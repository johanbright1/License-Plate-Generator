import random
import functions
import FreeSimpleGUI as sg

sg.theme("Dark Green")
label = sg.Text("Plate Generator App", font = ("Arial", 60))
generate_button = sg.Button("Generate", button_color="green", mouseover_colors= "light green", key = "gen", size = [10,2])
display = sg.Text("",font = ('Impact', 50), key = "display")

window = sg.Window("License Plate Generator",
                   layout = [[label], [generate_button], [display]], font = ("Ariel", 20),)
while True:
    event, values = window.read()

    match event:
        case "gen":
            window['display'].update(value=functions.generatePlate())


        case sg.WIN_CLOSED:
            break


window.close()