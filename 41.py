# Read the number of students subscribed to English newspaper
_ = input()
# Read roll numbers of students subscribed to English newspaper
english_subscribers = set(map(int, input().split()))

# Read the number of students subscribed to French newspaper
_ = input()
# Read roll numbers of students subscribed to French newspaper
french_subscribers = set(map(int, input().split()))

# Calculate total number of students with at least one subscription
total_subscribers = len(english_subscribers.union(french_subscribers))

print(total_subscribers)