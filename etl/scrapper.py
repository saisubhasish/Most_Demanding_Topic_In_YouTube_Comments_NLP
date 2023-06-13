import sys
import time
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from youtubeComments.exception import YoutubeCommentsException
from youtubeComments.logger import logging

# Scrapper code 

class Data_scraper:
    @staticmethod
    def scraper(link, path, driver_path):
        """
        Description: This function scraps comments from youtube videos and stores it to a csv file
        =========================================================
        Params:
        link: link of the video
        path: path where file get saved
        =========================================================
        saves data to a csv file
        """
        
        try:
            # Creating a session and loading the page
            logging.info('Creating a session and loading the page')
            driver = webdriver.Chrome(driver_path)
            driver.get(link)

        except Exception as e:
            raise YoutubeCommentsException(e, sys)
            
        # Maximizing window
        driver.maximize_window()
        # wait time
        time.sleep(2)
        
        # Scrolling page to view comments
        driver.execute_script("window.scrollBy(0,500)","")
        time.sleep(3)
        
        driver.execute_script("window.scrollBy(0,2000)","")
        time.sleep(3)
        
        driver.execute_script("window.scrollBy(0,5000)","")
        time.sleep(3)
        
        driver.execute_script("window.scrollBy(0,5000)","")
        time.sleep(3)
        
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        
        driver.execute_script("window.scrollBy(0,2000)","")
        time.sleep(5)
        
        try:
            soup = BeautifulSoup(driver.page_source, "html.parser")
            # Find the comment sections
            # Getting all the comments with web elements
            comment_sections = soup.find_all("yt-formatted-string", class_="style-scope ytd-comment-renderer")
        except Exception as e:
            raise YoutubeCommentsException(e, sys)
            
        # Extract the comments
        # Removing the web elements
        comments = [comment.text.strip() for comment in comment_sections]
        
        # Saving the list of comments to a pandas dataframe
        df = pd.DataFrame(comments)
        
        
        # Printing each comment
        for comment in comments:
            print(comment)
            
            
        print(df)
        df.to_csv(f'{path}youtube_comments_scrapped.csv')

        # Cloding driver
        driver.quit()
            