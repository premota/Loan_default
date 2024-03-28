import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "Loan_default"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/__init__.py",
    f"src/components/__init__.py",
    f"src/utils/__init__.py",
    f"src/utils/helper.py",
    f"src/config/__init__.py",
    f"src/config/config_manager.py",
    f"src/config/entity_config.py",
    f"src/pipeline/__init__.py",
    f"src/constants/__init__.py",
    "config/config.yaml",
    "config/params.yaml",
    "dvc.yaml",
    "requirements.txt",
    "setup.py",
    "Notebook/trials.ipynb",
    "templates/index.html"


]



for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")