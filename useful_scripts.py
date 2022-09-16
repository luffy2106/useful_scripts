"""
Force Reconfigure or remove broken package
"""
# Reconfigure DPKG, the base package management system, with the following command:

sudo dpkg --configure -a

# Check if DPKG marked some packages as needing a reinstall.

sudo dpkg -l | grep ^..R

# If the command above returns a list of one or more packages, try removing the packages by typing:

sudo dpkg --purge --force-all libgbm1

# After you finish troubleshooting, run the following command to clean up the system:

sudo apt clean

# Then update the repositories:

sudo apt update

# Then upgrade the repositories:

sudo apt upgrade

"""
Create symbolic link in linux
"""
https://www.freecodecamp.org/news/symlink-tutorial-in-linux-how-to-create-and-remove-a-symbolic-link/



"""
Install pyenv : to manage python package
"""

https://www.liquidweb.com/kb/how-to-install-pyenv-on-ubuntu-18-04/

After set python version you want to global, remember to install pipenv

pip install pipenv

"""
Enable GPU on WSL2 Window:

https://ubuntu.com/tutorials/enabling-gpu-acceleration-on-ubuntu-on-wsl2-with-the-nvidia-cuda-platform#3-install-nvidia-cuda-on-ubuntu
"""



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
This code convert pil images to bytes and vice versa. It's important when you want to save image
to ram then send to API to process.

Follow this tutor:
https://jdhao.github.io/2019/07/06/python_opencv_pil_image_to_bytes/
"""

from PIL import Image
import io

# creating a image object
img = Image.open(".\data\dog.jpg")

# convert pil image to bytes
im_resize = img.resize(img.size)
buf = io.BytesIO()
im_resize.save(buf, format='JPEG')
byte_im = buf.getvalue()

print(byte_im)

# convert bytes to pil image object
image = Image.open(io.BytesIO(byte_im))
image.show()



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
- In case you have a large folder, it's better to compress and send it by tar : tar zcvf - MyBackups | ssh user@server "cat > ~/Research_e-catalog/classification_section_3/data/foo.tgz"
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
    
    
