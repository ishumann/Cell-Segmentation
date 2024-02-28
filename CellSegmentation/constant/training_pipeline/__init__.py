ARTIFACTS_DIR: str = "artifacts"

"""Data Ingestion related constant start with DATA_INGESTION var name"""

DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str= "feature_store"
DATA_DOWNLOAD_URL: str = "https://drive.google.com/file/d/1487BQ-cmMHYSzLpVcE7toGNnfW1nhP7d/view?usp=sharing"




"""
Data Validation Related Content Start with DATA_VALIDATION VAR NAME
"""

DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_STATUS_FILE = 'status.txt'
DATA_VALIDATION_ALL_REQUIRED_FILES = ['train','valid', 'test', 'data.yaml']


"""
Model Trainer Related constant start with MODEL_TRAINER var name
"""

MODEL_TRAINER_DIR_NAME: str = 'model_trainer'
MODEL_TRAINER_PRETRAINED_WEIGHT_NAME: str = 'yolov8s-seg.pt'
MODEL_TRAINER_NO_EPOCHS: int = 1
# MODEL_TRAINER_BATCH_SIZE: int = 16 #using default batch size

