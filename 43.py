# Read the number of students subscribed to English newspaper
_ = input()
# Read roll numbers of students subscribed to English newspaper
english_subscribers = set(map(int, input().split()))

# Read the number of students subscribed to French newspaper
_ = input()
# Read roll numbers of students subscribed to French newspaper
french_subscribers = set(map(int, input().split()))

# Calculate total number of students with both subscriptions
common_subscribers = len(english_subscribers & french_subscribers)

print(common_subscribers)