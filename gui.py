from functions import get_todos
import PySimpleGUI as sq

label = sq.Text("Type in a to-do")
input_box = sq.InputText(tooltip="Enter todo")
add_button = sq.Button("Add")

window = sq.Window('To-Do App', layout=[[label, input_box, add_button]])
window.read()
window.close()