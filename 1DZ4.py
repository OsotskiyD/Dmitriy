from math import sqrt
# 4. Даны два действительных положительных числа.Найти среднее арифметическое и среднее геометрическое этих чисел.


def math(a, b):
    c = (a+b)/2
    d = sqrt(a*b)
    print("sred ar: ", c, "sred geo: ", d)


math(10, 20)