from pathlib import Path
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


@dataclass(frozen=True)
class DataTransformationConfig:
    local_root_dir : Path
    pickle_file : Path
    local_data_file: Path
    ordinal_map : dict
    Target : str
    train_data: Path
    test_data: Path

@dataclass(frozen=True)
class ModelTrainerConfig:
    local_root_dir: Path
    train_data: Path
    model_pickle_file: Path
    params: dict
    Target: str

@dataclass(frozen =True)
class ModelEvaluationConfig:
    local_root_dir: Path
    test_data_path: Path
    model_path: Path
    metric_file_name: Path
    params : dict
    Target : str
    
