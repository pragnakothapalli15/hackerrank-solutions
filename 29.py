try:
    T = int(input())
    for _ in range(T):
        a, b = input().split()
        try:
            print(int(a) // int(b))
        except ZeroDivisionError as e:
            print(f"Error Code: {e}")
        except ValueError as e:
            print(f"Error Code: {e}")
except Exception as e:
    pass