a = b'h\x65llo'

print(list(a))
# [104, 101, 108, 108, 111]

print(a)
# b'hello'

a = 'a\u0300 propos'

print(list(a))
# ['a', '̀', ' ', 'p', 'r', 'o', 'p', 'o', 's']
print(a)
# à propos


def to_str(bytes_or_str):
    '''
    Converts bytes/strings to string
    '''
    if isinstance(bytes_or_str, bytes):
        return bytes_or_str.decode('utf-8')
    return bytes_or_str


def to_byte(bytes_or_str):
    '''
    Converts bytes/strings to bytes
    '''
    if isinstance(bytes_or_str, str):
        return bytes_or_str.encode('utf-8')

    return bytes_or_str


print(repr(to_byte(b'foo')))
print(to_byte(b'bar'))

# Checking System default encoding from commad
# python3 -c 'import locale; print(locale.getpreferredencoding())'