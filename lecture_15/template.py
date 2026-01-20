import os
from pathlib import Path
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'        )

while True:
    project_name = input("Enter your project name (or 'exit' to quit): ").strip()
    if project_name!=" ":
        break
    else:
        logging.info("Project name cannot be empty. Please try again.")
logging.info(f"Creating project: {project_name}")
#list of files
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "requirements.txt",
     "requirements_dev.txt",
     "pyproject.toml",
     'setup.cfg',
     "tox.ini",
     "init_setup.sh",

    "setup.py",
   
]      
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir!="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
        logging.info(f"Creating file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")



        
        