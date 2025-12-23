from collections import namedtuple

N = int(input())
fields = input().split()
Student = namedtuple('Student', fields)
students = [Student(*input().split()) for _ in range(N)]
print(f"{sum(int(s.MARKS) for s in students) / N:.2f}")