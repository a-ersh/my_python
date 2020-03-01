#https://drakonhub.com/ide/doc/a-ersh/2
import random
def randomGame(num):
    randnum = random.randint(1,4)
    if num == randnum:
        print ("Победа")
    elif num > randnum:
        print ("Введенное число больше загаданного")
    else:
        print ("Введенное число меньше загаданного")

num = int(input("Введите число: "))
randomGame(num)
