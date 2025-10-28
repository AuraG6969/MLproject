import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass ## used for making class variables

@dataclass
class DataIngestionConfig: # this are the inputs we giving to the data ing compo and data ing comp knows where to save these data
    train_data_path: str=os.path.join('artifacts','train.csv') # folder name, file name
    test_data_path: str=os.path.join("artifacts",'test.csv')
    raw_data_path: str=os.path.join("artifacts",'raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self): ## reading data from the databases
        logging.info('Entered the data ingestion method or component')
        try:
            df=pd.read_csv('notebook\data\stud.csv')
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path))

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info('Train Test split initiated')
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)# saving train data
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info('Ingestion of the data is completed')
            return(
                self.ingestion_config.train_data_path, # this two info will be requiring by the data transformation to do data trans
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            raise CustomException(e,sys)
        

if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()

