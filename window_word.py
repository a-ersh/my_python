import tkinter
import random

def checkAns():
    if entry.get().lower() == dic[rndWord.get()]:
        result.set("Угадали!")
        rndWord.set(random.choice(list(dic.keys())))
    else:
        result.set("Не угадали!")

eng = ["advertisiment", "cake", "cushion", "newspaper","purchase", "quality","receipt",]
rus = ["реклама", "торт", "подушка", "газета", "покупка", "качество", "квитанция"]
dic = dict(zip(eng, rus))

window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()

label = tkinter.Label(frame, text = "Случайное слово:").pack()

rndWord = tkinter.StringVar()
rndWord.set(random.choice(list(dic.keys())))

lblWord = tkinter.Label(frame, textvariable = rndWord).pack()

label2 = tkinter.Label(frame, text = "Укажите перевод слова:").pack()

entry = tkinter.Entry(frame)
entry.pack()

result = tkinter.StringVar()
lblResult = tkinter.Label(frame, textvariable = result).pack()

btnAnswer = tkinter.Button(frame, text = "Готово!", command = checkAns).pack()
btnExit = tkinter.Button(frame, text = "Выход", command = window.destroy).pack()

window.mainloop()