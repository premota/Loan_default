from pathlib import Path
from box import Box
from dataclasses import dataclass


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir : Path
    source_url : str
    local_data_file : Path


@dataclass(frozen=True)
class DataValidationConfig:
    root_dir :Path
    status_file : str
    local_data_file : Path
    data_schema : dict

