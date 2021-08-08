# format function is decent but not ideal for string formatting

a = 1234.5678
formatted = format(a, ',.2f')
print(formatted)
# 1,234.57

b = 'my string'
formatted = format(b, '^20s')
print('*', formatted, '*')
# *      my string       *

key = 'my_var'
value = 1.234

formatted = '{} = {}'.format(key, value)
print(formatted)
#my_var = 1.234


# Use help('FORMATTING') for additional options
formatted = '{:<10} = {:.2f}'.format(key, value)
print(formatted)
#my_var     = 1.23

# use Interpolated Format Strings
formatted = f'{key!r:<10} = {value:.2f}'
print(formatted)
# 'my_var'   = 1.23
