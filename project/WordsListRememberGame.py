from tkinter import *
from tkinter import messagebox
import sqlite3
import datetime
import random

number_of_questions = 6 #количество слов (вопросов) в каждом тесте

def show_words(): #вывод всех слов из базы данных в текстовое поле главного окна
    conn = sqlite3.connect('wordsbase.db')
    cursor = conn.cursor()
    textBox.config(state=NORMAL)
    textBox.delete(1.0, END)
    textBox.tag_config("highlight", background="lightyellow2", font="12", foreground="blue")
    textBox.tag_config("txt", foreground="blue")
    textBox.tag_config("red", foreground="red")
    #слова сортируются по приоритету, затем по дате последнего повтора, затем по количеству ошибок
    for word in cursor.execute("SELECT * FROM words ORDER BY priority, last_repeat, mistakes DESC").fetchall():
        textBox.insert(END, f"Слово: {word[0]} Перевод: {word[1]}\n", ("highlight"))
        textBox.insert(END, "Ошибки: ", ('txt'))
        if word[2] != 0:
            textBox.insert(END, word[2], ("red"))
        else:
            textBox.insert(END, word[2], ("txt"))
        textBox.insert(END, f" Последний повтор:{word[3]} Приоритет:{word[4]} \n",("txt"))
    textBox.config(state=DISABLED)
    conn.commit()
    conn.close()


def changeDB(): #редактирование базы данных слов в новом окне
    global dbframe, entryWord, entryTranslation, entryPriority
    dbwindow = Toplevel()
    dbwindow.geometry('300x210')
    dbframe = Frame(dbwindow)
    dbframe.grid(row=0,column=0)
    labelWord = Label(dbframe , text='Word: ')
    labelWord.grid(row=0,column=0,padx=3)

    entryWord = Entry(dbframe, width=20)
    entryWord.grid(row=0,column=1, padx=3)

    labelTranslation = Label(dbframe, text='Translation: ')
    labelTranslation.grid(row=1, column=0, padx=3)

    entryTranslation = Entry(dbframe, width=20)
    entryTranslation.grid(row=1, column=1, padx=3)

    labelPriority = Label(dbframe, text='Priority:')
    labelPriority.grid(row=2, column=0, padx=3)

    entryPriority = Entry(dbframe, width=20)
    entryPriority.grid(row=2, column=1, padx=3)

    btnAddWord = Button(dbframe, text='Add new word',width=25, command=add_word)
    btnAddWord.grid(row=3,column=1,pady=5)

    btnChangePriority = Button(dbframe, text='Change word priority',width=25, command=change_priority)
    btnChangePriority.grid(row=4,column=1,pady=5)

    btnDelWord = Button(dbframe, text='Delete word',width=25, command=check)
    btnDelWord.grid(row=5,column=1,pady=5)

    btnClose = Button(dbframe, text='Close window',width=25, command=dbwindow.destroy)
    btnClose.grid(row=6,column=1,pady=5)
    

def add_word(): #добавление нового слова в базу данных
    newword = entryWord.get()
    newtrans = entryTranslation.get()
    newpriority = entryPriority.get()
    conn = sqlite3.connect('wordsbase.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO words (word, translation, mistakes, last_repeat, priority) VALUES(?,?,?,?,?)",
                   (newword, newtrans, 0, '00-00-00', newpriority))
    conn.commit()
    conn.close()

def change_priority(): #приоритет слова может быть изменен пользователем, по умолчанию = 2
    changeword = entryWord.get()
    newpriority = entryPriority.get()
    conn = sqlite3.connect('wordsbase.db')
    cursor = conn.cursor()
    sql = "UPDATE words SET priority = ? WHERE word = ?"
    cursor.execute(sql,(newpriority, changeword,) )
    conn.commit()
    conn.close()

def check(): #подтверждение удаления из базы данных
    answer = messagebox.askyesno(title="Подтверждение", message="Удалить данные?")
    if answer == True:
        delete_word()

def delete_word(): #удаление слова из базы данных
    delword = entryWord.get()
    conn = sqlite3.connect('wordsbase.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM words WHERE word = ?',(delword,))
    conn.commit()
    conn.close()



def startNewTest(n): #начало тестирования, аргумент функции n: 1 - тест слово-перевод, 2 - тест перевод-слово 
    global index, right, number_of_questions, questions, wrongAnswers, newframe, newwindow
    index = -1 #итерация по словам
    right = 0 #количество правильных ответов за время теста
    newwindow = Toplevel() #создается новое окно 
    newwindow.geometry('300x120') 
    newframe = Frame(newwindow)
    newframe.grid(row=0,column=0)
    textBox.config(state=NORMAL) #в главном окне очищается текстовое поле, кнопки становятся не активны
    textBox.delete(1.0, END)
    textBox.config(state=DISABLED)
    btnShowWords.config(state="disabled")
    btnTest1.config(state="disabled")
    btnTest2.config(state="disabled")
    btnDB.config(state="disabled")
    questions=[]
    wrongAnswers = [] #слова, на которые будет дан неправильный ответ
    words = words_choice()
    if n == 1:  #тип теста
        test1(words) 
    else:
        test2(words)
    
def words_choice(): #Генерация случайного набора слов для теста, частота выбора зависит от приоритета (задается пользователем), даты последнего повтора слова, количества ошибок
    global conn
    conn = sqlite3.connect("wordsbase.db")
    cursor = conn.cursor()
    sql = """SELECT * FROM words ORDER BY priority, last_repeat, mistakes DESC LIMIT 10"""
    cursor.execute(sql)
    words = cursor.fetchall()
    return random.sample(words, number_of_questions)  

def test1(words): #тест слово-перевод
    for word in words: 
        rand_trans = [x[0] for x in random.sample(words,4)] #генерация случайных ответов для каждого слова
        if word[0] not in rand_trans: #если правильного ответа нет среди случайных, он добавляется, список перемешивается
            rand_trans = rand_trans[:3]+ [word[0]]
            random.shuffle(rand_trans)
        questions.append(Question(word[1], rand_trans, word[0], "word")) 
    nextQuestionWord()
    

def test2(words): #тест перевод-слово
    for word in words:
        rand_trans = [x[1] for x in random.sample(words,4)]
        if word[1] not in rand_trans:
            rand_trans = rand_trans[:3]+ [word[1]]
            random.shuffle(rand_trans)
        questions.append(Question(word[0], rand_trans, word[1], "translation"))
    nextQuestionWord()
    
class Question: #Каждый объект имеет переменные: задаваемое слово, вожможные ответы, правильный ответ, тип теста
    def __init__(self, questionWord, answers, correctAns, testType): 
        self.question = questionWord
        self.answers = answers
        self.correctAns = correctAns
        self.testType = testType

    def check(self, guess): #проверка правильности ответа
        global right, wrongAnswers, conn, newframe
        cursor = conn.cursor()
        if(guess == self.correctAns): #если перевод верный, количество ошибок уменьшается, если их количество больше 0
            label = Label(newframe, text="Right!")
            right += 1
            if self.testType == "word": #если тип теста слово-перевод
                cursor.execute("UPDATE words SET mistakes = mistakes-1 WHERE word = :value AND mistakes>0",{"value": self.correctAns})
                #обновляется дата последнего повтора слова
                cursor.execute("UPDATE words SET last_repeat = :data WHERE word = :value",{"data": datetime.datetime.today().strftime('%Y-%m-%d'), "value": self.correctAns})
            else: #тоже самое, если тип теста перевод-слово
                cursor.execute("UPDATE words SET mistakes = mistakes-1 WHERE translation = :value AND mistakes>0",{"value": self.correctAns})
                cursor.execute("UPDATE words SET last_repeat = :data WHERE translation = :value",{"data": datetime.datetime.today().strftime('%Y-%m-%d'), "value": self.correctAns}) 
        else: #если перевод неверный, количество ошибок увеличивается, дата последнего повтора обновляется
            label = Label(newframe, text="Wrong!")
            wrongAnswers.append([self.question, self.correctAns])
            if self.testType == "word": 
                cursor.execute("UPDATE words SET mistakes = mistakes+1, last_repeat = :data WHERE word = :value",{"data": datetime.datetime.today().strftime('%Y-%m-%d'),"value": self.correctAns})
            else:
                cursor.execute("UPDATE words SET mistakes = mistakes+1, last_repeat = :data WHERE translation = :value",{"data": datetime.datetime.today().strftime('%Y-%m-%d'),"value": self.correctAns})
        conn.commit()
        label.grid(row=4,column=0,columnspan=2) #выводится правильный или неправильный текущий ответ
        nextQuestionWord()

    def getButtons(self, newframe): #кнопки выбора ответа
        lbl = Label(newframe, text="Choose the right answer:", width='20').grid(row=0,column=0, columnspan=2)
        lbl = Label(newframe, text=self.question, width='20').grid(row=1,column=0, columnspan=2)
        btn1 = Button(newframe, text=self.answers[0], bg="azure3", width='20', command=lambda: self.check(self.answers[0])).grid(row=2,column=0)
        btn2 = Button(newframe, text=self.answers[1], bg="azure3", width='20', command=lambda: self.check(self.answers[1])).grid(row=3,column=0)
        btn3 = Button(newframe, text=self.answers[2], bg="azure3", width='20', command=lambda: self.check(self.answers[2])).grid(row=2,column=1)
        btn4 = Button(newframe, text=self.answers[3], bg="azure3", width='20', command=lambda: self.check(self.answers[3])).grid(row=3,column=1)


def nextQuestionWord(): #следующее задаваемое слово
    global questions, newwindow, index, right, number_of_questions, wrongAnswers
    if(number_of_questions == index + 1): #если вопрос последний, окно закрывается, выводится количество правильных ответов
        newwindow.destroy()
        btnShowWords.config(state="normal")
        btnTest1.config(state="normal")
        btnTest2.config(state="normal")
        btnDB.config(state="normal")
        textBox.config(state=NORMAL)
        textBox.tag_config("highlight", background="lightyellow2", font="12", foreground="blue")
        textBox.tag_config("highlight2", background="lightyellow3", font="13", foreground="blue")
        textBox.insert(END, f"{right} of {number_of_questions} questions answered right.\n", ("highlight")) #выводится количество правильных ответов за тест
        if len(wrongAnswers)> 0: #если есть неправильные ответы, они выводятся в текстовое поле
            textBox.insert(END, "Wrong answers:\n",("highlight2"))
            for i in range(len(wrongAnswers)):
                textBox.insert(END, f"Word: {wrongAnswers[i][1]}\n", ("highlight"))
                textBox.insert(END, f"Correct answer: {wrongAnswers[i][0]}\n", ("highlight2"))
        textBox.config(state=DISABLED)
        return
    index += 1
    questions[index].getButtons(newframe)


window = Tk()
window.title('Word List Memory Game')
window.config(bg="MediumPurple1")
window.resizable(False, False)
frameMenu = Frame(window)

btnShowWords = Button(frameMenu, text='Show words', font="16",width=30, command=show_words)
btnShowWords.grid(row=1,column=1, pady=5)

btnTest1 = Button(frameMenu, text="Start test word - translation", font="16", width=30, command=lambda: startNewTest(1))
btnTest1.grid(row=2,column=1, pady=5)

btnTest2 = Button(frameMenu, text="Start test translation - word", font="16", width=30, command=lambda: startNewTest(2))
btnTest2.grid(row=3,column=1, pady=5)

btnDB = Button(frameMenu, text="Edit words", font="16", width=30, command=changeDB)
btnDB.grid(row=4,column=1, pady=5)

btnExit = Button(frameMenu, text='Exit', font="16", width=30, command=window.destroy)
btnExit.grid(row=5,column=1, pady=5)

frameMenu.grid(row=0,column=0)

scrollBar = Scrollbar(window, orient=VERTICAL)
scrollBar.grid(row=0,column=2, sticky='ns')

textBox = Text(window, yscrollcommand=scrollBar.set, width=40, height=20, wrap=WORD, state=DISABLED)
textBox.grid(row=0,column=1, padx=10, pady=10)

scrollBar.config(command=textBox.yview)

window.mainloop()
