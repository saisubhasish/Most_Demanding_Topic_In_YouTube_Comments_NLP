import pandas as pd
import nltk   # nltk is for natural language processing and computational linguistics
from nltk.corpus import stopwords   # corpus is a collection of authentic text or audio organized into datasets


from youtubeComments import utils

class NLP:
    @staticmethod
    def nlp_analysis(file_path):
        # Reading data

        '''df:pd.DataFrame  = utils.get_collection_as_dataframe(
                        database_name=self.data_ingestion_config.database_name, 
                        collection_name=self.data_ingestion_config.collection_name)'''

        df = pd.read_csv(file_path)

        # Perform analysis on the comments
        comments = df['0'].tolist()

        # Word Frequency Analysis with count
        utils.word_frequency_analysis(comments)

        # Sentiment Analysis
        utils.sentiment_analysis(comments)

        # Topic Modeling
        utils.topic_modeling(comments)