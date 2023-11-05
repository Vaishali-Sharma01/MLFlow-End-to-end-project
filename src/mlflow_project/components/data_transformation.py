import os
import pandas as pd
from sklearn.model_selection import train_test_split
from mlflow_project import logger
from mlflow_project.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config=config

    def train_test_splitting(self):
        df=pd.read_csv(self.config.data_path)

        #splitting ratio will be 7:3
        train,test=train_test_split(df,test_size=0.3,random_state=101)

        train.to_csv(os.path.join(self.config.root_dir,"train.csv"),index=False)
        test.to_csv(os.path.join(self.config.root_dir,"test.csv"),index=False)

        logger.info("Splitted dataset into training and test sets")
        logger.info(f"Size of training dataset: {train.shape}")
        logger.info(f"Size of test dataset: {test.shape}")

        print(train.shape)
        print(test.shape)