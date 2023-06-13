from youtubeComments.pipeline.data_pipeline import start_data_pipeline
from youtubeComments.config import DATABASE_NAME, COLLECTION_NAME
from youtubeComments.config import driver_path
from youtubeComments.pipeline.nlp_pipeline import start_nlp_pipeline

DATA_FILE_PATH="D:/FSDS-iNeuron/10.Projects-DS/Most_Demanding_Topic_In_YouTube_Comments_NLP/youtube_comments_scrapped.csv"
link = 'https://www.youtube.com/watch?v=fM4qTMfCoak&list=PLZoTAELRMXVMdJ5sqbCK2LiM0HhQVWNzm'
path = 'D:/FSDS-iNeuron/10.Projects-DS//YouTube_Comments/'



if __name__=='__main__':
    start_data_pipeline(link, path, driver_path, DATA_FILE_PATH, DATABASE_NAME, COLLECTION_NAME)
    start_nlp_pipeline()