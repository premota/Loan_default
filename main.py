from src.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.pipeline.stage_02_data_validation import DataValidationPipeline
from src.pipeline.stage_03_data_transformation import DataTransformationPipeline
from src.pipeline.stage_04_model_training import ModelTrainingPipeline
from src.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline
from src.utils.logger import logging
from src.utils.exception import CustomException

import sys


PHASE_NAME = "Data Ingestion phase"
try:
    logging.info(f">>>>>>>> {PHASE_NAME} about to begin <<<<<<<<<<<<<<<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logging.info(f">>>>>>>> {PHASE_NAME} completed <<<<<<<<<<<<<<<<<\n\nx==========x")
except Exception as e:
    raise CustomException(e,sys)




PHASE_NAME = "Data Validation phase"
try:
    logging.info(f">>>>>>>> {PHASE_NAME} about to begin <<<<<<<<<<<<<<<<<")
    obj = DataValidationPipeline()
    obj.main()
    logging.info(f">>>>>>>> {PHASE_NAME} completed <<<<<<<<<<<<<<<<<\n\nx==========x")
except Exception as e:
    raise CustomException(e,sys)




PHASE_NAME = "Data Transformation phase"
try:
    logging.info(f">>>>>>>> {PHASE_NAME} about to begin <<<<<<<<<<<<<<<<<")
    obj  = DataTransformationPipeline()
    obj.main()
    logging.info(f">>>>>>>> {PHASE_NAME} completed <<<<<<<<<<<<<<<<<\n\nx==========x")

except Exception as e:
    raise CustomException(e,sys)




PHASE_NAME = "Model Training phase"
try:
    logging.info(f">>>>>>>> {PHASE_NAME} about to begin <<<<<<<<<<<<<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logging.info(f">>>>>>>> {PHASE_NAME} completed <<<<<<<<<<<<<<<<<\n\nx==========x")
except Exception as e:
    raise CustomException(e, sys)



PHASE_NAME = "Model Evaluation phase"

try:
    logging.info(f">>>>>>>> {PHASE_NAME} about to begin <<<<<<<<<<<<<<<<<")
    obj = ModelEvaluationPipeline()
    obj.main()
    logging.info(f">>>>>>>> {PHASE_NAME} completed <<<<<<<<<<<<<<<<<\n\nx==========x")
except Exception as e:
    raise CustomException(e,sys)