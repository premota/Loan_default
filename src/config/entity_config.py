from pathlib import Path
from box import Box


class DataIngestionConfig:
    """
    Configures data ingestion parameters.

    Args:
        config (Box): Box object containing configuration details.

    Attributes:
        root_dir (str): Local root directory for data storage.
        source_url (str): URL of the data source.
        local_data_file (str): Local data file path.
    """
    def __init__(self, config: Box) -> None:
        data_ingestion_config  = config.data_ingestion
        self.root_dir = data_ingestion_config.local_root_dir
        self.source_url = data_ingestion_config.source_url
        self.local_data_file = data_ingestion_config.local_data_file
