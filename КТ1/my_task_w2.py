import tkinter
import json

def addTask():
    try:
        with open('todolist.json') as file_obj:
            data = json.load(file_obj)
            data.append(f"Задача: {entryTask.get()}, Категория: {entryCategory.get()}, Время: {entryTime.get()}\n")  
    except FileNotFoundError:
        data = [f"Задача: {entryTask.get()}, Категория: {entryCategory.get()}, Время: {entryTime.get()}\n"]
    with open('todolist.json','w') as file_obj:
        json.dump(data, file_obj)

def showTasks():
    try:
        with open('todolist.json') as file_obj:
            data = json.load(file_obj)
            data = ''.join(data).strip()
            tasks.insert(END, data)
    except FileNotFoundError:
        tasks.insert(1.0,"Нет задач")
    tasks.config(state=DISABLED)


window = tkinter.Tk(className = "Менеджер задач")
frame = tkinter.Frame(window)
frame.pack()

lblTask = tkinter.Label(frame,text = "Задача:")
lblTask.grid(row=0,column=0)
entryTask = tkinter.Entry(frame)
entryTask.grid(row=0,column=1)

lblCategory = tkinter.Label(frame,text = "Категория:")
lblCategory.grid(row=1,column=0)
entryCategory = tkinter.Entry(frame)
entryCategory.grid(row=1,column=1)

lblTime = tkinter.Label(frame,text="Время:")
lblTime.grid(row=2,column=0)
entryTime = tkinter.Entry(frame)
entryTime.grid(row=2,column=1)

tasks = tkinter.Text(frame, height=10, width=60)
tasks.grid(row=0,column=3, rowspan=6, padx=10, pady=10)

btnAdd = tkinter.Button(frame, text = "Добавить", command = addTask)
btnAdd.grid(row=3, column=0, columnspan=2)
btnShow = tkinter.Button(frame, text = "Список задач", command = showTasks)
btnShow.grid(row=4,column=0,columnspan=2)
btnExit = tkinter.Button(frame, text = "Выход", command = window.destroy)
btnExit.grid(row=5,column=0,columnspan=2)

window.mainloop()