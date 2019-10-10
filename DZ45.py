def DZ45(a, b, c, d):
    a = int(input('введите а: '))
    b = int(input('введите b: '))
    c = int(input('введите c: '))
    d = int(input('введите d: '))
    if a <= b and b <= c and c <= d:
        a = d
        b = d
        c = d
        print(a,b,c,d)
    elif a > b and b > c and c > d:
        print(a,b,c,d)
   
