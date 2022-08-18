
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


# for n in range(1, 14):
#     for k in range(1, 13):
#         for m in range(1, 12):
#             if 28 * n + 30 * k + 31 * m == 365:
#                 print('n =', n, 'k =', k, 'm =', m)


# for n in range(1, 11):
#     for k in range(1, 21):
#         for m in range(1, 201):
#             if 10 * n + 5 * k + 0.5 * m == 100:
#                 if n + k + m == 100:
#                     print(n, k, m)


# n = int(input('Ввод:'))
# num = 1
# for row in range(1, n + 1):
#     for k in range(1, row + 1):
#         print(num, end=' ')
#         num += 1
#     print()


# n = int(input('Ввод:'))
# for i in range(1, n + 1):
#     for j in range(i):
#         print(j + 1, end='')
#     for k in range(i - 1, 0, -1):
#         print(k, end='')
#     print()


# a = int(input('Ввод:'))
# b = int(input('Ввод:'))
# largest = 0
# total = 0
# for i in range(a, b + 1):
#     counter = 0
#     for j in range(1, i + 1):
#          if i % j == 0:
#              counter += j
#              if counter >= total:
#                  total = counter
#                  largest = i
# print(largest, total, end=" ")


# n = int(input('Ввод:'))
# for i in range(1, n + 1):
#     counter = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             counter += 1
#     print(i, '+' * counter, sep='')


# n = int(input('Ввод:'))
# while n > 9:
#     total = 0
#     while n > 0:
#         last_digit = n % 10
#         total += last_digit
#         n //= 10
#     n = total
# print(n)


# import math
#
# n = int(input('Ввод:'))
# summ = 0
# for x in range(1, n + 1):
#     summ += math.factorial(x)
# print(summ)


# a = int(input('Ввод:'))
# b = int(input('Ввод:'))
#
# for i in range(a, b + 1):
#     counter = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             counter += 1
#     if counter == 2:
#       print(i)


# i = 4
# while i <= 10:
#     print ('Python!')
#     i += 1


# n = 8
# count = 0
# maximum = 0
# for i in range(1, n + 1):
#     x = int(input('Ввод:'))
#     if x % 4 == 0:
#         count += 1
#         if x < maximum:
#             maximum = x
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')


# n = int(input('Ввод:'))
# print('*' * 19)
# for i in range(n - 2):
#     print('*', '*', sep='                 ')
# print('*' * 19)


# n = int(input('Ввод:'))
# while n > 99:
#     a = n % 10
#     n = n // 10
# print(a)


# num = int(input('Ввод:'))
# cifra3=0
# posl_cifra=num%10
# count_posl_cifra=0
# count_chet_cifr=0
# sum_cifr5=0
# proiz_cifr7=1
# count_0_5=0
#
# while num!=0:
#     last_digit = num % 10
#     if last_digit==3:
#         cifra3+=1
#     if last_digit==posl_cifra:
#         count_posl_cifra+=1
#     if last_digit%2==0:
#         count_chet_cifr+=1
#     if last_digit>5:
#         sum_cifr5+=last_digit
#     if last_digit>7:
#         proiz_cifr7*=last_digit
#     if last_digit==0 or last_digit==5:
#         count_0_5+=1
#     num = num // 10
# print(cifra3)
# print(count_posl_cifra)
# print(count_chet_cifr)
# print(sum_cifr5)
# print(proiz_cifr7)
# print(count_0_5)







