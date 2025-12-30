from itertools import combinations

def main():
    # Read input
    s, k = input().split()
    k = int(k)

    # Generate and print combinations
    for r in range(1, k + 1):
        for combo in combinations(sorted(s), r):
            print(''.join(combo))

if __name__ == "__main__":
    main()