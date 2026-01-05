def is_strict_superset(main_set, other_sets):
    """Check if main_set is a strict superset of all sets in other_sets"""
    for other_set in other_sets:
        if not main_set.issuperset(other_set) or main_set == other_set:
            return False
    return True

def main():
    # Read input from STDIN
    main_set = set(map(int, input().split()))
    num_other_sets = int(input())
    other_sets = [set(map(int, input().split())) for _ in range(num_other_sets)]

    # Check if main_set is a strict superset of all other sets
    result = is_strict_superset(main_set, other_sets)

    # Print result to STDOUT
    print(result)

if __name__ == "__main__":
    main()