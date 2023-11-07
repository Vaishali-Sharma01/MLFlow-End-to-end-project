from mlflow_project.config.configuration import ConfigurationManager
from mlflow_project import logger
from mlflow_project.components.model_evaluation import ModelEvaluation
from pathlib import Path

STAGE_NAME = "Model Evaluation stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        
        config=ConfigurationManager()
        model_evaluation_config=config.get_model_evaluation_config()
        model_evaluator=ModelEvaluation(config=model_evaluation_config)
        model_evaluator.log_into_mlflow()


if __name__ == '__main__':
    try :
        logger.info(f" Execution of {STAGE_NAME} has started")
        obj=ModelEvaluationPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} execution is completed")

    except Exception as e:
        logger.exception(e)
        raise e
       