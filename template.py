import os
from pathlib import Path 
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s: %(message)s:]')

project_name = "textSummarizer"

list_of_files =[
    ".github/workflows/.gitkeep"
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "test.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info("Creating directory: {} for the file {}".format(filedir,filename))
    
#os.path.getsize(filepath) == 0 because if the file size is not 0 then it will ignore otherwise if template file is run multiple times
# then it will overwrite the files and the code is lost
    if (not os.path.exists(filename)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info("Creating file: {}".format(filepath))
    else:
        logging.info(f"{filename} already exists")
            

