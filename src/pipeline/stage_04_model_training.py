from src.components.model_trainer import ModelTrainerComponent
from src.config.config_manager import ConfigurationManager


PHASE_NAME = ">>>>>>>>>>> MODEL TRAINING PHASE <<<<<<<<<<<<<<"

class ModelTrainingPipeline:
    """
    A class to execute a model training pipeline.

    Methods:
    main: Executes the model training pipeline.
    """
    
    def __init__(self):
        pass

    def main(self):
        config_obj = ConfigurationManager()
        config = config_obj.get_model_trainer_config()
        model_training_component = ModelTrainerComponent(config=config)
        model_training_component.train_model()




if __name__ == "__main__":
    obj = ModelTrainingPipeline()
    obj.main()