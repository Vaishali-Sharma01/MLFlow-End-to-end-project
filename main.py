from mlflow_project import logger
from mlflow_project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion stage"
try :
    logger.info(f" Execution of {STAGE_NAME} has started")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"{STAGE_NAME} execution is completed\n\n")

except Exception as e:
    logger.exception(e)
    raise e
