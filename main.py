# name = 'John Snow'
# age = '29'
# print(name, age, sep='\n')

# plan = '''Самолёт (устар. аэроплан) — класс воздушных судов тяжелее воздуха, предназначенных
# для полётов в атмосфере с помощью силового агрегата, создающего тягу и
# \неподвижного относительно других частей аппарата крыла, создающего подъёмную силу[4][5].
# Неподвижное крыло отличает самолёт от махолёта (орнитоптера) и вертолёта, а наличие
# двигателя — от планёра и мускулолёта. От дирижабля и аэростата самолёт отличается тем,
# что использует аэродинамический, а не аэростатический способ создания подъёмной силы.'''
#
# print(plan[28:33])
# print(plan[0:500:3])
#
# lst_mix = (1,2,3,4)

# anton = ["123", 1, None]
# print(anton[1])

# dct = [
#     {'name': 'bananas', 'weight':'10kg', 'date':'01.01.2024'},
#     {'name': 'strawberry','weight':'5kg', 'date':'21.03.2024'}
#       ]
# dct[0].keys()
# dct[0]['name'] = 'Green Apple'
# dct.append('Red Apple')
# print(dct)

# err = {
#     'length': 'Длина пароля не равна 8 символам',
#     'upper': 'Отсутствуют заглавные буквы',
#     'lower': 'Нет строчных букв в пароле',
#     'digits': 'Нет цифр в пароле',
#     }
#
# password = "Qwerty231!"
#
# if len(password) == 8:
#     print(err['length'])
# if password.isupper():
#     print(err['upper'])
# if password.islower():
#     print(err['lower'])
# if ('1' in password or '2' in password or '3' in password or '4' in password or '5' in password or '6' in password
#         or '7' in password or '8' in password or '9' in password):
#     print(err['digits'])
#
# else:
#     print("PASS")

# lst = [1,7,3,0,9,123,9,6,7,0]
# max = 0
# for i in lst:
#     if i >= max:
#        max = i
# print(max)

#
# lst = [1,7,3,0,9,123,9,6,7,0]
# max = 0
# while i in lst >= max


# for i in range(5, 15, 2):
#     print(i)
# i = 5
# while i <= 15:
#     print(i)
#     i += 2


lst = [1, 7, 3, 0, 9, 123, 9, 6, 7, 0]
max = 0
i = 0
while i < len(lst):
    num = lst[i]
    if num > max:
        max = num
    i += 1
print(max)
