from itertools import product

# Read input from STDIN
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Compute cartesian product
AxB = list(product(A, B))

# Print output in sorted order
print(' '.join(map(str, AxB)))