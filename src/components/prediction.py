from src.config.entity_config import PredictionConfig
from src.utils.logger import logging
from src.utils.helper import load_object

import pandas as pd

class  PredictionComponent:
    def __init__(self, config: PredictionConfig):
        self.config = config
        self.ordinal_map = self.config.ordinal_map


    def Make_prediction(self, data: pd.DataFrame):

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

