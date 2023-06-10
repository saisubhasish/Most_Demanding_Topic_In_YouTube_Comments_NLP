import sys
from etl.data_dump import Data_dump
from etl.scrapper import Data_scraper
from youtubeComments.exception import YoutubeCommentsException
from youtubeComments.logger import logging
from youtubeComments.config import DATABASE_NAME, COLLECTION_NAME

DATA_FILE_PATH="D:/FSDS-iNeuron/10.Projects-DS/Most_Demanding_Topic_In_YouTube_Comments_NLP/youtube_comments_scrapped.csv"
link = 'https://www.youtube.com/watch?v=fM4qTMfCoak&list=PLZoTAELRMXVMdJ5sqbCK2LiM0HhQVWNzm'
path = 'D:/FSDS-iNeuron/10.Projects-DS//YouTube_Comments/'


def start_data_pipeline():
    try:
        Data_scraper.scraper(link, path)
        Data_dump.dump(DATA_FILE_PATH, DATABASE_NAME, COLLECTION_NAME)

    except Exception as e:
        raise YoutubeCommentsException(e, sys)
