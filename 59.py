def custom_sort(s):
    return ''.join(sorted(s, key=lambda c: (c.isdigit(), c.isupper(), c.isdigit() and int(c) % 2 == 0, c)))

# Read input from STDIN
s = input().strip()

# Print output to STDOUT
print(custom_sort(s))