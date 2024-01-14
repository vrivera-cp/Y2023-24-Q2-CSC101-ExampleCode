"""importing.py
An example showing different ways to import built-in libraries.
"""

import math
from random import randint
from time import *  # imports the ctime function

result = math.sin(math.pi / 2.0)
print(result)

print(randint(0, 10))

print(ctime())
