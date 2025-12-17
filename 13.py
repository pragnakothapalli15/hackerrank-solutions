def print_door_mat(n, m):
    # Print the top half of the mat
    for i in range(1, n, 2):
        pattern = '.|.' * i
        print(pattern.center(m, '-'))
    
    # Print the welcome message
    print('WELCOME'.center(m, '-'))
    
    # Print the bottom half of the mat
    for i in range(n-2, -1, -2):
        pattern = '.|.' * i
        print(pattern.center(m, '-'))


def main():
    try:
        n, m = map(int, input().split())
        print_door_mat(n, m)
    except Exception as e:
        # Handle exception if needed
        pass


if __name__ == "__main__":
    main()