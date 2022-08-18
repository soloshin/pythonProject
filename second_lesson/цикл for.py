
# for i in range(10):
#     print('Python is awesome!')


# a = input('Ввод:')
# b = int(input('Ввод:'))
#
# for _ in range(b):
#     print(a)


# for _ in range(6):
#     print('AAA')
# for _ in range(5):
#     print('BBBB')
# print('E')
# for _ in range(9):
#     print('TTTTT')
# print('G')


# n = int(input('Ввод:'))
# for _ in range(n):
#     print('*' * 19)


# a = input('Ввод:')
# for i in range(10):
#     print(i,a)


# n = int(input('Ввод:'))
# for i in range(n + 1):
#     print('Квадрат числа', i, 'равен', i ** 2)


# n = int(input('Ввод:'))
# for i in range(n):
#     print('*' * (n - i))


# m = float(input('Ввод:'))
# p = float(input('Ввод:'))
# n = int(input('Ввод:'))
# for i in range(n):
#     print(i + 1, m * (p / 100 + 1) ** i)


# m = int(input('Ввод:'))
# n = int(input('Ввод:'))
# for i in range(m, n + 1):
#     print(i)


# m = int(input('Ввод:'))
# n = int(input('Ввод:'))
# if m < n:
#     for i in range(m, n + 1):
#         print(i)
# elif m > n:
#     for i in range(m, n - 1, -1):
#         print(i)
# elif m == n:
#     print(m)


# m = int(input('Ввод:'))
# n = int(input('Ввод:'))
# if m % 2 != 0:
#     for i in range(m, n -1, -2):
#         print(i)
# elif m % 2 == 0:
#     for i in range(m, n, -2):
#         print(i - 1)


# m = int(input('Ввод:'))
# n = int(input('Ввод:'))
# m1 = m % 2 - 1 + m
# for i in range(m1, n, -2):
#     print(i)


# m = int(input('Ввод:'))
# n = int(input('Ввод:'))
# for i in range(m, n + 1):
#     if i % 17 == 0:
#         print(i)
#     elif i % 10 == 9:
#         print(i)
#     elif (i % 3 == 0) and (i % 5 == 0):
#         print(i)


# n = int(input('Ввод:'))
# for i in range(1, 11):
#     print(n, 'x', i, '=', n * i)


# total = 0
# # for i in range(1, 6):
# #     total += i
# #     print(total, end='')


# counter = 0
# a = int(input('Ввод:'))
# b = int(input('Ввод:'))
#
# for i in range(a, b + 1):
#     if i ** 3 % 10 == 4 or i ** 3 % 10 == 9:
#         counter += 1
# print(counter)


# n = int(input('Ввод:'))
# total = 0
# for i in range(n):
#     total += int(input('Ввод:'))
# print(total)


# import math
#
# num = 0
# n = int(input('Ввод:'))
# for i in range(1, n):
#     num = num + (1 / (i + 1))
# num2 = num + 1 - math.log(n)
# print(num2)


# total = 0
# n = int(input('Ввод:'))
#
# for i in range(1, n + 1):
#     if i ** 2 % 10 == 2 or i ** 2 % 10 == 5 or i ** 2 % 10 == 8:
#         total = total + i
# print(total)


# total = 1
# n = int(input('Ввод:'))
# for i in range(1, n + 1):
#     total *= i
# print(total)


# total = 1
# for i in range(1, 11):
#     num = int(input('Ввод:'))
#     if num != 0:
#         total *= num
# print(total)


# total = 0
# n = int(input('Ввод:'))
# for i in range(1, n + 1):
#     if n % i == 0:
#         total += i
# print(total)


# n = int(input('Ввод:'))
# counter = 0
#
# for i in range(1, n + 1):
#     if i % 2 == 0:
#         counter -= i
#     else:
#         counter += i
# print(counter)


# n = int(input('Ввод:'))
# max1 = 0
# max2 = 1
#
# for i in range(1, n + 1):
#     num = int(input('Ввод:'))
#     if num > max1:
#         max2 = max1
#         max1 = num
#     elif num > max2:
#         max2 = num
# print(max1)
# print(max2)


# counter = 0
#
# for i in range(1, 11):
#     num = int(input('Ввод:'))
#     if num % 2 == 0:
#         counter += 1
# if counter == 10:
#     print('YES')
# else:
#     print('NO')



# n = int(input('Ввод:'))
# a = 1
# y = 0
#
# for i in range(1, n + 1):
#     b = a
#     a = b + y
#     y = b
#     print(b, end=' ')
