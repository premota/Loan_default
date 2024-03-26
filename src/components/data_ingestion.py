import os
import sys
import gdown

from src.utils.logger import logging
from src.config.entity_config import DataIngestionConfig
from src.utils.exception import CustomException

from pathlib import Path
from src.utils.helper import read_yaml



class DataIngestionComponent:
    def __init__(self, config: DataIngestionConfig):
         self.config = config

    
    def extract_data(self):
        try:
            prefix = "https://drive.google.com/uc?/export=download&id="
            url = self.config.source_url
            data_path = self.config.local_data_file
            data_root_dir = self.config.root_dir
            os.makedirs(data_root_dir, exist_ok= True)

            file_id = url.split("/")[-2]
            logging.info(f"Downloading data from {url}")
            gdown.download(prefix + file_id, data_path)
            logging.info(f"Downloaded data from {url}")

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    d_path = Path(r"C:\Users\pc\Desktop\Dummy_projects\MLflow Loan default\config\config.yaml")
    output = read_yaml(d_path)
    obj = DataIngestionConfig(output)
    ingest_obj = DataIngestionComponent(obj)
    ingest_obj.extract_data()