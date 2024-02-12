import re
from collections import Counter
from textblob import TextBlob
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

def analyze_comments(comments):
    # Preprocessing
    cleaned_comments = preprocess_comments(comments)
    
    # Keyword Extraction
    keywords = extract_keywords(cleaned_comments)
    
    # Sentiment Analysis
    sentiment_distribution = analyze_sentiment(cleaned_comments)
    
    return keywords, sentiment_distribution

def preprocess_comments(comments):
    cleaned_comments = []
    stop_words = set(stopwords.words('english'))
    for comment in comments:
        # Remove special characters and links
        cleaned_comment = re.sub(r'http\S+', '', comment)
        cleaned_comment = re.sub(r'[^a-zA-Z\s]', '', cleaned_comment)
        # Convert to lowercase and remove stopwords
        cleaned_comment = ' '.join(word for word in cleaned_comment.lower().split() if word not in stop_words)
        cleaned_comments.append(cleaned_comment)
    return cleaned_comments

def extract_keywords(comments):
    tfidf_vectorizer = TfidfVectorizer(max_features=1000)
    tfidf_matrix = tfidf_vectorizer.fit_transform(comments)
    feature_names = tfidf_vectorizer.get_feature_names_out()
    word_scores = tfidf_matrix.sum(axis=0).A1
    word_scores_dict = {feature_names[i]: word_scores[i] for i in range(len(feature_names))}
    top_keywords = Counter(word_scores_dict).most_common(10)  # Get top 10 keywords
    return top_keywords

def analyze_sentiment(comments):
    sentiments = [TextBlob(comment).sentiment.polarity for comment in comments]
    positive_count = sum(1 for sentiment in sentiments if sentiment > 0)
    negative_count = sum(1 for sentiment in sentiments if sentiment < 0)
    neutral_count = sum(1 for sentiment in sentiments if sentiment == 0)
    total_comments = len(comments)
    positive_percentage = (positive_count / total_comments) * 100
    negative_percentage = (negative_count / total_comments) * 100
    neutral_percentage = (neutral_count / total_comments) * 100
    sentiment_distribution = {'Positive': positive_percentage, 'Negative': negative_percentage, 'Neutral': neutral_percentage}
    return sentiment_distribution

# Example usage
comments = ["I love this product! It's amazing.", "I hate waiting for deliveries.", "This service is okay, nothing special."]
keywords, sentiment_distribution = analyze_comments(comments)
print("Top Keywords:", keywords)
print("Sentiment Distribution:", sentiment_distribution)
