from mlflow_project import logger
from mlflow_project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlflow_project.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

STAGE_NAME = "Data Ingestion stage"
try :
    logger.info(f" Execution of {STAGE_NAME} has started")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"{STAGE_NAME} execution is completed\n\n")

except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data Validation stage"

try :
    logger.info(f" Execution of {STAGE_NAME} has started")
    obj=DataValidationTrainingPipeline()
    obj.main()
    logger.info(f"{STAGE_NAME} execution is completed")

except Exception as e:
    logger.exception(e)
    raise e