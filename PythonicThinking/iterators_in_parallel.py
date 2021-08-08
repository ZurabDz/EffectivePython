# Use zip to Process Iterators in Parallel
import itertools


names = ['Cecilia', 'Lise', 'Marie']
counts = [len(n) for n in names]


longest_name = None
max_count = 0

# Beware both iterator should be exhausted at the same iteration
for name, count in zip(names, counts):
    if count > max_count:
        longest_name = name
        max_count = count

# File len(lines) should match or use zip_longest
with open('file1.in', 'r') as f1, open('file2.in', 'r') as f2:
    for f1_line, f2_line in zip(f1, f2):
        pass

names.append('Levan')


# Zip to longest and use None for first exhausted iterator
for name, count in itertools.zip_longest(names, counts):
    print(f'{name}: {count}')

