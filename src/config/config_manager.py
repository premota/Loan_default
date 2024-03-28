from src.config.entity_config import DataIngestionConfig
from src.constants import *
from src.utils.helper import read_yaml
from src.utils.logger import logging

class ConfigurationManager:
    def __init__(self,
                 config_file_path = CONFIG_FILE_PATH,
                 params_file_path = PARAMS_FILE_PATH,
                 schema_file_path = SCHEMA_FILE_PATH): 
        
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path) 
        self.schema = read_yaml(schema_file_path) 
        
      
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        
        data_ingestion_config = DataIngestionConfig(
                root_dir = config.local_root_dir,
                source_url = config.source_url,
                local_data_file = config.local_data_file)
        
        
        return data_ingestion_config
