# Read the number of test cases
T = int(input())

# Loop through each test case
for _ in range(T):
    # Read the size of set A (not used)
    _ = input()
    # Read set A
    A = set(map(int, input().split()))
    # Read the size of set B (not used)
    _ = input()
    # Read set B
    B = set(map(int, input().split()))

    # Check if A is a subset of B
    print(A.issubset(B))