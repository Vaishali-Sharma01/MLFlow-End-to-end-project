import os
import pandas as pd
from mlflow_project import logger
from mlflow_project.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self,config:DataValidationConfig):
        self.config=config

    def validate_all_columns(self) -> bool:
        try:
            validation_status = None
            df=pd.read_csv(self.config.unzip_data_dir)
            all_columns=list(df.columns)
            all_schema=self.config.all_schema
            

            for column in all_columns:
                if column not in all_schema.keys() or df[column].dtype != all_schema[column] :
                    logger.info(f"validating status as false for column:{column}")
                    validation_status=False
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"Validation Status : {validation_status}")

                else:
                    validation_status=True
                    logger.info(f"validating status as true for column:{column}")
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"Validation Status : {validation_status}")

        except Exception as e:
            raise e
                    

