def function1 (x):
    if x >= -2.4 and x <= 5.7:
        return pow(x, 2)
    else:
        return 4

number = float(input("Введите число: "))
print (function1(number))
