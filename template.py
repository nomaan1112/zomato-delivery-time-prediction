import os, sys
import logging
from pathlib import Path

while True:
    project_name = input("Enter the name of source file.")
    if project_name != "":
        break


list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/exceptions/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/utils/__init__.py",
    f"config/config.yaml",
    "schema.yaml",
    "app.py",
    "logs.py" ,
    "setup.py"   
]

for file_path in list_of_files:
    path = Path(file_path)
    filedir,filename = os.path.split(path)

    if filedir != "":
        os.makedirs(filedir, exist_ok = True)

    if (not os.path.exists(path) or (os.path.getsize(path)) == 0):
        with open(file_path , "w") as f:
            pass

    else:
        logging.info("File is already present.")            

