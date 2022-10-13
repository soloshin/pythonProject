# объявление функции
# def draw_box():
#     print('*' * 10)
#     for i in range(14 - 2):
#         print('*', '*', sep='        ')
#     print('*' * 10)
#
#
# draw_box()


# # объявление функции
# def draw_triangle():
#     for i in range(1, 11):
#         print('*' * i)
#
# # основная программа
# draw_triangle()  # вызов функции





# # объявление функции
# def print_fio(name, surname, patronymic):
#     print(name[0].upper(), surname[0].upper(), patronymic[0].upper())
#
# # считываем данные
# name, surname, patronymic = input(), input(), input()
#
# # вызываем функцию
# print_fio(name, surname, patronymic)


# # объявление функции
# def convert_to_miles(km):
#     return km * 0.6214
#
# # считываем данные
# num = int(input('add:'))
#
# # вызываем функцию
# print(convert_to_miles(num))


# # объявление функции
# def get_days(month):
#     m = [31,28,31,30,31,30,31,31,30,31,30,31]
#     return m[month - 1]
#
# # считываем данные
# num = int(input('ввод:'))
#
# # вызываем функцию
# print(get_days(num))


# # объявление функции
# def get_factors(num):
#     num = []
#     for i in range(1, n + 1):
#         if n % i == 0:
#             num.append(i)
#     return num
# # считываем данные
# n = int(input('ввод:'))
#
# # вызываем функцию
# print(get_factors(n))