from re import *

def get_address():
    pattern = compile('(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)')
    address = input('inter you email address:')
    is_valid = pattern.match(address)
    if is_valid:
        print('правильный email:', is_valid.group())
    else:
        print('неверный email! введите email...\n')


get_address()
