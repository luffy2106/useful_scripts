# useful_scripts


## Virtual environments jupyterlab 
virtualenv --python=python3.6 .venv
source .venv/bin/activate
pip install jupyterlab ipykernel
ipython kernel install --user --name=.venv
jupyter lab  --no-browser --ip="0.0.0.0" --port=9874 --NotebookApp.token='' --NotebookApp.password=''
