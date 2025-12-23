import math

AB = int(input())
BC = int(input())
angle = math.degrees(math.atan2(AB, BC))
print(f"{round(angle)}\u00b0")