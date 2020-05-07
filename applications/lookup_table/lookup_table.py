import math
import random

cache = {}

def slowfun(x, y):
    # TODO: Modify to produce the same results, but much faster
    # We want to store the power as our key
    # We want to store the factorial as our value (takes very long to compute)

    v = math.pow(x, y)

    if v not in cache:
        cache[v] = math.factorial(v)
        print('GIT CACHED')

        value = cache[v]
        value //= (x + y)
        value %= 982451653

        return value
    
    else:
        value = cache[v]
        value //= (x + y)
        value %= 982451653
        
        return value

# slowfun(2, 3)
# slowfun(3, 3)
# print(cache)


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
