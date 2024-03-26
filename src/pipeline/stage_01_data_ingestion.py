from src.components.data_ingestion import DataIngestionComponent
from src.utils.helper import read_yaml
from src.config.entity_config import DataIngestionConfig
from src.constants import CONFIG_FILE_PATH
from src.utils.exception import CustomException

import sys

class DataIngestionPipeline:
    def __init__(self, CONFIG_FILE_PATH):
        self.config = read_yaml(CONFIG_FILE_PATH)

    def main(self):
        try:
            config_obj = DataIngestionConfig(self.config)
            ingest_obj = DataIngestionComponent(config_obj)
            ingest_obj.extract_data() 
        except Exception as e:
            raise CustomException(e,sys)


if __name__ == "__main__":
    try:
        obj = DataIngestionPipeline(CONFIG_FILE_PATH=CONFIG_FILE_PATH)
        obj.main()

    except Exception as e:
        raise CustomException(e,sys)