from src.components.data_ingestion import DataIngestionComponent
from src.utils.exception import CustomException
from src.config.config_manager import ConfigurationManager

import sys

PHASE_NAME = "Data Ingestion phase"

class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config_obj = ConfigurationManager()
            ingestion_config = config_obj.get_data_ingestion_config()
            component = DataIngestionComponent(config=ingestion_config)
            component.extract_data()
        except Exception as e:
            raise CustomException(e,sys)


if __name__ == "__main__":
    try:
        obj = DataIngestionPipeline()
        obj.main()

    except Exception as e:
        raise CustomException(e,sys)