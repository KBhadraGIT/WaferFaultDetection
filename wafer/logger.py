import os, logging
from datetime import datetime

#Name of the log file
LOG_FILE_NAME = f"{datetime.now().strftime('%Y%m%d__%H%M%S')}.log"

#Log file directory
LOG_FILE_DIR = os.path.join(os.getcwd(),"logs")

#Creating Log file directory if not available
os.makedirs(LOG_FILE_DIR, exist_ok = True)

#Log file path
LOG_FILE_PATH = os.path.join(LOG_FILE_DIR , LOG_FILE_NAME)

#Formating the logger
logging.basicConfig(
    level = logging.INFO,
    filename = LOG_FILE_NAME,
    format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s]",
)