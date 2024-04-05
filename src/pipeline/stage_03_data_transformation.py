from src.components.data_transformation import DataTransformationComponent
from src.config.config_manager import ConfigurationManager


PHASE_NAME = ">>>>>>>>>>>>>> DATA TRANSFORMATION <<<<<<<<<<<<<<<<<<<"

class DataTransformationPipeline:
    """
    A class to execute a data transformation pipeline.

    Methods:
    main: Executes the data transformation pipeline.
    """
    
    def __init__(self):
        pass

    def main(self):
        transformation_config = ConfigurationManager()
        config = transformation_config.get_data_transformation_config()
        transformation_obj = DataTransformationComponent(config)
        transformation_obj.transform_data()




if __name__ == "__main__":
    obj  = DataTransformationPipeline()
    obj.main()
