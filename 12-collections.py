from collections import defaultdict
from collections import Counter
from collections import deque
from collections import namedtuple
from enum import Enum
import json

tree = lambda: defaultdict(tree)
some_dict = defaultdict(tree)
some_dict['colours']['favourite'] = "yellow"
print(json.dumps(some_dict))

colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

favourite_colours = defaultdict(list)

for name, colour in colours:
    favourite_colours[name].append(colour)

print(favourite_colours)

favs = Counter(name for name, colour in colours)
print(favs)

# output
# defaultdict(<type 'list'>,
#    {'Arham': ['Green'],
#     'Yasoob': ['Yellow', 'Red'],
#     'Ahmed': ['Silver'],
#     'Ali': ['Blue', 'Black']
# })

colours =  {"Green" : 170, "Red" : 198, "Blue" : 160}
for key, value in colours.items():
    print(key, value)
    
d = deque()
d.append('1')
d.append('2')
d.append('3')

print(len(d))
# Output: 3

print(d[0])
# Output: '1'

print(d[-1])
# Output: '3'

d = deque(range(5))

print(d[0])
# Output: '0'

print(d[-1])
# Output: '4'

print(d.popleft())
# Output: '0'

print(d.popleft())
# Output: '0'

print(d.pop())
# Output: '0'

print(d)
# Output: deque([2, 3])

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="perry", age=31, type="cat")

print(perry)
# Output: Animal(name='perry', age=31, type='cat')

print(perry.name)
# Output: 'perry'

class Species(Enum):
    cat = 1
    dog = 2
    horse = 3
    aardvark = 4
    butterfly = 5
    owl = 6
    platypus = 7
    dragon = 8
    unicorn = 9
    # The list goes on and on...

    # But we don't really care about age, so we can use an alias.
    kitten = 1
    puppy = 2
    
perry = Animal(name="Perry", age=31, type=Species.cat)
drogon = Animal(name="Drogon", age=4, type=Species.dragon)
tom = Animal(name="Tom", age=75, type=Species.cat)
charlie = Animal(name="Charlie", age=2, type=Species.kitten)

print(charlie)