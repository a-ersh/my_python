elem = int(input("Введите номер элемента: "))

def periodic_table (num_el):
    if num_el == 3:
        return "Li"
    elif num_el == 25:
        return "Mn"
    elif num_el == 80:
        return "Hg"
    elif num_el == 17:
        return "Cl"
    else:
        return "Введите другой номер"

print (periodic_table (elem))
