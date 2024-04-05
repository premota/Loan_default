from src.config.entity_config import PredictionConfig
from src.utils.logger import logging
from src.utils.helper import load_object
from src.utils.exception import CustomException

import pandas as pd
import sys


class  PredictionComponent:
    """
    A class to make predictions using a trained machine learning model.

    Attributes:
    config (PredictionConfig): Configuration object containing prediction parameters.
    ordinal_map (dict): Mapping of ordinal categorical features to numerical values.

    Methods:
    Make_prediction: Makes predictions on input data using a trained model and transformation pipeline.
    """

    def __init__(self, config: PredictionConfig):
        self.config = config
        self.ordinal_map = self.config.ordinal_map


    def Make_prediction(self, data: pd.DataFrame):
        """
        Makes predictions on input data using a trained model and transformation pipeline.

        Args:
        data (pd.DataFrame): Input data for prediction.

        Returns:
        array: Predicted labels.

        Raises:
        CustomException: If an error occurs during prediction.
        """
        try:
            logging.info("Transforming oridinal categorical features")
            # Replace your ordinal categorical feature with encoded values using the custom mapping
            data['Grade'] = data['Grade'].map(self.ordinal_map.grade_map)
            data['Sub Grade'] = data['Sub Grade'].map(self.ordinal_map.subgrade_map)
            data['Verification Status'] = data['Verification Status'].map(self.ordinal_map.verification_status_map)

            # load transformer object and model 
            logging.info("loading transformer and model object")
            transformer = load_object(file_path= self.config.transfomer_path)
            model = load_object(file_path= self.config.model_path)

            logging.info("Transforming categorical features with transformer object")
            transformed_df = transformer.transform(data)

            logging.info("Making prediction")
            y_pred = model.predict(transformed_df)

            return y_pred
        
        except Exception as e:
            raise CustomException(e,sys)

