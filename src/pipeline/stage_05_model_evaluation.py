from src.components.model_evaluation import ModelEvaluationComponent
from src.config.config_manager import ConfigurationManager



class ModelEvaluationPipeline:
    """
    A class to execute a model evaluation pipeline.

    Methods:
    main: Executes the model evaluation pipeline.
    """
    
    def __init__(self):
        pass

    def main(self):
        config_obj = ConfigurationManager()
        config = config_obj.get_model_evaluation_config()
        model_eval_component_obj = ModelEvaluationComponent(config=config)
        model_eval_component_obj.evaluate_model()



if __name__ == "__main__":
    obj = ModelEvaluationPipeline()
    obj.main()