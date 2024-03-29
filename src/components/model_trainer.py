from src.config.config_manager import ModelTrainerConfig
from src.utils.logger import logging
from src.utils.helper import save_to_pickle
from src.utils.exception import CustomException

from xgboost import XGBClassifier as xgb_clf
import pandas as pd

import sys


class ModelTrainerComponent:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train_model(self):
        try:
            train_data = pd.read_csv(self.config.train_data)

            # Create X and y variable
            X_train = train_data.drop([self.config.Target], axis =1)
            y_train = train_data[self.config.Target]

            # fit and save model
            logging.info("Fitting model to Data")
            clf = xgb_clf(**self.config.params)
            clf.fit(X_train, y_train)

            logging.info("model training complete")

            save_to_pickle(obj_path=self.config.model_pickle_file, obj=clf)
            logging.info(f"model has been saved to {self.config.local_root_dir}")
        
        except Exception as e:
            raise CustomException(e,sys)



        
