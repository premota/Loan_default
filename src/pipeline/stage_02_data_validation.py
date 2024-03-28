from src.config.config_manager import ConfigurationManager
from src.components.data_validation import DataValidationComponent
from src.utils.logger import logging
from src.utils.helper import CustomException


import sys


PHASE_NAME = "Data validation phase"

class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
        logging.info("Data validation about to begin")
        config = ConfigurationManager()
        validation_config = config.get_data_validation()

        validation_component = DataValidationComponent(validation_config)
        validation_component.validate_data()


if __name__ == "__main__":
    try:
        obj = DataValidationPipeline()
        obj.main()
    
    except Exception as e:
        raise CustomException(e,sys)