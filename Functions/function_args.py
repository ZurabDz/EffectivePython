import json

def decode(data, default={}):
    try:
        return json.loads(data)
    except ValueError:
        return default

# Default directory will be shared for
# every call of function


def decode_right(data, default=None):
    if default is None:
        default = {}

    try:
        return json.loads(data)
    except ValueError:
        return default 

        
# Maybe add *args and **kwargs not sure how well I know it

# Enforcing keyword-only args for clearity
def safe_division_c(number, divisor, *, ingore_overflow=False, ignore_zero_division=False):
    pass

# Type error
# safe_division_c(1.0, 10**500, True, False)


# Positional only arguments python 3.8
#def safe_divisor_d(numerator, denominator, /, *, ingore_overflow=False, , ignore_zero_division=False):
#    pass


# Anything between / *, can be passed as keyword or by position