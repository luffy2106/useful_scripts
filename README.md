# useful_scripts


## Virtual environments jupyterlab 
virtualenv --python=python3.6 .venv  
source .venv/bin/activate  
pip install jupyterlab ipykernel  
ipython kernel install --user --name=.venv  
jupyter lab  --no-browser --ip="0.0.0.0" --port=9874 --NotebookApp.token='' --NotebookApp.password=''  





## Delete similar files in folder
from pathlib import Path
import glob

all_files = set()
my_path = ".\\Pictures"
files = glob.glob(my_path + '/**/*.*', recursive=True)
for file in files:
    path_file = Path(file)
    file_name = path_file.name
    if file_name not in all_files:
        all_files.add(file_name)
    else:
        rem_file = Path(file)
        rem_file.unlink()
