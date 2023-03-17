import os, logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s || %(levelname)s || %(message)s]'
)

while True:
    PROJECT_NAME = input("Enter project name: ")
    if PROJECT_NAME != "":
        break

#List of file for the project
list_of_files = [
    "main.py", 
    "setup.py",
    "requirements.txt",
    f"{PROJECT_NAME}/__init__.py",
    f"{PROJECT_NAME}/components/__init__.py",
    f"{PROJECT_NAME}/components/data_ingestion.py",
    f"{PROJECT_NAME}/components/data_validation.py",
    f"{PROJECT_NAME}/components/data_transformation.py",
    f"{PROJECT_NAME}/components/model_trainer.py",
    f"{PROJECT_NAME}/components/model_evaluation.py",
    f"{PROJECT_NAME}/components/model_pusher.py",
    f"{PROJECT_NAME}/entity/__init__.py",
    f"{PROJECT_NAME}/entity/config_entity.py",
    f"{PROJECT_NAME}/entity/artifact_entity.py",
    f"{PROJECT_NAME}/logger.py",
    f"{PROJECT_NAME}/exception.py",
    f"{PROJECT_NAME}/utils.py",
]

for filepath in list_of_files:
    
    filepath = Path(filepath)
    filedir , filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Directory created: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)):
        with open(filepath, 'w') as f:
            pass
        logging.info(f'File created: {filename}')

    else:
        logging.info(f"This file already present: {filepath}")