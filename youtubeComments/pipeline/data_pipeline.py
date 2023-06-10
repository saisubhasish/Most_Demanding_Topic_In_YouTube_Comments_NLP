import sys
from etl.data_dump import Data_dump
from etl.scrapper import Data_scraper
from youtubeComments.exception import YoutubeCommentsException
from youtubeComments.logger import logging



def start_data_pipeline(link, path, driver_path, DATA_FILE_PATH, DATABASE_NAME, COLLECTION_NAME):
    try:
        logging.info('Started scrapper code')
        Data_scraper.scraper(link, path, driver_path)

        logging.info('Started data dump code')
        Data_dump.dump(DATA_FILE_PATH, DATABASE_NAME, COLLECTION_NAME)

    except Exception as e:
        raise YoutubeCommentsException(e, sys)
