# a = input('Ввод:')
# while a != 'КОНЕЦ':
#         print(a)
#         a = input('Ввод:')


# a = input('Ввод:')
# while a != 'КОНЕЦ' and a != 'конец':
#         print(a)
#         a = input('Ввод:')


# a = input('Ввод:')
# counter = 0
#
# while a != 'стоп' and a != 'хватит' and a != 'достаточно':
#         counter += 1
#         a = input('Ввод:')
# print(counter)


# a = int(input('Ввод:'))
# while a % 7 == 0:
#         print(a)
#         a = int(input('Ввод:'))


# a = int(input('Ввод:'))
# total = 0
#
# while a >= 0:
#         total += a
#         a = int(input('Ввод:'))
# print(total)


# num = int(input('Ввод:'))
# counter5 = 0
#
# while 0 <= num <= 5:
#         if num == 5:
#                 counter5 += 1
#         num = int(input('Ввод:'))
# print(counter5)


# n = int(input('Ввод:'))
# counter = 0
# while n >= 25:
#         counter += 1
#         n = n - 25
# while n >= 10:
#         counter += 1
#         n = n - 10
# while n >= 5:
#         counter += 1
#         n = n - 5
# while n >= 1:
#         counter += 1
#         n = n - 1
# print(counter)


# num = int(input('Ввод:'))
#
# while num != 0:
#         n = num % 10
#         print(n, end='')
#         num = num // 10


# total = 0
# maax = 0
# miin = 9
# n = int(input('Ввод:'))
#
# while n > 0:
#         num = n % 10
#         total = num
#         if total > maax:
#                 maax = total
#         if total < miin:
#                 miin = total
#         n = n // 10
# print('Максимальная цифра равна', maax)
# print('Минимальная цифра равна', miin)


# n = int(input('Ввод:'))
# summ = 0
# counter = 0
# proiz = 1
# last = n % 10
#
# while n != 0:
#     first_num = n % 10
#     summ += first_num
#     counter += 1
#     proiz *= first_num
#     n = n // 10
# print(summ, counter, proiz, summ / counter, first_num, first_num + last, sep='\n')


# n = int(input('Ввод:'))
# while n > 9:
#     num = n % 10
#     n = n // 10
# print(num)


# n = int(input('Ввод:'))
# last_digit = n % 10
# counter = 0
#
# while n > 0:
#     new_last_digit = n % 10
#     n = n // 10
#     if last_digit != new_last_digit:
#         counter += 1
# if counter < 0:
#     print('NO')
# else:
#     print('YES')


# n = int(input('Ввод:'))
# flag = True
# s = n % 10
# while n != 0:
#     n1 = n % 10
#     if n1 < s:
#         flag = False
#     else:
#         s = n1
#     n = n // 10
# if flag == True:
#     print('YES')
# else:
#     print('NO')


# n = int(input('Ввод:'))
# for i in range(2, n + 1):
#     if n % i == 0:
#         print(i)
#         break


# n = int(input('Ввод:'))
# for i in range(1, n + 1):
#     if 5 <= i <= 9 or 17 <= i <= 37 or 78 <= i <= 87:
#         continue
#     print(i)


# mx = -10 ** 6
# s = 0
# for i in range(1, 11):
#     x = int(input())
#     if x < 0:
#         s += x
#         if x > mx:
#             mx = x
# if s < 0:
#     print(s)
#     print(mx)
# else:
#     print('NO')


# n = int(input())
# max_digit = -1
# while n > 0:
#     digit = n % 10
#     if digit % 3 == 0:
#         if digit > max_digit:
#             max_digit = digit
#     n = n // 10
# if max_digit == -1:
#     print('NO')
# else:
#     print(max_digit)


# n = int(input())
# while n > 9:
#     n //= 10
# print(n)


# n = int(input())
# product = 1
# while n > 0:
#     digit = n % 10
#     product = product * digit
#     n //= 10
# print(product)


# n = int(input('Ввод:'))
# for i in range(n):
#     for j in range(3):
#         print('*', end=' ')
#     print()


# n = int(input('Ввод:'))
# for i in range(1, n + 1):
#     for _ in range(5):
#         print(i, end=' ')
#     print()


# n = int(input('Ввод:'))
# # for i in range(1, n + 1):
# #     for j in range(1, 10):
# #         print(i, '+', j, '=', i + j)
# #     print()


# n = int(input('Ввод:'))
# for i in range(1, n // 2 + 2):
#     print('*' * i)
# for j in range(n // 2, 0, -1):
#     print('*' * j)


# n = int(input('Ввод:'))
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(i, end=' ')
#     print()







