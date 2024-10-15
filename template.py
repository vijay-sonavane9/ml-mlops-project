import os 
import os.path
from pathlib import Path 
import logging 

logging.basicConfig(level=logging.INFO)

project_name = "mlproject"

list_of_files=[
    #".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_monitering.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/predictions_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"
]

for filepath in list_of_files:
    filepath = Path(filepath) #to make it easier to work with file paths (file addresses) in Python.
    filedir, filename = os.path.split(filepath)  # filedir -->  "src/{project_name}", filename --> "__init__.py"
    
    if filedir !="": # if there is some parent folder to a file
        os.makedirs(filedir,exist_ok=True) # if yes then keep as it is #exist_ok=True part means, "It's okay if the folder already exists. Don't give an error.
        logging.info(f"creating directory:{filedir} for the file {filename}")

    """
    
This checks two things:
1. Is the file already there (os.path.exists(filepath)) ???
2. If the file is there, is it empty (size 0) ??

    """
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        
        """ 
        
If either of these conditions is true, the code inside the if block runs. This block is:
The creation of an empty file happens automatically when you use the open() function in write mode ('w') in Python,
even if you don't explicitly write any content to the file.

        """
     
        with open(filepath,'w') as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
        
        
    else:
        logging.info(f"{filename} already exists")
        
    