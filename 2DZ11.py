# Строка состоит из слов, разделенных одним или несколькими пробелами. Найдите слово наибольшей длины.

s = 'Hello  Ukraine  -  my country'
b = s.split()
print(s)
print(b)
print(max(b, key=len))

