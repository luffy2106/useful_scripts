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


Set permanent DNS server in Ubuntu(To avoid wifi can not access in ubuntu)

https://www.tecmint.com/set-permanent-dns-nameservers-in-ubuntu-debian/

