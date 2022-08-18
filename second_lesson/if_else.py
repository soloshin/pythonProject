# a = input()
# b = input()
# if a == b:
#     print('Пароль принят')
# else:
#     print('Пароль не принят')


# num = int(input('Число:'))
# if num % 2 == 0:
#     print('Четное')
# else:
#     print('Нечетное')


# num = int(input('Число:'))
# a = num // 1000
# b = (num // 100) % 10
# c = (num // 10) % 10
# d = num % 10
# if a + d == b - c:
#     print('ДА')
# else:
#     print('НЕТ')


# age = int(input())
# if age >= 18:
#     print('Доступ разрешен')
# else:
#     print('Доступ запрещен')


# a = int(input())
# b = int(input())
# c = int(input())
# if b - a == c - b:
#     print('YES')
# else:
#     print('NO')


# a = int(input('Число:'))
# b = int(input('Число:'))
# if a < b:
#     print(a)
# else:
#     print(b)


# a = int(input('Число:'))
# b = int(input('Число:'))
# c = int(input('Число:'))
# d = int(input('Число:'))
# if a > b:
#     b = a
# if c > d:
#     c = d
# if a > c:
#     a = c
# print(a)


# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# if a > b: #Сравниваем a и b. В случае если А больше Б, то выполняем строчку ниже, если А не больше Б, то А и так меньшее число из группы А и Б
#     a = b # А=Б, т.е. перезаписываем значение переменной А меньшим значением Б.
# if c > d: # Тоже самое со следующей группой (СД). Если С больше Д, то С заменяется меньшим значением Д
#     c = d #
# if a > c: #Тут уже идет сравнение меньших значений в группах (АБ и СД). Сравниеваем значения А и С (они либо перезаписанны меньшими значениями в свое групее, либо сами являются меньшим значением). И если А больше С, то переменной А присваивается значение С.
#     a = c #
# print(a)  # Печатаем А, в которое перезаписанно самое маленькое значение.


# age =int(input('Число:'))
# if (age <= 13):
#     print('детство')
# if 14 <= age <= 24:
#     print('молодость')
# if 25 <= age <= 59:
#     print('зрелость')
# if age >= 60:
#     print('старость')


# num1 = int(input('Число:'))
# num2 = int(input('Число:'))
# num3 = int(input('Число:'))
# summa = 0
# if num1 > 0:
#     summa = summa + num1
# if num2 > 0:
#     summa = summa + num2
# if num3 > 0:
#     summa = summa + num3
# print(summa)


# x = int(input('Число:'))
# if x > -1 and x < 17:
#     print('Принадлежит')
# else:
#     print('Не принадлежит')


# x = int(input('Число:'))
# if x <= -3 or x >= 7:
#     print('Принадлежит')
# else:
#     print('Не принадлежит')


# x = int(input('Число:'))
# if -2 >= x > -30 or 7 < x <= 25:
#     print('Принадлежит')
# else:
#     print('Не принадлежит')

# x = int(input('Число:'))
# if -30 < x <= -2 or 7 < x <= 25:
#     print('Принадлежит')
# else:
#     print('Не принадлежит')


# num = int(input('Число:'))
# if (1000 <= num <= 9999) and ((num % 7 == 0) or (num % 17 == 0)):
#     print('YES')
# else:
#     print('NO')


# a = int(input('Число:'))
# b = int(input('Число:'))
# c = int(input('Число:'))
#
# if (a < b + c) and (b < c + a) and (c < a + b):
#     print('YES')
# else:
#     print('NO')


# year = int(input('Число:'))
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print('YES')
# else:
#     print('NO')

# a = int(input('Число:'))
# b = int(input('Число:'))
# c = int(input('Число:'))
# d = int(input('Число:'))
#
# if (a != c and b == d) or (b != d and a == c):
#     print('YES')
# else:
#     print('NO')


# a = int(input('Число:'))
# b = int(input('Число:'))
# c = int(input('Число:'))
# d = int(input('Число:'))
# if (a - 1 <= c <= a + 1) and (b - 1 <= d <= b + 1):
#     print('YES')
# else:
#     print('NO')
