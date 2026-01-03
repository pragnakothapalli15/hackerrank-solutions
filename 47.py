# Read input
n_english = int(input().strip())
english_subscribers = set(map(int, input().strip().split()))
n_french = int(input().strip())
french_subscribers = set(map(int, input().strip().split()))

# Calculate the number of students subscribed to only English newspaper
only_english = english_subscribers.difference(french_subscribers)

# Print the result
print(len(only_english))