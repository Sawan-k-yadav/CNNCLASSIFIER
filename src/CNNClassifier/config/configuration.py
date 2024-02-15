from CNNClassifier.utils.utils import read_yaml, create_directory
from CNNClassifier.entity.config_entity import DataIngestionConfig
from CNNClassifier.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from pathlib import Path
import os


class ConfigurationManager:
    def __init__(self,config_filepath = CONFIG_FILE_PATH, params_filepath = PARAMS_FILE_PATH):
        
        # Configuration of data ingestion
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directory([self.config.artifacts_root])



    def get_data_ingestion_config(self):
        config=self.config.data_ingestion
        create_directory([self.config.root_dir])
