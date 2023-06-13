import os
import sys
import pandas as pd
from youtubeComments.config import mongo_client
from youtubeComments.logger import logging
from youtubeComments.exception import YoutubeCommentsException

import nltk   # nltk is for natural language processing and computational linguistics
from nltk.corpus import stopwords   # corpus is a collection of authentic text or audio organized into datasets
from nltk.sentiment import SentimentIntensityAnalyzer    # To analyse sentiment
from sklearn.feature_extraction.text import CountVectorizer    # method to convert text to numerical data
from sklearn.decomposition import LatentDirichletAllocation    # explains a set of observations through unobserved groups, and each group explains why some parts of the data are similar

def get_collection_as_dataframe(database_name:str,collection_name:str)->pd.DataFrame:
    """
    Description: This function return collection as dataframe
    =========================================================
    Params:
    database_name: database name
    collection_name: collection name
    =========================================================
    return Pandas dataframe of a collection
    """
    try:    
        logging.info(f"Reading data from database: {database_name} and collection: {collection_name}")
        df = pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
        logging.info(f"Found columns: {df.columns}")
        if "_id" in df.columns:
            logging.info(f"Dropping column: _id ")
            df = df.drop("_id",axis=1)
        logging.info(f"Row and columns in df: {df.shape}")
        return df
    except Exception as e:
        raise YoutubeCommentsException(e, sys)
    

nltk.download('stopwords')     # used to eliminate unimportant words (commonly used words)
nltk.download('punkt')    # a tokenizer that divides a text into a list of sentences by using an unsupervised algorithm to build a model for abbreviation words, collocations, and words that start sentences.
nltk.download('vader_lexicon')    # is a lexicon and rule-based sentiment analysis tool that is specifically attuned to sentiments expressed in social media, and works well on texts from other domains.

# Preprocess the comments o remove the unwanted words

stop_words = set(stopwords.words('english'))
    
def word_frequency_analysis(comments):
    """
    This function prints frequency of each word in a descending order
    """
    # Convert comments to strings and handle float values
    comments = [str(comment) if not pd.isnull(comment) else '' for comment in comments]

    # Combine all comments into a single string
    all_comments = ' '.join(comments)

    # Tokenize the comments
    tokens = nltk.word_tokenize(all_comments)

    # Filter out stopwords
    filtered_tokens = [token for token in tokens if token.lower() not in stop_words]

    # Calculate word frequencies
    word_freq = nltk.FreqDist(filtered_tokens)

    # Print the most common words
    print('Most common words:')
    for word, freq in word_freq.most_common(10):
        print(f'{word}: {freq}')

def sentiment_analysis(comments):
    """
    This function prints the over all sentiment of the text
    """
    sid = SentimentIntensityAnalyzer()

    # Calculate sentiment scores for each comment
    sentiment_scores = [sid.polarity_scores(comment) for comment in comments]

    # Calculate average sentiment scores
    avg_sentiment = sum(score['compound'] for score in sentiment_scores) / len(sentiment_scores)

    print(f'Average sentiment: {avg_sentiment}')

def topic_modeling(comments):
    """
    This function prints the most discussed topics in the comments
    """
    # Create a CountVectorizer object
    tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2, stop_words='english')
    
    # Fit and transform the comments
    tf = tf_vectorizer.fit_transform(comments)
    
    # Create an LDA model
    lda = LatentDirichletAllocation(n_components=5, random_state=42)
    
    # Fit the LDA model
    lda.fit(tf)
    
    # Print the top words for each topic
    print('Top words per topic:')
    feature_names = tf_vectorizer.get_feature_names_out()
    for topic_idx, topic in enumerate(lda.components_):
        top_words = [feature_names[i] for i in topic.argsort()[:-10 - 1:-1]]
        print(f"Topic {topic_idx+1}: {' '.join(top_words)}")