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


# объявление функции
def print_digit_sum(num):
    sp = [ int(i)  for  i  in  str(num) ]
    print(sum(sp))

# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)