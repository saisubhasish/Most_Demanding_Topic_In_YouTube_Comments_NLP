import json
import pymongo
import pandas as pd
from youtubeComments.exception import YoutubeCommentsException
from youtubeComments.logger import logging
from youtubeComments.config import DATABASE_NAME, COLLECTION_NAME
from youtubeComments.config import mongo_client

DATA_FILE_PATH="D:/FSDS-iNeuron/10.Projects-DS/Most_Demanding_Topic_In_YouTube_Comments_NLP/youtube_comments_scrapped.csv"


class Data_scraper:
    @staticmethod
    def scraper(DATA_FILE_PATH, DATABASE_NAME, COLLECTION_NAME):
        df = pd.read_csv(DATA_FILE_PATH)
        print(f"Rows and columns: {df.shape}")

        #Convert dataframe to json so that we can dump these record in mongo db
        df.reset_index(drop=True,inplace=True)

        # Each record will represent one row
        json_record = list(json.loads(df.T.to_json()).values())
        print(json_record[1])

        # Creating database
        mydb = mongo_client[DATABASE_NAME]

        # Creating collection
        coll = mydb[COLLECTION_NAME]

        #insert converted json record to mongo db
        coll.insert_many(json_record)


if __name__ == '__main__':
    Data_scraper.scraper(DATA_FILE_PATH, DATABASE_NAME, COLLECTION_NAME)