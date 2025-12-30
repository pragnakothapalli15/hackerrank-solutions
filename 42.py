import itertools

n = int(input())
letters = input().split()
k = int(input())

total_combinations = list(itertools.combinations(range(n), k))
a_combinations = [c for c in total_combinations if any(letters[i] == 'a' for i in c)]

probability = len(a_combinations) / len(total_combinations)
print(f'{probability:.3f}')