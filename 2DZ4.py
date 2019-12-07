import re
# В строке найдите все серии подряд идущих пробелов и замените каждую на один пробел.


s = 'Hello  Ukraine  -  my country'
index = re.findall(r'  ', s)
edited = s.replace('  ', ' ')
print(s)
print(index)
print(edited)

