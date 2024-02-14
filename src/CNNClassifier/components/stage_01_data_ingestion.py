import os
import urllib.request as request  # For doing any request to the server
from zipfile import ZipFile
from CNNClassifier import logger
from pathlib import Path
from tqdm import tqdm   #-- Used for showing prgress bar of any process
from CNNClassifier.entity import DataIngestionConfig
from CNNClassifier.utils import utils

class DataIngestion:
    def __init__(self,config=DataIngestionConfig):
        # whatever configuration I will have in config.yaml, we will keep it here
        self.config=config            

    def download_file(self):
        pass

    def get_updated_list_file(self):
        pass







