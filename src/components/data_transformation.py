from src.config.config_manager import DataTransformationConfig
from src.utils.logger import logging
from src.utils.helper import save_to_pickle
from src.utils.helper import CustomException

import sys

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
import pandas as pd



class DataTransformationComponent:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.ordinal_map = self.config.ordinal_map
        self.target = self.config.Target

    def transform_data(self, target = True):
        try:
            data_frame = pd.read_csv(self.config.local_data_file)
            data = data_frame.drop([self.target], axis =1)

            logging.info("Transforming oridinal categorical features")
            # Replace your ordinal categorical feature with encoded values using the custom mapping
            data['Grade'] = data['Grade'].map(self.ordinal_map.grade_map)
            data['Sub Grade'] = data['Sub Grade'].map(self.ordinal_map.subgrade_map)
            data['Verification Status'] = data['Verification Status'].map(self.ordinal_map.verification_status_map)

            logging.info("Finised encoding ordinal features")


            numerical_features = data.select_dtypes(exclude = "object").columns.to_list()
            categorical_features = data.select_dtypes(include = "object").columns.to_list()
            
            # Transformers
            numerical_transformer = StandardScaler()
            categorical_transformer = OneHotEncoder(drop = 'if_binary')
            
            logging.info("Creating sklearn transformer pipeline")
            pipeline = ColumnTransformer(
            [
            ( "numerical transformer", numerical_transformer, numerical_features),
                ("categorical transformer", categorical_transformer, categorical_features)
            ])
            
            # apply transformer
            transformed_array = pipeline.fit_transform(data)

            logging.info(f"Transformation completed, saving transformation object as pickle file to {self.config.pickle_file}")
            save_to_pickle(self.config.pickle_file, pipeline)
            
            # Get the transformed column names
            transformed_numerical_columns = pipeline.transformers_[0][2]
            transformed_categorical_columns = pipeline.transformers_[1][1].get_feature_names_out(input_features=categorical_features)
            
            # Combine numerical and categorical transformed column names
            transformed_columns = list(transformed_numerical_columns) + list(transformed_categorical_columns)
            
            # convert array to dataframe
            transformed_data = pd.DataFrame(transformed_array, columns=transformed_columns)
            
            
            # attach target feature
            transformed_data[self.target] = data_frame[self.target]
            logging.info(f"transformated dataset has dimension of {transformed_data.shape}")

            #perform train-test split
            train_df, test_df = train_test_split(transformed_data, test_size= 0.3, stratify= transformed_data[self.target])
            train_df.to_csv(self.config.train_data, index = False)
            test_df.to_csv(self.config.test_data, index = False)

            logging.info(f"train data size is: {train_df.shape}, test data size is: {test_df.shape}")
            logging.info(f"Train and test data is saved at {self.config.local_root_dir}")

        except Exception as e:
            raise CustomException(e,sys)