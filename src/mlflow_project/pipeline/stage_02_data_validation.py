from mlflow_project.config.configuration import ConfigurationManager
from mlflow_project.components.data_validation import DataValidation
from mlflow_project import logger

STAGE_NAME = "Data Validation stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        ## data ingestion pipeline
        config=ConfigurationManager()
        data_validation_config=config.get_data_validation_config()
        data_validation=DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()


if __name__ == '__main__':
    try :
        logger.info(f" Execution of {STAGE_NAME} has started")
        obj=DataValidationTrainingPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} execution is completed")

    except Exception as e:
        logger.exception(e)
        raise e


