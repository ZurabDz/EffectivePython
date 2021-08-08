# Note: At python 3.7 python dict has order guranteed but if speed is necessary
# better use DetfaultDict

from collections import defaultdict
from typing import Dict
from collections.abc import MutableMapping


def func(**kwargs):
    for key, val in kwargs.items():
        print(f'key: {key}, val" {val}')


# Consider Static Analysis via typing to Obviate Bugs
# sorted dict implementation
# python3 -m mypy --strict example.py


class SortedDict(MutableMapping):
    def __init__(self) -> None:
        super().__init__()
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    def __iter__(self):
        keys = list(self.data.keys())
        keys.sort()

        for key in keys:
            yield key

    def __len__(self) -> int:
        return len(self.data)


def some_function(votes: Dict[str, int]) -> None:
    pass


some_dict = SortedDict()
some_function(some_dict)

# Access elements from dict with get function
data = {}

counter = data.get('morph', 0)

# If you want to fetch data from dict otherwise set it to some defualt value can be used
# setdefault(key, default_value) method. Gotcha value is "moved"(like std::move) not copied
# better use defaultdict(for big objects)

# If you need to count elements collections module has Counter class for that

# Implementing custom defaultdict


class Visits:
    def __init__(self) -> None:
        self.data = defaultdict(set)

    def add(self, country, city):
        self.data[country].add(city)


visits = Visits()
visits.add('England', 'Bath')
visits.add('England', 'London')
print(visits.data)
# defaultdict(<class 'set'>, {'England': {'London', 'Bath'}})