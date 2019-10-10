from math import sqrt
def geo(a, b):
    a=float(input('Введите первый катет: '))
    b=float(input('Введите гипотенузу: '))
    k=sqrt(b*b-a*a)
    r=a*k/(a+b+k)
    print( "второй катет: ", k, "радиус вписаной окружности: ", r)
