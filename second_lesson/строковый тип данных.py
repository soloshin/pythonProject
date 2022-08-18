# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
#
# print(s[7])


# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
#
# print(s[-10])


# s = input('Ввод:')
# for i in range(0, len(s), 2):
#     print(s[i])


# s = input('Ввод:')
# for i in range(-1, -len(s) - 1, -1):
#     print(s[i])


# a = input('Ввод:')
# b = input('Ввод:')
# c = input('Ввод:')
# print(b[0], a[0], c[0], sep='')

# n = input('Ввод:')
# total = 0
# for i in n:
#     total += int(i)
# print(total)


# n = input('Ввод:')
# flag = 'Цифр нет'
# for i in range(len(n)):
#     if n[i] in ('0123456789'):
#         flag = 'Цифра'
#         break
# print(flag)



# n = input('Ввод:')
# counter_star = 0
# counter_plus = 0
#
# for i in range(len(n)):
#     if n[i] in ('*'):
#         counter_star += 1
#     elif n[i] in ('+'):
#             counter_plus += 1
# print('Символ + встречается', counter_plus, 'раз')
# print('Символ * встречается', counter_star, 'раз')


# n = input('Ввод:')
# counter = 0
# for i in range(0, len(n) - 1):
#     if n[i] == n[i + 1]:
#         counter += 1
# print(counter)


# n = input('Ввод:')
# counter_glass = 0
# counter_soglass = 0
#
# for i in range(len(n)):
#     if n[i] in ('а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е','А','У','О','Ы','И','Э','Я','Ю','Ё','Е'):
#         counter_glass += 1
#     elif n[i] in ('б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'Б', 'В', 'Г', 'Д','Ж','З','Й','К','Л','М','Н','П','Р','С','Т','Ф','Х','Ц','Ч','Ш','Щ'):
#         counter_soglass += 1
# print('Количество гласных букв равно', counter_glass)
# print('Количество согласных букв равно', counter_soglass)


# n = int(input('Ввод:'))
# s = ''
# while n != 0:
#     s = str(n % 2) + s
#     n = n // 2
# print(s)


# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[-9:])


# s = input('Ввод:')
# if s == s[::-1]:
#     print('YES')
# else:
#     print('NO')


# s = input('Ввод:')
# print(len(s))
# print(s * 3)
# print(s[0])
# print(s[:3])
# print(s[-3:])
# print(s[::-1])
# print(s[1:-1])


# s = input('Ввод:')
# print(s[2])
# print(s[-2])
# print(s[:5])
# print(s[:-2])
# print(s[::2])
# print(s[1::2])
# print(s[::-1])
# print(s[::-2])


# s = input('Ввод:')
# if s == s.title():
#     print('YES')
# else:
#     print('NO')


# s = input('Ввод:')
# print(s.swapcase())


# s = input('Ввод:').lower()
# flag = 'NO'
# if 'хорош' in s:
#     flag = 'YES'
# print(flag)


# s = input('Ввод:')
# count = 0
#
# for i in range(len(s)):
#     if s[i] in ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'):
#         count += 1
# print(count)


# s = input('Ввод:')
# print(s.count(' ') + 1)


# s = input('Ввод:').lower()
# print('Аденин: ' + str(s.count('a')), 'Гуанин: ' + str(s.count('г')), 'Цитозин: ' + str(s.count('ц')), 'Тимин: ' + str(s.count('т')), sep='\n')


# n = int(input('Ввод:'))
# count1 = 0
# for _ in range(n):
#     n = input('Ввод:')
#     if n.count('11') >= 3:
#         count1 += 1
# print(count1)


# s = input('Ввод:')
# total = 0
# for i in range(10):
#     total = total + s.count(str(i))
# print(total)


# s = input('Ввод:')
# if s.endswith('.com') or s.endswith('.ru'):
#     print('YES')
# else:
#     print('NO')


# s = input('Ввод:')
# maxx = 0
# b = 0
# for i in s:
#     if s.count(i) >= maxx:
#         maxx = s.count(i)
#         b = i
# print(b)


# s = input('Ввод:')
# if s.count('f') == 1:
#     print(s.find('f'))
# elif s.count('f') >= 1:
#     print(s.find('f'), s.rfind('f'))
# else:
#     print('NO')


# s = input()
#
# print(s[:s.find('h')] + s[s.rfind('h')+1:])


# a = int(input('Ввод:'))
# b = int(input('Ввод:'))
# for i in range(a, b + 1):
#     print(chr(i), end=' ')


# s = input('Ввод:')
# for i in s:
#     print(ord(i), end=' ')


# n = int(input('Ввод:'))
# text = input('Ввод:')
#
# for letter in text:
#     decryption = ord(letter) - n
#     if decryption < 97:
#         decryption += 26
#     print(chr(decryption), end='')
#
#     1.
#     n.Объявляете
#     переменную
#     с
#     числом(это
#     наш
#     шаг)
#     2.
#     text.Объявляете
#     строковую
#     переменную(это
#     сам
#     текст)
#     3.
#     Создаёте
#     цикл, который
#     будет
#     перебирать
#     каждую
#     букву
#     текста:
#     for letter in text:
#         Мы
#         ДЕшифруем, а
#         потому
#         отнимаем
#         от
#         ЦИФРОВОГО(ord)
#         кода
#         каждой
#         буквы
#         шаг
#     decryption(дешифрование) = ord(letter) - n
# И
# строкой
# ниже
# создаём
# условие, если
# после
# того, как
# мы
# отнимем
# от
# цифрового
# кода
# наш
# шаг
# получится
# число
# меньше
# 97(97 - цифровой
# код
# буквы “a”), то
# добавляем
# к
# переменной
# decryption
# 26(кол - во
# букв
# в
# английском
# алфавите, дабы
# оттолкнуться
# от
# буквы “а” и
# попасть
# на
# нужную)
# if decryption < 97:
#     decryption += 26
# Всё, это
# вся
# программа, выводим
# на
# экран
# значение
# нашего
# дешифрования(но
# уже
# в
# виде
# букв
# а
# не
# цифрового
# кода(chr)), в
# цикле
# и, чтобы
# это
# все
# выводилось
# в
# одну
# строку, оставляем ‘’пустой’’ end
# print(chr(decryption), end=‘’)


# s = input()
# for i in range(len(s)):
#     if i % 3 != 0:
#         print(s[i], end='')


# s = input('Ввод:')
# print(s.replace('1', 'one'))

# s = input('Ввод:')
# print(s.replace('@',''))

# s = input('Ввод:')
# if s.count('f') == 1:
#     print(-1)
# elif s.count('f') == 0:
#     print(-2)
# else:
#     s = s.replace('f', ' ', 1)
#     print(s.find('f'))

# s = input('Ввод:')
# print(s [ : s.find('h') ]   +   s[ s.rfind('h') : s.find('h') :  -1 ]   +   s[ s.rfind('h')  :  ])


# n = int(input('Ввод:'))
# a =[]
# for i in range(97, n + 97):
#     s = chr(i)
#     a += s
# print(a)


# numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
# print(len(numbers))
# print(numbers[-1])
# print(numbers[::-1])
# if 5 and 17 in numbers:
#     print('YES')
# else:
#     print('NO')
#
# del numbers[0]
# del numbers[-1]
# print(numbers)


# s = []
# n = int(input('Ввод:'))
# for i in range(n):
#     languages = input('Ввод:')
#     s.append(languages)
# print(s)


# sp = ['Ввод:']
# for i in range(1, 27):
#     sp.append(chr(96 + i) * i)
# print(sp)

# l = []
# n = int(input('Ввод:'))
# for i in range(n):
#     n1 = int(input('Ввод:'))
#     l.append(n1 ** 3)
# print(l)


# n = int(input('Ввод:'))
# l = []
# for i in range(1, n + 1):
#     if n % i == 0:
#         l.append(i)
# print(l)


# n = int(input('Ввод:'))
# total = 0
# sp = []
# for i in range(n):
#     l = int(input('Ввод:'))
#     total += l
#     sp.append(total)
#     total = l
# print(sp[1:])


# l = []
# n = int(input('Ввод:'))
# for i in range(n):
#     n1 = int(input('Ввод:'))
#     l.append(n1)
# del l[1::2]
# print(l)


# n = int(input('Ввод:'))
# list1 = []
# for i in range(n):
#     a = input('Ввод:')
#     list1.append(a)
#
# k = int(input('Ввод:'))
# x1 = ''
# x2 = ''
# for j in range(n):
#     if len(list1[j]) >= k:
#         x1 = list1[j][k - 1]
#         x2 += x1
# print(x2)


# n = int(input('Ввод:'))
# l = []
# for i in range(n):
#     s = input('Ввод:')
#     l.extend(s)
# print(l)


# numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
# total = 0
# for i in numbers:
#     total += i ** 2
# print(total)


# sp1 = []
# sp2 = []
# n = int(input('Ввод:'))
# for i in range(n):
#     n1 = int(input('Ввод:'))
#     sp1.append(n1)
# print(*sp1, sep='\n')
# print()
#
# for x in sp1:
#     f =  x ** 2 + 2  * x + 1
#     sp2.append(f)
# print(*sp2, sep='\n')


# sp = []
# n = int(input('Ввод:'))
# for i in range(n):
#     n1 = int(input('Ввод:'))
#     sp.append(n1)
# for j in sp:
#     if j != min(sp) and j != max(sp):
#         print(j)


# sp = []
# n = int(input('Ввод:'))
# for i in range(n):
#     s = input('Ввод:')
#     if s not in sp:
#         sp.append(s)
# print(*sp, sep='\n')


# sp = []
# n = int(input('Ввод:'))
# for i in range(n):
#     a = input('Ввод:')
#     sp.append(a)
# zapros = input('Ввод:')
# for x in sp:
#     if zapros.lower() in x.lower():
#         print(x)
#     else:
#         continue


# n = int(input('Ввод:'))
# a = []
# b = []
# c = []
# for i in range(n):
#     s = input('Ввод:')
#     a.append(s)
#
# k = int(input('Ввод:'))
# for i in range(k):
#     s1 = input('Ввод:')
#     b.append(s1)
#
# for i in range(len(a)):
#     count = 0
#     for j in range(len(b)):
#         if b[j].lower() in a[i].lower():
#             count += 1
#     if count == len(b):
#         print(a[i])

#
# negative = []
# positive = []
# zero = []
#
# n = int(input('Ввод:'))
# for i in range(n):
#     n1 = int(input('Ввод:'))
#     if n1 < 0:
#         negative.append(n1)
#     elif n1 == 0:
#         zero.append(n1)
#     elif n1 > 0:
#         positive.append(n1)
# print(*negative, *positive, *zero, sep='\n' )


# s = input('Ввод:')
# words = s.split()
# print(*words, sep='\n')


# s = input('Ввод:').split()
# for i in range(len(s)):
#     print(s[i][0],end='.')


# s = input('Ввод:')
# words = s.split('\\')
# print(*words, sep='\n')


# s = input('Ввод:')
# words = s.split()
# for i in range(len(words)):
#     words[i] = int(words[i])
#     print('+' * words[i])\


# ip = input('Ввод:').split('.')
# if len(ip) == 4 and (0 <= int(ip[0]) <= 255) and (0 <= int(ip[1]) <= 255) and (0 <= int(ip[2]) <= 255) and (0 <= int(ip[3]) <= 255):
#     print('ДА')
# else:
#     print('НЕТ')


# a = list(input('Ввод:'))
# delitel = input('Ввод:')
# print(*a, sep=delitel)


# s = input('Ввод:').split()
# counter = 0
#
#
# for i in range(len(s)):
#     for j in range(i + 1, len(s)):
#         if s[i] == s[j]:
#             counter += 1
# print(counter)


# numbers = [8, 9, 10, 11]
# numbers[1] = 17
# numbers.extend([4, 5, 6])
# del numbers[0]
# numbers *= 2
# numbers.insert(3, 25)
# print(numbers)


# s = input('Ввод:')
# numbers = s.split()
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
# maxx = numbers.index(max(numbers))
# print(maxx)

# s = input().split()
# s_min = min(s, key=int)
# s_max = max(s, key=int)
# i_min = s.index(s_min)
# i_max = s.index(s_max)
# s[i_max] = s_min
# s[i_min] = s_max
# print(*s, sep=' ')


# s = input('Ввод:').lower().split()
# print('Общее количество артиклей:',s.count('a') + s.count('an') + s.count('the'))


# n = input('Ввод:')
# for _ in range(int(n[1:])):
#     s = input('Ввод:')
#     if '#' in s:
#         s = s[:s.find('#')]
#     print(s.rstrip())



# int_lst = [int(i) for i in input('Ввод:').split()]
# int_lst.sort()
# print(*int_lst)
# int_lst.sort(reverse=True)
# print(*int_lst)


# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
#
# new_keywords = [i[1:] for i in keywords]
#
# print(new_keywords)


# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
#
# lengths = [len(i) for i in keywords]
#
# print(lengths)


# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
#
# new_keywords = [i for i in keywords if len(i) >= 5]
#
# print(new_keywords)


# palindromes = [i for i in range(100, 1001) if i % 10 == i // 100]
#
# print(palindromes)


# numbers = [i ** 2 for i in range(1, int(input('Ввод:')) + 1)]
# print(*numbers, sep='\n')


# s = [int(i) ** 3 for i in (input('Ввод:').split())]
# print(*s)


# s = [i for i in input('Ввод:').split()]
# print(*s, sep='\n')


# s = [i for i in input('Ввод:') if i in '0123456789']
# print(*s, sep='')

# s = [int(i) ** 2 for i in input('Ввод:').split() if int(i) ** 2 % 2 == 0 and int(i) ** 2 % 10 != 4]
# print(*s)


# n = int(input('Ввод:'))
# line = [i for i in range(1, n + 1)]
# print(line[1::2])


# lst1 = [int(i) for i in input('Ввод:').split()]
# lst2 = [int(i) for i in input('Ввод:').split()]
# result = [lst1[i] + lst2[i] for i in range(len(lst1))]
# print(*result)


# n = [int(i) for i in (input('Ввод:').split())]
# print(*n, sep='+', end=f'={sum(n)}')


# n = input().split("-")
# c = [len(i) for i in n]
# if c == [3, 3, 4] and ''.join(n).isdigit():
#     print("YES")
# elif c == [1, 3, 3, 4] and ''.join(n).isdigit() and n[0] == '7':
#     print("YES")
# else:
#     print("NO")


# print(*[i[1:] + i[0] + "ки"for i in input().split()])

