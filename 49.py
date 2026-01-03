# Read input
n_english = int(input().strip())
english_subscribers = set(map(int, input().strip().split()))
n_french = int(input().strip())
french_subscribers = set(map(int, input().strip().split()))

# Calculate the number of students subscribed to either English or French but not both
either_but_not_both = english_subscribers.symmetric_difference(french_subscribers)

# Print the result
print(len(either_but_not_both))