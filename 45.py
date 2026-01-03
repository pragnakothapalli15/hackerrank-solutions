# Read input integers
a = int(input().strip())
b = int(input().strip())
m = int(input().strip())

# Calculate and print results
print(pow(a, b))  # a^b
print(pow(a, b, m))  # a^b % m