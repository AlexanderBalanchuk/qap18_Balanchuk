# 1 Привести к целому типу - 1.6, 2.99

x = round(1.6)
y = round(2.99)
print(x, y, sep='\n')

# 2 Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'

text = 'www.my_site.com#about'

# 3 Напишите программу, которая добавляет ‘ing’ к слову ‘stroka’

text1 = 'stroka'
text2 = 'ing'
summ = text1 + text2
print(summ)

# 4 В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"

name = 'Ivanou Ivan'
name = name.replace('Ivanou Ivan', 'Ivan Ivanou')
print(name)

# 5 Напишите программу которая удаляет пробел в начале, в конце строки

S = ' Напишите программу которая удаляет пробел в начале, в конце строки '
print(S.lstrip(),S.rstrip())


# 6 Создайте словарь, связав его с переменной school, и наполните его данными которые бы отражали количество учащихся в десяти разных классах (например, 1а, 1б, 2б, 6а, 7в и т.д.).

school = {
    '1A': 23,
    '1B': 25,
    '1C': 30,
    '2A': 12,
    '2C': 26,
    '3A': 23,
    '3B': 25,
    '3C': 30,
    '4A': 12,
    '4C': 26.
}

# 7 Создайте список и извлеките из него списка второй элемент.

lst = [1, 2, 3]
print(lst[1])

# 8 Вывести входит ли строка1 в строку2 (пример: employ и employment )

line = 'employment'
line1 = 'employ'
if line1 in line:
    print(True),
else:
    print(False)

# 9 Вывести нужные символы

x = "My name is Agent Smith"
print(x[1]) #y
print(x[3:16:3]) #nesgt