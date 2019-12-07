from functools import wraps

# Дана строка. Разделить строку на фрагменты по три подряд идущих символа.
# В каждом фрагменте средний символ заменить на случайный символ, не совпадающий ни с одним из символов этого фрагмента.
# Показать фрагменты, упорядоченные по алфавиту.


def dz9(self, s):
    split_len = 3
    letter = ''
    a = ' '
    s = s.replace(' ', '')
    s = textwrap.wrap(s, 3)
    for i in s:
        index = 1
        a = random.choice(string.ascii_letters)
        try:
            while a == i[0]:
                a = random.choice(string.ascii_letters)
        except:
            pass
        try:
            while a == i[2]:
                a = random.choice(string.ascii_letters)
        except:
            pass
        i = i[:index] + a + i[index + 1:]
        letter = letter[:] + i
    letter = textwrap.wrap(letter, 3)
    letter.sort()
    return (letter)


dz9('ghgjgkl', '2')
