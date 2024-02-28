import os,sys
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
import yaml
from CellSegmentation.utils.main_utils import read_yaml_file
from CellSegmentation.logger import logging
from CellSegmentation.exception import AppException
from CellSegmentation.entity.config_entity import ModelTrainerConfig
from CellSegmentation.entity.artifacts_entity import ModelTrainerArtifact


class ModelTrainer:
    
    def __init__(self, model_trainer_config: ModelTrainerArtifact):
        self.model_trainer_config = model_trainer_config
    
    
    
    def initiate_model_trainer(self,)-> ModelTrainerArtifact:

        logging.info('Entered initiate_model_trainer method of modelTrainer Class')
        
        try:
            
            logging.info('unzipping data')
            os.system("unzip data.zip")
            os.system("rm data.zip")
            os.system(f"yolo task=segment mode=train model={self.model_trainer_config.weight_name} data=data.yaml epochs={self.model_trainer_config.no_epochs} imgsz=640 save=true")
            os.makedirs(
                self.model_trainer_config.model_trainer_dir, exist_ok=True)
            os.system(
                f"cp runs/segment/train/weights/best.pt {self.model_trainer_config.model_trainer_dir}/")
            
            os.system("rm -rf yolov8s-seg.pt")
            os.system("rm -rf train")
            os.system("rm -rf valid")
            os.system("rm -rf test")
            os.system("rm -rf data.yaml")
            os.system("rm -rf runs")

            
            model_trainer_artifact = ModelTrainerArtifact(
            trained_model_file_path= 'artifacts/model_trainer/best.pt',
            )
            
            logging.info('Exited initiate_model_trainer method of of model')
            
        
            logging.info(f'model trainer artifact: {model_trainer_artifact}')
            
            
            return model_trainer_artifact
        
        
        
        
        except Exception as e:
            raise AppException(e, sys) from e