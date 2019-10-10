year = int (input('высокосный год: '))
if year%4 != 0 or (year%100 == 0 and not year%400 == 0):
    print('не высокосный')
else:
    print('высокосный')

