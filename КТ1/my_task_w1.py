import tkinter
import json

def addTask():
    try:
        with open('todolist.json') as file_obj:
            data = json.load(file_obj)
            data.append({"Задача": {entryTask.get()}, "Категория": {entryCategory.get()}, "Время": {entryTime.get()}})  
    except FileNotFoundError:
        data = [{"Задача": {entryTask.get()}, "Категория": {entryCategory.get()}, "Время": {entryTime.get()}}]
    with open('todolist.json','w') as file_obj:
        json.dump(data, file_obj)

def showTasks():
    try:
        with open('todolist.json') as file_obj:
            data = json.load(f_obj)
        for i in range(len(data)): 
             print('\nЗадача: ', data[i]['name'],'\nКатегория: ', data[i]['category'], '\nДата: ', data[i])
    except FileNotFoundError:
        print("Нет задач")


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

btnAdd = tkinter.Button(frame, text = "Добавить", command = addTask)
btnAdd.grid(row=3, column=0, columnspan=2)
btnShow = tkinter.Button(frame, text = "Список задач", command = showTasks)
btnShow.grid(row=4,column=0,columnspan=2)
btnExit = tkinter.Button(frame, text = "Выход", command = window.destroy)
btnExit.grid(row=5,column=0,columnspan=2)

window.mainloop()