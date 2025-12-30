import math
import os
import random
import re
import sys
from collections import Counter

if __name__ == '__main__':
    s = input().strip()
    
    # 1. Count frequency of each character
    counts = Counter(s)
    
    # 2. Convert to a list of items: [('a', 2), ('b', 3), ...]
    items = counts.items()
    
    # 3. Sort: 
    # Primary key: count (descending, hence -x[1])
    # Secondary key: character (ascending, hence x[0])
    sorted_items = sorted(items, key=lambda x: (-x[1], x[0]))
    
    # 4. Print the top 3
    for i in range(3):
        print(f"{sorted_items[i][0]} {sorted_items[i][1]}")