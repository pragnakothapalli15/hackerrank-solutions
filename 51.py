from collections import Counter

K = int(input())
print(Counter(input().split()).most_common()[-1][0])