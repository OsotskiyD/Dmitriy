import re
s = 'Hello  Ukraine  -  my country'
index = re.findall(r'  ', s)
edited = s.replace('  ', ' ')
print(s)
print(index)
print(edited)

