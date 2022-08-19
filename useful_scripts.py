"""
Virtual environments jupyterlab
"""
pip freeze > requirements.txt
virtualenv --python=python3.6 .venv
source .venv/bin/activate
pip install jupyterlab ipykernel
ipython kernel install --user --name=.venv
jupyter lab --no-browser --ip="0.0.0.0" --port=9874 --NotebookApp.token='' --NotebookApp.password=''



"""
Check to see to reasearch on if cuda and pytorch is compatible
"""
python -m detectron2.utils.collect_env





"""
Delete similar files in folder
"""
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


"""
Draw list of bounding bounding box from list of coordinator
"""
import cv2
from google.colab.patches import cv2_imshow
def show_bounding_boxs(image_path, list_bounding_box):
  """
  Each bouding box in the list is : x0,y0,x1,y1, which follow the standard of\
  openCV
  """
  image = cv2.imread(path)
  #Blue color in BGR
  color = (255, 0, 0)
  #Line thickness of 2 px 
  thickness = 2
  for box in list_bounding_box: 
    start_point = (box[0], box[1]) 
    end_point = (box[2], box[3])    
    # Using cv2.rectangle() method  
    # Draw a rectangle with blue line borders of thickness of 2 px  
    image = cv2.rectangle(image, start_point, end_point, color, thickness) 
    # if you use openCV
    # cv2.imshow('image',image) 
    # if you use google colab 
    cv2_imshow(image)

path = "V-216B-131-A-873_005_001-105.jpg"
list_bounding_box = [(5,5,220,220)]
show_bounding_boxs(path, list_bounding_box)


"""
Tips for VScode
"""
- https://medium.com/@i_AnkurBiswas/pro-tips-for-visual-studio-code-to-be-productive-in-2018-d5252e914561


"""
Transfer files between server and host
"""
Download file from server to local
- (Go to location on the local computer):scp ecatdeployv2@172.16.255.27:/etc/systemd/system/log_back_20.7.txt . 
Upload file from local to server
- (Go to location on the local computer):scp /file/to/send username@remote:/where/to/put

"""
Set permanent DNS server in Ubuntu(To avoid wifi can not access in ubuntu)
"""

https://www.tecmint.com/set-permanent-dns-nameservers-in-ubuntu-debian/

"""
Set up remote ssh along with key vscode
"""

https://towardsdatascience.com/5-steps-setup-vs-code-for-remote-development-via-ssh-from-windows-to-linux-b9bae9e8f904


"""
Debuggin in vscode 
"""
- Set up working environtment for debugging and running program in vs code : Bam to hop phim Ctrl+Shift+P => search interpreter => select path of intepreter python. 
Cach 2, co the chon Python intepreter goc duoi cung ben phai man hinh(goc 17h).
- Set up debugging(Luu y buoc nay chi nen ap dung trong truong hop debug ung dung, con voi file python thong thuong, buoc dau tien la du) : Bam to hop phim Ctrl+Shift+D, create 'launch.json' file(if there is not), file dc tao ra se o trong thu muc .vscode/launch.json, tai day ban co the chon
python interpreter (thong qua bien envFile) va file ban muon debug (thong qua bien program). File mau launch.json se co noi dung nhu sau:

{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            // "program": "${file}",
            "program": "${file}",
            "console": "integratedTerminal",
            "envFile": "${workspaceFolder}/.env",
            "justMyCode": true,
            "env": {}
        }
    ]
}
    
    
