# Read the initial set size and elements
_ = input()
A = set(map(int, input().split()))

# Read the number of operations
N = int(input())

# Perform operations
for _ in range(N):
    op, _ = input().split()
    S = set(map(int, input().split()))
    getattr(A, op)(S)

# Print the sum of elements in the modified set
print(sum(A))