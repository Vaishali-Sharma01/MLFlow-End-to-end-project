from mlflow_project.config.configuration import ConfigurationManager
from mlflow_project import logger
from mlflow_project.components.model_trainer import ModelTrainer
from pathlib import Path

STAGE_NAME = "Model Training stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        
        config=ConfigurationManager()
        model_trainer_config=config.get_model_trainer_config()
        model_trainer=ModelTrainer(model_trainer_config)
        model_trainer.train()


if __name__ == '__main__':
    try :
        logger.info(f" Execution of {STAGE_NAME} has started")
        obj=ModelTrainingPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} execution is completed")

    except Exception as e:
        logger.exception(e)
        raise e
       