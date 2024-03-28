from pathlib import Path
from box import Box
from typing import List
import os

import yaml
import sys

from src.utils.logger import logging
from src.utils.exception import CustomException




def read_yaml(path: Path) -> Box:
    try:
        with open(path) as y_file:
            data = yaml.safe_load(y_file)
            logging.info(f"Reading {path} yaml file")
            return Box(data)
    except Exception as e:
        raise CustomException(e,sys)
    

def create_folder(folder_path: List, verbose =True):
    for path in folder_path:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logging.info(f"created a directory at {path}")

######### testing script

if __name__ == "__main__":
    d_path = Path(r"C:\Users\pc\Desktop\Dummy_projects\MLflow Loan default\config\config.yaml")
    output = read_yaml(d_path)
    print(output.artifacts_root)
