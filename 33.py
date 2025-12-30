def main():
    # Read input
    _ = input()
    set_a = set(map(int, input().split()))
    _ = input()
    set_b = set(map(int, input().split()))

    # Calculate symmetric difference
    symmetric_diff = set_a.symmetric_difference(set_b)

    # Print result in ascending order
    for num in sorted(symmetric_diff):
        print(num)

if __name__ == "__main__":
    main()