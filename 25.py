from itertools import permutations

# Read input
string, size = input().split()
size = int(size)

# Generate permutations
perms = permutations(sorted(string), size)

# Print permutations
for perm in perms:
    print(''.join(perm))