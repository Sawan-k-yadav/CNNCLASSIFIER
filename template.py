import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s")

package_name = "CNNClassifier"

list_of_files=[
    ".github/workflows/.gitkeep",     # This .gitkeep is just for creating and adding workflow folder in github
   f"src/{package_name}/__init__.py", 
   f"src/{package_name}/components/__init__.py", 
   f"src/{package_name}/utils/__init__.py", 
   f"src/{package_name}/config/__init__.py", 
   f"src/{package_name}/pipeline/__init__.py", 
   f"src/{package_name}/entity/__init__.py", 
   f"src/{package_name}/constants/__init__.py",
   "tests/__init__.py",
   "tests/unit/__init__.py",
   "tests/integration/__init__.py",
   "configs/config.yaml",
   "params.yaml",
   "init_setup.sh",
   "requirements.txt", 
   "requirements_dev.txt",
   "setup.py",
   "setup.cfg",
   "pyproject.toml",
   "tox.ini",
   "research/trials.ipynb",
]


# Here I need to Path for getting the path of file which we will create because in window when we fetch the
# path then it comes with backward slash (\) while in linux then path comes in forward slash (/)
# So for avoiding this conflict we are using Path(filepath)
for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)

    # Here we need to check if we are creating only file creating or file under directory. 
    # If there is only file and not directory then filedir will ""(empty) which can give error in code
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filepath} already exists")