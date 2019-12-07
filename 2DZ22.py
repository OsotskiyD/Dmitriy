# Дан email в строке. Определить, является ли он корректным (наличие символа @
# и точки, наличие не менее двух символов после последней точки и т.д.).

from re import *


def get_address():
    pattern = compile('(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)')
    address = input('enter you email address:')
    is_valid = pattern.match(address)
    if is_valid:
        print('?????????? email:', is_valid.group())
        print('??????: start:', is_valid.start(), 'end:',\
        is_valid.end(), 'group:', is_valid.group())
    else:
        print('???????? email! ??????? email...\n')


get_address()


