import PySimpleGUI as sg
from functions import get_todos,write_todos

label = sg.Text("Enter a todo")
input_text = sg.InputText(tooltip="write todo ", key="todo")
add_button = sg.Button("Add")
exit_button = sg.Button("Exit")
list_box = sg.Listbox(values=get_todos(),key="todos",
                      enable_events=True,size=(45,10))
edit_button = sg.Button("edit")
window = sg.Window('TODO',
                   layout=[[label], [input_text, add_button,],
                           [list_box, edit_button]],
                   font=('Helvetica', 15))

while True:
    event, values = window.read()
    print(1,event)
    print(2,values)
    match event:
        case "Add":
            todos = get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value=['😃 added'][0])

        case "edit":
            todo1 = values['todos'][0]
            todo2 = values['todo']+"\n"

            todos = get_todos()
            index = todos.index(todo1)
            todos.pop(index)
            todos.insert(index, todo2)
            write_todos(todos)
            window['todos'].update(values=todos)

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:

            break


window.close()

