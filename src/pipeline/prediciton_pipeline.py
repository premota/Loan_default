from src.components.prediction import PredictionComponent
from src.config.config_manager import ConfigurationManager

import pandas as pd

class PredictionPipeline:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def predict(self):
        config_obj = ConfigurationManager()
        prediction_config = config_obj.get_prediction_config()
        predict_component = PredictionComponent(config= prediction_config)
        prediction = predict_component.Make_prediction(data= self.data)
        return prediction