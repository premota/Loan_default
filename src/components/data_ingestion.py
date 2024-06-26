import os
import sys
import gdown

from src.utils.logger import logging
from src.config.entity_config import DataIngestionConfig
from src.utils.exception import CustomException



class DataIngestionComponent:
    """
    A class to handle data ingestion tasks.

    Attributes:
    config (DataIngestionConfig): Configuration object containing data ingestion parameters.

    Methods:
    extract_data: Downloads data from a specified URL and saves it locally.
    """

    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def extract_data(self):
        """
        Downloads data from a specified URL and saves it locally.
        """

        try:
            prefix = "https://drive.google.com/uc?/export=download&id="
            url = self.config.source_url
            data_path = self.config.local_data_file

            file_id = url.split("/")[-2]
            logging.info(f"Downloading data from {url}") 
            gdown.download(prefix + file_id, data_path)
            logging.info(f"Downloaded data from {url}")

        except Exception as e:
            raise CustomException(e, sys)
  

