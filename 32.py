def calculate_happiness():
    # Read input
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    set_a = set(map(int, input().split()))
    set_b = set(map(int, input().split()))

    # Initialize happiness
    happiness = 0

    # Calculate happiness
    for num in array:
        if num in set_a:
            happiness += 1
        elif num in set_b:
            happiness -= 1

    # Print happiness
    print(happiness)

calculate_happiness()