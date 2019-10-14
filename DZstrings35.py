l = list(range(10))
string = ''
for i in l:
   string += str(i)
g = 'a'
i = 0
new_str = ''
while i < len(string):
    if i % 2 == 0:
        new_str += str(i)
    else:
        new_str += g
    i += 1
print(new_str)

