from src.config.config_manager import DataValidationConfig
from src.utils.exception import CustomException
from src.utils.logger import logging

import sys

import pandas as pd



class DataValidationComponent:
    """
    A class to perform data validation tasks.

    Attributes:
    config (DataValidationConfig): Configuration object containing validation parameters.

    Methods:
    validate_data: Validates data against a predefined schema and writes the validation status to a file.
    """

    def __init__(self, config: DataValidationConfig):
        self.config = config


    def validate_data(self) -> bool:
        """
        Validates data against a predefined schema and writes the validation status to a file.

        Returns:
        bool: True if data validation succeeds, False otherwise.

        Raises:
        CustomException: If an error occurs during data validation.
        """

        try:
            validation_status = True

            data = pd.read_csv(self.config.local_data_file)
            logging.info("reading columns of origin data")
            all_data_columns = data.columns.to_list()

            logging.info("Reading columns in Schema")
            all_schema_columns = self.config.data_schema.keys()

            for data_col in all_data_columns:
                if data_col not in all_schema_columns:
                    validation_status = False
                else:
                    pass
                
            with open(self.config.status_file, 'w') as status_file:
                status_file.write(f" VALIDATION STATUS: {validation_status}")
        
            logging.info("data validation completed")
            return validation_status
        
        except Exception as e:
            raise CustomException(e,sys)

