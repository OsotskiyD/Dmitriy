import re
s = 'Hello Ukraine  - ///\\ my country 345111'
print(s)
print(s.lower())
result = re.sub(r'[^A-Za-z]', ' ', s)
print(result)
result = []
g = ['a', 'e', 'i', 'o', 'u', 'y']
for i in s.lower():
    if i in g and i not in result:
        result.append(i)
b = sorted(result)
print(b)
