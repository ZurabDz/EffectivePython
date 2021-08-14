# A decorator has the ability to run additional code before
# and after each call to a function it wraps. This means decorators
# can access and modify input arguments, return values, and raised
# exceptions. This functionality can be useful for enforcing semantics,
# debugging, registering functions, and more.


def trace(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        print(f'{func.__name__}({args!r}, {kwargs!r}) -> {result!r}')
        return result

    return wrapper

@trace
def fibonacci(n):
    if n in (0, 1):
        return n

    return (fibonacci(n - 1) + fibonacci(n - 2))


res = fibonacci(5)
print(res)

# Function don't know it's fibonacci debuging tools confuse, serializers dont work 
# Use functools
print(fibonacci)


from functools import wraps


def trace_2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        print(f'{func.__name__}({args!r}, {kwargs!r}) -> {result!r}')

        return result

    return wrapper

@trace_2
def fibonacci_2(n):
    if n in (0, 1):
        return n

    return (fibonacci(n - 1) + fibonacci(n - 2))

res = fibonacci_2(5)
print(res)

print(fibonacci_2)