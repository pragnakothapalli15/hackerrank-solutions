from collections import deque

def main():
    # Read number of operations
    n = int(input())

    # Initialize an empty deque
    d = deque()

    # Perform operations
    for _ in range(n):
        command = input().split()
        if command[0] == 'append':
            d.append(int(command[1]))
        elif command[0] == 'appendleft':
            d.appendleft(int(command[1]))
        elif command[0] == 'pop':
            d.pop()
        elif command[0] == 'popleft':
            d.popleft()

    # Print the elements of the deque
    print(' '.join(map(str, d)))

if __name__ == "__main__":
    main()