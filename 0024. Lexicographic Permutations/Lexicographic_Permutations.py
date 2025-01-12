
from itertools import permutations

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
perms = list(permutations(digits))

print(*perms[999999], sep="")
