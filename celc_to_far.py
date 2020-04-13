import tkinter
from operator import mul, add 

def celc_to_far():
    '''
    Функция для перевода градусов по шкале Цельсия в градусы по шкале Фаренгейта.
    '''
    try: 
        result.set(add(mul(9/5, float(entry.get())), 32))
    except ValueError:
        result.set("Ошибка ввода")

window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()

label = tkinter.Label(frame, text  = "Температура в Цельсиях")
label.pack()

entry = tkinter.Entry(frame)
entry.pack()

result = tkinter.IntVar()

label = tkinter.Label (frame, textvariable = result).pack()

btnConv = tkinter.Button(frame, text = "Конвертировать", command = celc_to_far).pack()
btnExit = tkinter.Button(frame, text = "Выход", command = window.destroy).pack()

window.mainloop()