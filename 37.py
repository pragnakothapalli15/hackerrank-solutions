from collections import OrderedDict

def main():
    # Read number of words
    n = int(input())

    # Initialize an ordered dictionary to store word counts
    word_counts = OrderedDict()

    # Read words and count occurrences
    for _ in range(n):
        word = input().strip()
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    # Print the number of distinct words
    print(len(word_counts))

    # Print the word counts
    print(' '.join(map(str, word_counts.values())))

if __name__ == "__main__":
    main()