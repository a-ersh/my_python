def my_max(num1, num2):
    if num1 >= num2:
        return num1
    else:
        return num2
    
first = float(input("Введите первое число: "))
second = float(input("Введите второе число: "))

print(my_max (first, second))

