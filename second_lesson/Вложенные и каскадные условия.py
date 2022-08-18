# n = int(input('Число:'))
# k = int(input('Число:'))
# if n > k:
#     print('NO')
# elif k > n:
#     print('YES')
# else:
#     print("Don't know")


# a = int(input('Число:'))
# b = int(input('Число:'))
# c = int(input('Число:'))
#
# if a == b ==c:
#     print('Равносторонний')
# elif a == b or a == c or b == c:
#     print('Равнобедренный')
# else:
#     print('Разносторонний')


# a = int(input('Число:'))
# b = int(input('Число:'))
# c = int(input('Число:'))
#
# if b > a > c or c > a > b:
#     print(a)
# elif a > b > c or c > b > a:
#     print(b)
# elif a > c > b or b > c > a:
#     print(c)


# month = int(input('Число:'))
# if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
#     print('31')
# elif month == 4 or month == 6 or month == 9 or month == 11:
#     print('30')
# else:
#     print('28')


# boxer = int(input())
# if boxer < 60:
#     print('Легкий вес')
# elif 60 <= boxer < 64:
#     print('Первый полусредний вес')
# elif 64 <= boxer < 69:
#     print('Полусредний вес')


# num1 = int(input('Число:'))
# num2 = int(input('Число:'))
# operator = input('Оператор:')
#
# if operator == '+':
#     print(num1 + num2)
# elif operator == '-':
#     print(num1 - num2)
# elif operator == '*':
#     print(num1 * num2)
# elif operator == '/':
#     if num2 == 0:
#         print('На ноль делить нельзя!')
#     else:
#         print(num1 / num2)
# else:
#     print('Неверная операция')


# a, b = input(), input()
# if a == b and (a == 'красный' or a == 'желтый' or a == 'синий'):
#     print(a)
# elif (a == 'красный' and b == 'синий') or (b == 'красный' and a == 'синий'):
#     print('фиолетовый')
# elif (a == 'красный' and b == 'желтый') or (b == 'красный' and a == 'желтый'):
#     print('оранжевый')
# elif (a == 'синий' and b == 'желтый') or (b == 'синий' and a == 'желтый'):
#     print('зеленый')
# else:
#     print('ошибка цвета')


# num = int(input('Число:'))
# if num == 0:
#     print('зеленый')
# elif (1 <= num <= 10) or (19 <= num <= 28):
#     if num % 2 == 0:
#         print('черный')
#     else:
#         print('красный')
# elif (11 <= num <= 18) or (29 <= num <= 36):
#     if num % 2 == 0:
#         print('красный')
#     else:
#         print('черный')
# else:
#     print('ошибка ввода')


# a1 = int(input('Число:'))
# b1 = int(input('Число:'))
# a2 = int(input('Число:'))
# b2 = int(input('Число:'))
#
# if b1 < a2 or b2 < a1:
#     print('пустое множество')
# elif b1 == a2:
#     print(b1)
# elif a1 == b2:
#     print(a1)
# elif a1 <= a2 < b1 < b2:
#     print(a2, b1)
# elif a2 <= a1 < b2 < b1:
#     print(a1, b2)
# elif a1 < a2 < b2 <= b1:
#     print(a2, b2)
# elif a2 < a1 < b1 <= b2:
#     print(a1, b1)
# elif a1 == a2 and b1 == b2:
#     print(a1, b1)


# a = int(input('Число:'))
# if a % 100 == 00:
#     print('YES')
# else:
#     print('NO')


# a = int(input('Число:'))
# b = int(input('Число:'))
# c = int(input('Число:'))
# d = int(input('Число:'))
#
# if (a + b + c + d ) % 2 == 0:
#     print('YES')
# else:
#     print('NO')


# age = int(input('Число:'))
# pol = input('Пол:')
# if 10 <= age <= 15 and pol == 'f':
#     print('YES')
# else:
#     print('NO')


# a = int(input('Число:'))
# if a == 1:
#     print('I')
# elif a == 2:
#     print('II')
# elif a == 3:
#     print('III')
# elif a == 4:
#     print('IV')
# elif a == 5:
#     print('V')
# elif a == 6:
#     print('VI')
# elif a == 7:
#     print('VII')
# elif a == 8:
#     print('VIII')
# elif a == 9:
#     print('IX')
# elif a == 10:
#     print('X')
# else:
#     print('ошибка')


# a = int(input('Число:'))
# if a % 2 != 0:
#     print('YES')
# elif a % 2 == 0 and 2 <= a <= 5:
#     print('NO')
# elif a % 2 == 0 and 6 <= a <= 20:
#     print('YES')
# elif a % 2 == 0 and a > 20:
#     print('NO')


# x1 = int(input('Число:'))
# y1 = int(input('Число:'))
# x2 = int(input('Число:'))
# y2 = int(input('Число:'))
#
# if x1 - y1 == x2 - y2 or x1 + y1 == x2 + y2:
#     print('YES')
# else:
#     print('NO')


# x1 = int(input('Число:'))
# y1 = int(input('Число:'))
# x2 = int(input('Число:'))
# y2 = int(input('Число:'))
#
# if ((x1 - x2) * (y1 - y2) == 2) or ((x1 - x2) * (y1 - y2) == -2):
#     print('YES')
# else:
#     print('NO')


# x1 = int(input('Число:'))
# y1 = int(input('Число:'))
# x2 = int(input('Число:'))
# y2 = int(input('Число:'))
#
# if (x1 == x2 and y1 != y2) or (x1 != x2 and y1 == y2) or abs(x1 - x2) == abs(y1 - y2):
#     print('YES')
# else:
#     print('NO')









