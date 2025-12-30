from itertools import combinations_with_replacement

def main():
    # Read input
    s, k = input().split()
    k = int(k)

    # Generate combinations with replacement
    s = sorted(s)
    for combo in combinations_with_replacement(s, k):
        print(''.join(combo))

if __name__ == "__main__":
    main()