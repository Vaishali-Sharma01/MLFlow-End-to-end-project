from mlflow_project.config.configuration import ConfigurationManager
from mlflow_project.components.data_validation import DataValidation
from mlflow_project import logger
from mlflow_project.components.data_transformation import DataTransformation
from pathlib import Path

STAGE_NAME = "Data Transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        ## data transformation pipeline
        try:
            with open(Path("artifacts/data_validation/status.txt"),"r") as f:
                status=f.read().split(" ")[-1]

            if status=="True":

                config=ConfigurationManager()
                data_transformation_config=config.get_data_transformation_config()
                data_transformation=DataTransformation(data_transformation_config)
                data_transformation.train_test_splitting()

            else:
                raise Exception("Your data schema is not valid.")
            

        except Exception as e:
            print(e)


if __name__ == '__main__':
    try :
        logger.info(f" Execution of {STAGE_NAME} has started")
        obj=DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} execution is completed")

    except Exception as e:
        logger.exception(e)
        raise e


