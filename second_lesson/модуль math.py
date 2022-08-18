# math.ceil(X) – округление до ближайшего большего числа.
#
# math.copysign(X, Y) - возвращает число, имеющее модуль такой же, как и у числа X, а знак - как у числа Y.
#
# math.fabs(X) - модуль X.
#
# math.factorial(X) - факториал числа X.
#
# math.floor(X) - округление вниз.
#
# math.fmod(X, Y) - остаток от деления X на Y.
#
# math.frexp(X) - возвращает мантиссу и экспоненту числа.
#
# math.ldexp(X, I) - X * 2i. Функция, обратная функции math.frexp().
#
# math.fsum(последовательность) - сумма всех членов последовательности. Эквивалент встроенной функции sum(), но math.fsum() более точна для чисел с плавающей точкой.
#
# math.isfinite(X) - является ли X числом.
#
# math.isinf(X) - является ли X бесконечностью.
#
# math.isnan(X) - является ли X NaN (Not a Number - не число).
#
# math.modf(X) - возвращает дробную и целую часть числа X. Оба числа имеют тот же знак, что и X.
#
# math.trunc(X) - усекает значение X до целого.
#
# math.exp(X) - eX.
#
# math.expm1(X) - eX - 1. При X → 0 точнее, чем math.exp(X)-1.
#
# math.log(X, [base]) - логарифм X по основанию base. Если base не указан, вычисляется натуральный логарифм.
#
# math.log1p(X) - натуральный логарифм (1 + X). При X → 0 точнее, чем math.log(1+X).
#
# math.log10(X) - логарифм X по основанию 10.
#
# math.log2(X) - логарифм X по основанию 2. Новое в Python 3.3.
#
# math.pow(X, Y) - XY.
#
# math.sqrt(X) - квадратный корень из X.
#
# math.acos(X) - арккосинус X. В радианах.
#
# math.asin(X) - арксинус X. В радианах.
#
# math.atan(X) - арктангенс X. В радианах.
#
# math.atan2(Y, X) - арктангенс Y/X. В радианах. С учетом четверти, в которой находится точка (X, Y).
#
# math.cos(X) - косинус X (X указывается в радианах).
#
# math.sin(X) - синус X (X указывается в радианах).
#
# math.tan(X) - тангенс X (X указывается в радианах).
#
# math.hypot(X, Y) - вычисляет гипотенузу треугольника с катетами X и Y (math.sqrt(x * x + y * y)).
#
# math.degrees(X) - конвертирует радианы в градусы.
#
# math.radians(X) - конвертирует градусы в радианы.
#
# math.cosh(X) - вычисляет гиперболический косинус.
#
# math.sinh(X) - вычисляет гиперболический синус.
#
# math.tanh(X) - вычисляет гиперболический тангенс.
#
# math.acosh(X) - вычисляет обратный гиперболический косинус.
#
# math.asinh(X) - вычисляет обратный гиперболический синус.
#
# math.atanh(X) - вычисляет обратный гиперболический тангенс.
#
# math.erf(X) - функция ошибок.
#
# math.erfc(X) - дополнительная функция ошибок (1 - math.erf(X)).
#
# math.gamma(X) - гамма-функция X.
#
# math.lgamma(X) - натуральный логарифм гамма-функции X.
#
# math.pi - pi = 3,1415926...
#
# math.e - e = 2,718281...



# import math
#
# x1 = float(input('Ввод:'))
# y1 = float(input('Ввод:'))
# x2 = float(input('Ввод:'))
# y2 = float(input('Ввод:'))
# p = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
# print(p)



# import math
#
# r = float(input('Ввод:'))
# s = math.pi * math.pow(r, 2)
# c = 2 * math.pi * r
# print(s, c, sep='\n')


# import math
#
# a = float(input('Ввод:'))
# b = float(input('Ввод:'))
# ar = (a + b) / 2
# geo = math.sqrt(a * b)
# gar = (2 * a * b) / (a + b)
# kva = math.sqrt((math.pow(a, 2) + math.pow(b, 2)) / 2)
# print(ar, geo, gar, kva, sep='\n')


# import math
# #
# # x = float(input('Ввод:'))
# # r = math.radians(x)
# # trig = math.sin(r) + math.cos(r) + (math.tan(r) ** 2)
# # print(trig)


# import math
#
# x = float(input('Ввод:'))
# print(math.ceil(x) + math.floor(x))


# from math import
#
# a = float(input())
# b = float(input())
# c = float(input())
# d = b**2-4*a*c
#
# if d < 0:
#     print('Нет корней')
# elif d == 0:
#     print(-b / (2*a))
# elif d > 0:
#     x1 = (-b - d ** 0.5) / (2*a)
#     x2 = (-b + d ** 0.5) / (2*a)
#     print(min(x1, x2))
#     print(max(x1, x2))


# import math
#
# n = float(input('Ввод:'))
# a = float(input('Ввод:'))
# s = (n * a ** 2) / (4 * math.tan(math.pi / n))
# print(s)

