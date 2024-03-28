from pathlib import Path
from box import Box
from dataclasses import dataclass


@dataclass(frozen=True)
class DataIngestionConfig:
    local_root_dir : Path
    source_url : str
    local_data_file : Path


@dataclass(frozen=True)
class DataValidationConfig:
    local_root_dir :Path
    status_file : str
    local_data_file : Path
    data_schema : dict

