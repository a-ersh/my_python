def cost_call (code, mins):
    if code == 343:
        rate = 15
    elif code == 381:
        rate = 18
    elif code == 473:
        rate = 13
    elif code == 485:
        rate = 11
    else: rate = "Введите другой код"
    if rate == "Введите другой код":
        print (rate)
    else:
        print ("Стоимость звонка -", rate * mins, "рублей")

cost_call(381, 10)
