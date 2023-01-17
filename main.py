import PySimpleGUI as sg

label = sg.Text("Enter a todo")
input_text = sg.InputText(tooltip="write todo ❓")
add_button = sg.Button("ADD")
window = sg.Window('TODO', layout=[[label], [input_text, add_button]])
window.read()
window.close()

print("hello")