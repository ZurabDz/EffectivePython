
# Variable scopes in function
def sort_priority3(numbers, group):
    '''
        using tuples to sort values with additional interest e.g 
        sort if elements where in group priority(1 where, 0 don't)
    '''
    found = False

    def helper(x):
        nonlocal found
        if x in group:
            found = True
            return (0, x)

        return (1, x)

    numbers.sort(key=helper)
    return found