from math import sqrt
def xyx(x, y):
    x = float(input('Введите первое число x: '))
    y = float(input('Введите второе число y: '))
    print((x**2*3+y**2*3)-(x**3*9+y**3*9)-(y**2*4)
      +((x+y)*15)+(x**2*2)-(x*3)+(y*10)+6)
