from collections import Counter
from textblob import TextBlob  # Assuming you have a sentiment analysis tool

def analyze_user_commands(user_commands):
    # Extracting topics from user commands
    topics = extract_topics(user_commands)

    # Analyzing sentiment distribution
    sentiment_distribution = analyze_sentiment(user_commands)

    return topics, sentiment_distribution

def extract_topics(user_commands):
    # Simple example: Extracting topics by splitting commands into words
    all_words = [word.lower() for command in user_commands for word in command.split()]
    topic_counter = Counter(all_words)
    
    # Get the most commonly mentioned topic
    most_common_topic = topic_counter.most_common(1)
    # print(most_common_topic)
    return most_common_topic[0][0] if most_common_topic else None

def analyze_sentiment(user_commands):
    # Simple example: Using TextBlob for sentiment analysis
    positive_comments = 0
    negative_comments = 0
    neutral_comments = 0

    for command in user_commands:
        analysis = TextBlob(command)

        # Classify sentiments as positive, negative, or neutral
        if analysis.sentiment.polarity > 0:
            positive_comments += 1
        elif analysis.sentiment.polarity < 0:
            negative_comments += 1
        else:
            neutral_comments += 1

    total_comments = len(user_commands)

    # Calculate percentages
    percentage_positive = (positive_comments / total_comments) * 100
    percentage_negative = (negative_comments / total_comments) * 100
    percentage_neutral = (neutral_comments / total_comments) * 100

    sentiment_distribution = {
        'Positive': percentage_positive,
        'Negative': percentage_negative,
        'Neutral': percentage_neutral
    }

    return sentiment_distribution

# Example Usage:
user_commands = [
    "I love the new update! The platform is amazing.",
    # "The customer service is terrible. They never respond to issues.",
    # "Great features, but the interface could be more user-friendly.",
    # "This platform is a lifesaver for my business.",
    # "The community support is fantastic. Everyone is helpful!",
    # "I'm really disappointed with the recent changes.",
    # "The app crashes every time I try to use it. Very frustrating.",
    # "Amazing job on the new features. Keep up the good work!",
    # "The platform is so slow. It takes forever to load pages.",
    # "I can't believe how easy it is to connect with others on this platform.",
    # "The latest update fixed all the problems I was experiencing. Thank you!",
    # "The design is outdated. It needs a modern look.",
    # "I'm addicted to this platform! Can't go a day without using it.",
    # "The algorithm for displaying content is not working well. I see irrelevant posts.",
    # "The user interface is intuitive and easy to navigate.",
    # "I hate the new feature. It's confusing and unnecessary.",
    # "This is the best social media platform I've ever used!",
    # "The security measures are not strong enough. Concerned about privacy.",
]

topics, sentiment_distribution = analyze_user_commands(user_commands)

print(f"Most commonly mentioned topic: {topics}")
print("Sentiment Distribution:")
for sentiment, percentage in sentiment_distribution.items():
    print(f"{sentiment}: {percentage:.2f}%")