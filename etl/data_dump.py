import sys
import json
import pymongo
import pandas as pd
from youtubeComments.exception import YoutubeCommentsException
from youtubeComments.logger import logging

from youtubeComments.config import mongo_client




class Data_dump:
    @staticmethod
    def dump(DATA_FILE_PATH, DATABASE_NAME, COLLECTION_NAME):
        """
        Description: This function takes Database_name and Collection_name, Data path as input, creqates database and collection in mongoDB and inserts data
        =========================================================
        Params:
        DATA_FILE_PATH: path where data is stored
        DATABASE_NAME: name for the database
        COLLECTION_NAME: name for the collection 
        =========================================================
        stores data in mongoDB
        """
        df = pd.read_csv(DATA_FILE_PATH)
        print(f"Rows and columns: {df.shape}")

        #Convert dataframe to json so that we can dump these record in mongo db
        logging.info('Convert dataframe to json so that we can dump these record in mongo db')
        df.reset_index(drop=True,inplace=True)

        # Each record will represent one row
        logging.info('Each record will represent one row')
        json_record = list(json.loads(df.T.to_json()).values())
        print(json_record[1])

        try:
            # Creating database
            logging.info('Creating database')
            mydb = mongo_client[DATABASE_NAME]

            # Creating collection
            logging.info('Creating collection')
            coll = mydb[COLLECTION_NAME]

            # insert converted json record to mongo db
            logging.info('insert converted json record to mongo db')
            coll.insert_many(json_record)

        except Exception as e:
            raise YoutubeCommentsException(e, sys)
