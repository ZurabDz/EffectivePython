
stock = {
    'nails': 125,
    'screws': 35,
    'wingnuts': 8,
    'washers': 24,
}

order = ['screws', 'wingnuts', 'clips']

def get_batches(count, size):
    return count // size


result = {name: batches for name in order
            if (batches := get_batches(stock.get(name, 0), 8))}