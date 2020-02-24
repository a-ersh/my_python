def cinema_price (movie, date, time, tickets):
    if movie == "Паразиты" :
        if time == "12":
            result = 250 * tickets;
        elif time == "16":
            result = 350 * tickets;
        elif time == "20":
            result = 450 * tickets;
        else:
            result = "Ошибка ввода"
    elif movie == "1917":
        if time == "10":
            result = 250 * tickets;
        elif time == "13":
            result = 350 * tickets;
        elif time == "16":
            result = 350 * tickets;
        else:
            result = "Ошибка ввода"
    elif movie == "Соник в кино":
        if time == "10":
            result = 350 * tickets;
        elif time == "14":
            result = 450 * tickets;
        elif time == "18":
            result = 450 * tickets;
        else:
            result = "Ошибка ввода"
    else: result = "Ошибка ввода"
    if result != "Ошибка ввода":
        if date == "завтра":
            result = result * 0.95
        elif date != "сегодня":
            result = "Ошибка ввода"
    if result != "Ошибка ввода":
        if tickets >= 20:
            result = result * 0.8
    print("Выбрали фильм:", movie, "День:", date, "Время:", time, "Количество билетов:", tickets)
    if result == "Ошибка ввода":
        print (result)
    else:
        print ("Результат:", result, "руб.")

movie1 = input("Выбрать фильм: ")
date1 = input ("Выбрать дату (сегодня, завтра): ")
time1 = input ("Выбрать время: ")
tickets1 = int(input ("Выбрать количество билетов: "))

cinema_price(movie1,date1,time1,tickets1)
