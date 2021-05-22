import json
from itertools import permutations
# import enchant

# us_dict = enchant.Dict("en_US")

input_letters = ['d','a','d','t','y']

permutations_set = set()

for n in range(3,len(input_letters)):
    for y in list (permutations(input_letters,n)):
        z = "".join(y)
        permutations_set.add(z)

print(len(permutations_set))

