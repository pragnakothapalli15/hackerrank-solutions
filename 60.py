def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# Read the number of test cases
n = int(input())

# Process each test case
for _ in range(n):
    s = input().strip()
    print(is_float(s))