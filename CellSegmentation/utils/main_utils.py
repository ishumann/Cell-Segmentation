import os.path
import sys
import yaml
import base64

from CellSegmentation.exception import AppException
from CellSegmentation.logger import logging

def read_yaml_file(file_path: str) -> dict:
    """
    Read a YAML file and return its contents as a dictionary.
    Args:file_path (str): The path to the YAML file.
    Returns: dict: The contents of the YAML file as a dictionary.
    Raises: AppException: If there is an error reading the YAML file.
    """
    try:
        with open(file_path, "rb") as yaml_file:
            logging.info("Read yaml file successfully")
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise AppException(e, sys) from e
    


def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    """
    Write content to a YAML file.

    Args:
        file_path (str): The path to the YAML file.
        content (object): The content to be written to the file.
        replace (bool, optional): Whether to replace the file if it already exists. Defaults to False.
    
    Raises:
        AppException: If an error occurs while writing the file.

    Returns:
        None
    """
    
    try:
        if replace and os.path.exists(file_path):
            os.remove(file_path)
            
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            yaml.dump(content, file)
            logging.info("Successfully wrote YAML file")

    except Exception as e:
        raise AppException(e, sys) from e
    
    
import base64

def decodeImage(imgstring, fileName):
    """
    Decode the given image string and save it as a file with the specified file name.

    Args:
        imgstring (str): The base64 encoded image string.
        fileName (str): The name of the file to be saved.

    Returns:
        None
    """
    imgdata = base64.b64decode(imgstring)
    with open(f'./data/{fileName}', "wb") as file:
        file.write(imgdata)
        file.close()
        
def encodeImageIntoBase64(croppedImagePath):
    """
    Encodes an image file into base64 format.

    Args:
        croppedImagePath (str): The path to the image file.

    Returns:
        bytes: The base64-encoded image data.
    """
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())
        
    