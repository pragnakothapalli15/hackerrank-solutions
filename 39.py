from itertools import groupby

def main():
    # Read input string
    s = input()

    # Group consecutive occurrences of characters
    groups = [(len(list(g)), int(k)) for k, g in groupby(s)]

    # Print the modified string
    print(' '.join(f'({count}, {num})' for count, num in groups))

if __name__ == "__main__":
    main()