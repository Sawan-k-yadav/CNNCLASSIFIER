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
        if not os.path.exists(self.config.local_data_file):
            logger.info("Trying to download file")
            request.urlretrieve(
                url=self.config.Source_URL,
                filename=self.config.local_data_file
            )

        else:
            logger.info("file already exists")

    def get_updated_list_file(self, list_of_files):
        return [f for f in list_of_files if f.endswith(".jpg")]
        

    def preprocess(self,zf,f,working_dir):
        target_filepath=os.path.join(working_dir)
        if not os.path.exists(target_filepath):
            zf.extract(f, working_dir)

    def unzip_and_clean(self):
        with ZipFile(file=self.config.local_data_file, mode="r") as zf:
            list_of_file=zf.namelist()
            updated_list_of_file=self.get_updated_list_file(list_of_file)
            for f in tqdm(updated_list_of_file):
                self.preprocess()







