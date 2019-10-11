s = 'Hello  Ukraine  -  my country 345111'
num = [int(i) for i in s if i.isdigit()]
print('Количество цифр в тексте:', len(num))
