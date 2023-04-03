"""
Force Reconfigure or remove broken package in linux
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
Fix missing and broken packages in linux
"""
Method 1 : 
# Use the "fix-missing" option with "apt-get update" to run the updates and ensure the packages are up to date and there is no new version available for the packages.
sudo apt-get update --fix-missing
# Once you are done with the update, execute the below command in order to force the package manager to find any missing dependencies or broken packages and install them.
sudo apt-get install -f

Other method, check this link : https://linuxhint.com/apt_get_fix_missing_broken_packages/


"""
Install pipreques:

A very useful package when a phase of development is done, Generating concise requirements is done automatically (it looks at the packages you're importing in your project directory): https://pypi.org/project/pipreqs/

It's much better and more efficient than "pip freeze"
"""
https://pypi.org/project/pipreqs/
    

"""
Install pyenv : to manage python package
"""

https://www.liquidweb.com/kb/how-to-install-pyenv-on-ubuntu-18-04/

In case you have errors while install lib for virutal env which is related to vendored-six
Solution 1:
After set python version you want to global, remember to install pipenv
pip install pipenv

Solution 2:
https://bnikolic.co.uk/blog/python/pip/2022/02/21/vendored-six.html

"""
Enable GPU and install on WSL2 Window
"""
Solution 1(do not work 100%):
- https://ubuntu.com/tutorials/enabling-gpu-acceleration-on-ubuntu-on-wsl2-with-the-nvidia-cuda-platform#3-install-nvidia-cuda-on-ubuntu

Solution 2(work 100%, remember that install pytorch version which is suitable for cuda) 
* 1st install nvidia driver on windows 
* 2nd remove all nvidia files from WSL2: 
sudo apt-get --purge remove "*cublas*" "*cufft*" "*curand*" \ "*cusolver*" "*cusparse*" "*npp*" "*nvjpeg*" "cuda*" "nsight*"  
sudo apt-get --purge remove "*nvidia*"  
sudo rm -rf /usr/local/cuda*  
sudo apt-key del 7fa2af80  
sudo apt-get autoremove
sudo apt-get update 
* 3rd download and install cuda-11.6 run from : 
https://developer.nvidia.com/cuda-11-6-0-download-archive?target_os=Linux&target_arch=x86_64&Distribution=WSL-Ubuntu&target_version=2.0&target_type=runfile_local 
* After cuda installations: 
sudo apt-get install build-essential cmake 
* Open .bashrc file and add cuda path: 
export LD_LIBRARY_PATH="/usr/local/cuda-11.6/libnvvp:$LD_LIBRARY_PATH"  
export PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/usr/local/cuda-11.6/bin:$PATH" 
* Install pytorch for cuda 11.6: 
pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116 

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

Another way : Use FileZilla (support skip if files are already exists)


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

"""
Create symbolic link
"""
ln -s [Source_File_Path] [Symbolic_Link_Path]

ln -s /data/E-cataloging-product-data/virtualenv /home/tkdang/E-cataloging-product/e-cataloging-pipe

After this command, in e-cataloging-pipe folder there will be a symbolic link named virtualenv, which link to /data/E-cataloging-product-data/virtualenv
    
"""
Download package whl to the specfic location before installing
"""
pip download [requirement] --dest . --extra-index-url https://download.pytorch.org/whl/cu116
Ex: 
pip download torch torchvision torchaudio --dest . --extra-index-url https://download.pytorch.org/whl/cu116

"""
set up variable
"""
Solution 1:
- Go to /etc/environment file and set up. ex : TMPDIR=/home/repldba/tempfiles
Solution 2:
- export TMPDIR=/home/repldba/tempfiles/

"""
Set up path for global varialbe
"""
Open bashrc file by nano ~/.bashrc then add the line to specify the path you want to use for the variable. Ex :  
- If you want to set up path for global python : export PATH=$PATH:/usr/bin/python2.7
- If you want to set up path for global npm : export PATH=$PATH:/usr/bin/npm
Remember to apply change by command : .  ~/.bashrc

"""
Force pip to use a different tmp directory that resides on a partition where we have a lot of free space.
"""
TMPDIR=/data/tmp pip install -r requirements.txt
More info : https://issamemari.github.io/jekyll/update/2022/03/16/pip-install-no-space-left.html
        
"""
Get into the default terminal of Linux
"""

/bin/bash

"""
copy file from local machine to WSL
"""
Go to the place in WSL where you want to copy file there, then type:
- cp /mnt/c/Users/tkdang/Downloads/resnet101-FPN_nuclaynet_2x_AMP.zip .


