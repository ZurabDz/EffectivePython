even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
print(even_squares)

# This one is clumsy but if function logic is complicated
# things turn around
res = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, range(10)))
print(list(res))

