from winetester.config.configuration import ConfigurationManger
from winetester.components.data_transformation import DataTransformation
from winetester import logger


STAGE_NAME = "Data Transformation Stage"


class DataTransformationTrainingPipeline():
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManger()
        data_transformation_config = config.get_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.train_test_split()
        
        
        
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
        
    except Exception as e:
        logger.exception(e)
        raise e
        
