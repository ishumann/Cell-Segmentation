from CellSegmentation.logger import logging
from CellSegmentation.exception import AppException
import sys
logging.info("Welcome is running")

try:
    a= 4/"8"

except Exception as e:
    raise AppException(e,sys)
#   print('An exception occurred')