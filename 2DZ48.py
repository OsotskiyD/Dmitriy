# Дан текст. Найти сумму имеющихся в нем цифр.

s = 0
for i in 'fjgjjtii2345768':
    if i.isdigit():
        s += int(i)
print('сумма чисел =', s)


