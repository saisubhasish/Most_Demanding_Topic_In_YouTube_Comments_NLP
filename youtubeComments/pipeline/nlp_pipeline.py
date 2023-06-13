from youtubeComments.nlp import NLP
from youtubeComments.config import file_path


def start_nlp_pipeline():
    NLP.nlp_analysis(file_path)