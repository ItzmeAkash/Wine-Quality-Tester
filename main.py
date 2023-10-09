from winetester import logger
from winetester.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from winetester.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from winetester.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline


# Data ingestion Pipeline
STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    
except Exception as e:
    logger.exception(e)
    raise e


# Data Validation Pipeline


STAGE_NAME = "Data Validation Stage"


try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")


except Exception as e:
    logger.exception(e)
    raise e    

    
# Data Transformation Pipeline

STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_transformation =  DataTransformationTrainingPipeline()
    data_transformation.main()
 
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e    