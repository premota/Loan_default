from src.config.config_manager import ModelEvaluationConfig
from src.utils.logger import logging
from src.utils.exception import CustomException
from src.utils.helper import load_object, save_json

import sys
from pathlib import Path

import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score




class ModelEvaluationComponent:
    def __init__(self,config: ModelEvaluationConfig):
        self.config = config


    def evaluate_model(self):
        try:
            logging.info("reading test data and saved model")
            test_data = pd.read_csv(self.config.test_data_path)
            model = load_object(file_path= Path(self.config.model_path))
    
            logging.info("split into train and test")
            # split test data to x and y
            X_test = test_data.drop([self.config.Target], axis=1)
            y_test = test_data[self.config.Target]

            logging.info("Make predictions")
            y_pred = model.predict(X_test)

            logging.info("Evaluate model")
            accuracy = accuracy_score(y_test, y_pred)
            precision = precision_score(y_test, y_pred)
            recall = recall_score(y_test, y_pred)
            f1 = f1_score(y_test, y_pred)

            # save result in json file
            result = {
                "accuracy" : accuracy,
                "precision": precision,
                "recall": recall,
                "f1": f1
            }

            save_json(Path(self.config.metric_file_name), result)

            logging.info(f"model has accuracy of {accuracy}, precision of {precision}, recall of {recall} and f1 of {f1}")

            logging.info("logging information in MLFlow")

            mlflow.set_experiment("Loan_default")

            with mlflow.start_run():
                mlflow.log_params(self.config.params)
                mlflow.log_metric("Accuracy", accuracy)
                mlflow.log_metric("precision", precision)
                mlflow.log_metric("recall", recall)
                mlflow.log_metric("f1", f1)

            mlflow.end_run()

        except Exception as e:
            raise CustomException(e,sys)


        
