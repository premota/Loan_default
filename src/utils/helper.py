from pathlib import Path
from box import Box
from typing import List
import os
import pickle
import json

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


def save_to_pickle(obj_path: Path, obj):
    try:
        dir_path = os.path.dirname(obj_path)
        os.makedirs(dir_path, exist_ok =True )
        with open(obj_path, 'wb') as file:
            pickle.dump(obj, file)
    except Exception as e:
        raise CustomException(e,sys)
    
def load_object(file_path: Path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        raise CustomException(e,sys)


def save_json(path: Path, data: dict):
    
    with open(path, "w") as f:
        json.dump(data, f, indent=4)




######### testing script

if __name__ == "__main__":
    d_path = Path(r"C:\Users\pc\Desktop\Dummy_projects\MLflow Loan default\config\config.yaml")
    output = read_yaml(d_path)
    print(output.artifacts_root)
