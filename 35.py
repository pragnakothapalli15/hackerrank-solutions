def main():
    # Read number of stamps
    n = int(input())

    # Initialize a set to store unique country stamps
    country_stamps = set()

    # Read country stamps
    for _ in range(n):
        country = input().strip()
        country_stamps.add(country)

    # Print the total number of distinct country stamps
    print(len(country_stamps))

if __name__ == "__main__":
    main()