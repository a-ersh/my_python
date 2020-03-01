import random

def guess_game():
    s = ['самовар', 'весна', 'лето']
    word = s[random.randint(0,len(s)-1)]
    num = random.randint(0,len(word)-1)
    print(word[:num] + "?" + word[num+1:])
    guess = input("Введите букву: ")
    if guess == word[num]:
        print("Победа!\nСлово: " + word)
    else:
        print("Увы! Попробуйте в другой раз.\nСлово: " + word)
         
guess_game()
