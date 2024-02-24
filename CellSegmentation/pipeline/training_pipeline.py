import sys, os
from CellSegmentation.logger import logging
from CellSegmentation.exception import AppException
from CellSegmentation.components.data_ingestion import DataIngestion
from CellSegmentation.entity.config_entity import (DataIngestionConfig)
from CellSegmentation.entity.artifacts_entity import (DataIngestionArtifact)

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()


    def start_data_ingestion(self)-> DataIngestionArtifact:
        try:
            logging.info("entered the start_data_ingestion method of TrainPipeline class")
            logging.info('getting the data from url')
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            
            logging.info('Got the data from URL')
            logging.info('Exited the start_data_ingestion method of TrainPipeline class')
            
            return data_ingestion_artifact
        except Exception as e:
            raise AppException(e,sys) from e
        
    def run_pipeline(self)-> None:
        try:
            data_ingestion_artifact = self.start_data_ingestion()
        except Exception as e:
            raise AppException(e,sys) from e