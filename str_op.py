s = "У лукоморья 123 дуб зеленый 456"
print(s.find('я'))
print(s.count('у'))

if s.isalpha()!= True:
    print(s.upper())
    
print(len(s))
if len(s) > 4:
    print(s.lower())
    
print(s.replace("У","О"))
