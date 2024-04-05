from src.components.prediction import PredictionComponent
from src.config.config_manager import ConfigurationManager

import pandas as pd

class PredictionPipeline:
    """
    A class to execute a prediction pipeline.

    Attributes:
    data (pd.DataFrame): Input data for prediction.

    Methods:
    predict: Executes the prediction pipeline and returns the predictions.
    """
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def predict(self):
        config_obj = ConfigurationManager()
        prediction_config = config_obj.get_prediction_config()
        predict_component = PredictionComponent(config= prediction_config)
        prediction = predict_component.Make_prediction(data= self.data)
        return prediction