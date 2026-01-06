def sort_and_print_table():
    # Read number of rows and columns
    num_rows, num_cols = map(int, input().split())

    # Read table data
    table_data = [list(map(int, input().split())) for _ in range(num_rows)]

    # Read column index to sort by
    sort_index = int(input())

    # Sort table data based on the specified column
    sorted_data = sorted(table_data, key=lambda x: x[sort_index])

    # Print sorted table
    for row in sorted_data:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    sort_and_print_table()