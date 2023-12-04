# This is the useful scripts that need to reuse frequently

#### Force Reconfigure or remove broken package in Linux
Reconfigure DPKG, the base package management system, with the following command:
```
sudo dpkg --configure -a
```
Check if DPKG marked some packages as needing a reinstall.
```
sudo dpkg -l | grep ^..R
```
If the command above returns a list of one or more packages, try removing the packages by typing:
```
sudo dpkg --purge --force-all libgbm1
```
After you finish troubleshooting, run the following command to clean up the system:
```
sudo apt clean
```
Then update the repositories:
```
sudo apt update
```
Then upgrade the repositories:
```
sudo apt upgrade
```

#### Fix missing and broken packages in linux
##### - Method 1 : 
Use the "fix-missing" option with "apt-get update" to run the updates and ensure the packages are up to date and there is no new version available for the packages.
```
sudo apt-get update --fix-missing
```
Once you are done with the update, execute the below command in order to force the package manager to find any missing dependencies or broken packages and install them.
```
sudo apt-get install -f
```
##### - Other method, check this link : 
```
https://linuxhint.com/apt_get_fix_missing_broken_packages/
```

#### Create a symbolic link in Linux
After this command, in e-cataloging-pipe folder, there will be a symbolic link named virtualenv, which links to /data/E-cataloging-product-data/virtualenv
```
ln -s [Source_File_Path] [Symbolic_Link_Path]
ln -s /data/E-cataloging-product-data/virtualenv /home/tkdang/E-cataloging-product/e-cataloging-pipe
```
Reference:
```
https://www.freecodecamp.org/news/symlink-tutorial-in-linux-how-to-create-and-remove-a-symbolic-link/
```

#### Install pipreques:

A very useful package when a phase of development is done, Generating concise requirements is done automatically (it looks at the packages you're importing in your project directory): 
```
https://pypi.org/project/pipreqs/
```
It's much better and more efficient than "pip freeze"


#### Install pyenv : to manage python package
```
https://www.liquidweb.com/kb/how-to-install-pyenv-on-ubuntu-18-04/
```

In case you have errors while install lib for virutal env which is related to vendored-six
##### - Solution 1:
After set python version you want to global, remember to install pipenv
```
pip install pipenv
```
##### - Solution 2:(more effective)
Create virtual environment and download get-pip.py
```
curl -sS https://bootstrap.pypa.io/get-pip.py |  python    
```
More solution:
```
https://bnikolic.co.uk/blog/python/pip/2022/02/21/vendored-six.html
```

#### Install poetry : better to manage python package than pyenv

Install and usage:
```
https://python-poetry.org/docs/#installing-with-the-official-installer
```
Install virutual environment with requirement.txt:
1. Go to your project directory and init project
```
cd pre-existing-project
poetry init
```
2. pyproject.toml will be create, set up your virtualenv
```
poetry env use python
```
3. Activate virtual env
```
poetry shell
```
You can follow this tutor for ref:
```
https://python-poetry.org/docs/basic-usage/
```
4. Once you are inside the virtualenv, you can use the following command to generate a poetry.lock file based on your existing dependencies:
```
poetry lock
```
If you have file pyproject.toml, you can install dependency by:
```
poetry install
```
5. After generating the poetry.lock file, you can use the following command to add the dependencies from your requirements.txt file to your virtualenv:
```
for item in $(cat requirements.txt); do poetry add "${item}"; done
```
6. Finally, you can use the following command to update your poetry.lock file with the new dependencies:
```
poetry lock
```
7. Test virtualenv
```
poetry run python your_script.py
```
or
```
poetry run python
```
 
#### Install CUDA on WSL2 Window and enable GPU in Pytorch

##### - Solution 1(do not work 100%):
```
https://ubuntu.com/tutorials/enabling-gpu-acceleration-on-ubuntu-on-wsl2-with-the-nvidia-cuda-platform#3-install-nvidia-cuda-on-ubuntu
```
##### - Solution 2(work 100%, remember that install pytorch version which is suitable for cuda) 
1. Install nvidia driver on windows
- type "dxdiag" in the searchbar, then click on Affichage 2, see "Nom" to know the name of your NVIDIA card
- Go to the following website and download NVIDIA drive(remember to choose the driver which is suitable to your card)
```
https://www.nvidia.com/download/find.aspx# 
```
3. Remove all nvidia files from WSL2: 
```
sudo apt-get --purge remove "*cublas*" "*cufft*" "*curand*" \ "*cusolver*" "*cusparse*" "*npp*" "*nvjpeg*" "cuda*" "nsight*"  
sudo apt-get --purge remove "*nvidia*"  
sudo rm -rf /usr/local/cuda*  
sudo apt-key del 7fa2af80  
sudo apt-get autoremove
sudo apt-get update
``` 
3. download and install cuda-11.6 run from : 
```
https://developer.nvidia.com/cuda-11-6-0-download-archive?target_os=Linux&target_arch=x86_64&Distribution=WSL-Ubuntu&target_version=2.0&target_type=runfile_local 
```
4. Verify Cuda installation
The following command should show Cuda and NVIDIA driver versions:
```
nvidia-smi
```
5. After cuda installations, install essential tools such as compilers, libraries, and build utilities required for building software. Also install cmake
```
sudo apt-get install build-essential cmake 
```
6. Set up cuda as environment variable:
Open .bashrc file 
```
nano  ~/.bashrc
```
and add Cuda path: 
```
export LD_LIBRARY_PATH="/usr/local/cuda-11.6/libnvvp:$LD_LIBRARY_PATH"  
export PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/usr/local/cuda-11.6/bin:$PATH" 
```
7. Verify cuda is well installed and configure 
Install pytorch for cuda 11.6(optional): 
```
pip3 install torch torchvision --extra-index-url https://download.pytorch.org/whl/cu116 
```
Go to python environment and test
```
import torch
cuda_version = torch.version.cuda
print(f"CUDA Version: {cuda_version}")
```
It should show CUDA version
#### Virtual environments jupyterlab
```
pip freeze > requirements.txt
virtualenv --python=python3.6 .venv
source .venv/bin/activate
pip install jupyterlab ipykernel
ipython kernel install --user --name=.venv
jupyter lab --no-browser --ip="0.0.0.0" --port=9874 --NotebookApp.token='' --NotebookApp.password=''
```


#### Check to see to reasearch on if cuda and pytorch is compatible
```
python -m detectron2.utils.collect_env
```
#### This code convert pil images to bytes and vice versa. It's important when you want to save image to ram then send to API to process.
Follow this tutor:
```
https://jdhao.github.io/2019/07/06/python_opencv_pil_image_to_bytes/
```
Code implementation
```
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
```


#### Delete similar files in folder
```
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
```

#### Draw list of bounding bounding box from list of coordinator
```
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
```

#### Tips for VScode
```
https://medium.com/@i_AnkurBiswas/pro-tips-for-visual-studio-code-to-be-productive-in-2018-d5252e914561
```
#### Transfer files between server and host
##### - Download file from server to local
Go to the location on the local computer:
```
scp ecatdeployv2@172.16.255.27:/etc/systemd/system/log_back_20.7.txt . 
```
In case you have a large folder, it's better to compress and send it by tar : 
```
tar zcvf - MyBackups | ssh user@server "cat > ~/Research_e-catalog/classification_section_3/data/foo.tgz"
```
##### - Upload file from local to server
Go to the location on the local computer:
```
scp /file/to/send username@remote:/where/to/put
```
Another way: Use FileZilla (support skip if files already exist)

#### Set permanent DNS server in Ubuntu(To avoid wifi can not access in ubuntu)
```
https://www.tecmint.com/set-permanent-dns-nameservers-in-ubuntu-debian/
```
Set up remote ssh along with key vscode
```
https://towardsdatascience.com/5-steps-setup-vs-code-for-remote-development-via-ssh-from-windows-to-linux-b9bae9e8f904
```
#### Debugging in vscode 

- Set up working environtment for debugging and running program in vs code : Bam to hop phim Ctrl+Shift+P => search interpreter => select path of intepreter python. 
Cach 2, co the chon Python intepreter goc duoi cung ben phai man hinh(goc 17h).
- Set up debugging(Luu y buoc nay chi nen ap dung trong truong hop debug ung dung, con voi file python thong thuong, buoc dau tien la du) : Bam to hop phim Ctrl+Shift+D, create 'launch.json' file(if there is not), file dc tao ra se o trong thu muc .vscode/launch.json, tai day ban co the chon
python interpreter (thong qua bien envFile) va file ban muon debug (thong qua bien program). File mau launch.json se co noi dung nhu sau:
```
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
```

#### Download package whl to the specfic location before installing
```
pip download [requirement] --dest . --extra-index-url https://download.pytorch.org/whl/cu116
```
Ex:
``` 
pip download torch torchvision torchaudio --dest . --extra-index-url https://download.pytorch.org/whl/cu116
```

#### Set up a variable

##### - Solution 1:
Go to /etc/environment file and set up. ex : TMPDIR=/home/repldba/tempfiles
##### - Solution 2:
```
export TMPDIR=/home/repldba/tempfiles/
```

#### Set up path for global variable
Open bashrc file by nano ~/.bashrc then add the line to specify the path you want to use for the variable. Ex :  
- If you want to set up path for global python : export PATH=$PATH:/usr/bin/python2.7
- If you want to set up path for global npm : export PATH=$PATH:/usr/bin/npm
Remember to apply change by command : .  ~/.bashrc

#### Force pip to use a different tmp directory that resides on a partition where we have a lot of free space.
```
TMPDIR=/data/tmp pip install -r requirements.txt
```
More info : 
```
https://issamemari.github.io/jekyll/update/2022/03/16/pip-install-no-space-left.html
```        

#### Get into the default terminal of Linux
```
cd /bin/bash
```
#### Copy file from local machine to WSL
Go to the place in WSL where you want to copy file there, then type:
```
cp /mnt/c/Users/tkdang/Downloads/resnet101-FPN_nuclaynet_2x_AMP.zip .
```

#### Docker
##### Docker tips
If you want to see logs of docker container:
```
docker logs <container_id>
```
If you want to see logs of docker, but the docker exit immediately => Try starting a new container and dropping into a shell
```
docker run --interactive --tty --entrypoint /bin/sh nginx:latest(docker container name/ID)
docker run -it image_name sh
```
If you want to delete all docker container which associate with a docker image:
```
docker rm $(docker ps -aq --filter ancestor=<name_docker_image>)
```
Docker tricks:
```
https://chrislevn.github.io/dockerfile-practices/
```
##### Optimize docker build from docker file:
The --cache-from option in Docker allows you to specify a previously built image as a cache source for the current build. This can help speed up the build process by reusing layers from the cached image that are identical to the ones in the current build.
Here's an example of how to use --cache-from:
1. First, build your Docker image and tag it with a name and version number:
```
docker build -t my-image:v1 .
```
2. Next, make some changes to your code or dependencies, and rebuild the image using the --cache-from option:
```
docker build --cache-from my-image:v1 -t my-image:v2 .
```
In this command, we're telling Docker to use the my-image:v1 image as a cache source for the my-image:v2 build. If there are any identical layers between the two images, Docker will reuse them instead of rebuilding them.

Note that if the my-image:v1 image is not available locally, Docker will try to pull it from the registry specified in the Dockerfile (FROM statement).
3. Finally, run your updated container using the new image:
```
docker run -it my-image:v2
```
That's it! By using the --cache-from option, you can speed up your Docker builds by reusing identical layers from previously built images.

##### Clean docker 

If you want to see how much docker take the size of the system:
```
docker system df
```
If you want to clear all docker data
```
sudo docker system prune -a
```
If you want to clear all docker volumn only
```
sudo docker system prune -a --volumes
```

#### gunicorn
If you want to debug gunicorn, use "preload"
```
gunicorn app:application --preload -b 0.0.0.0:5000 
```

#### Elastic Search
1. List all docs name in an index:
```
curl -H 'Content-Type: application/json' -XGET 'http://localhost:9200/index_name/_search?size=10000&filter_path=hits.hits._source' -d '
{
    "query": {
        "match_all": {}
    },
   "_source": ["filename"]
}
'
```

2. List all id of docs in an index
```
curl -X GET "localhost:9200/k_catalog/_search?pretty" -H 'Content-Type: application/json' -d'
{
    "query": {
        "match_all": {}
    },
  "stored_fields": [
    "_source.filename"
  ]
}
'
```
3. Delete all docs in an index
```
curl -X GET "http://localhost:9200/<index_name>/_search" -H 'Content-Type: application/json' -d'
{
  "query": {
    "match_all": {}
  }
}
'
```

#### Enable docker connect to GPU
1. If you use docker-compose to build
```
https://docs.docker.com/compose/gpu-support/
```
2. If you user docker file to build(highly recommend)
Set up the NVIDIA Container Toolkit by running the following command:
```
sudo apt-get install -y nvidia-container-toolkit
```
After the installation is complete, restart Docker to apply the changes by running the following command:
- If you use linux:
```
sudo systemctl restart docker
```
- If you use WSL:
```
sudo service docker restart
```
Verify that the NVIDIA Container Toolkit is installed correctly by running the following command(need to check that docker image is available on docker hub first):
```
docker run --gpus all nvidia/cuda:11.4.3-base-ubuntu20.04 nvidia-smi
```
It should show CUDA and driver version

#### Useful tricks and library
1. Use only one logger to debug
```
https://github.com/Delgan/loguru#structured-logging-as-needed
```
2. Modify proxy in WSL
You need to modify 3 files:
For download package:
```
~/.bashrc
/etc/environment
```
For git:
```
~/.gitconfig
```
#### Back up and restore WSL
```
https://www.virtualizationhowto.com/2021/01/wsl2-backup-and-restore-images-using-import-and-export/
```

#### Install package by poetry using external link
Suppose that you have this command to install by pip
```
pip install torch==1.13.1+cu116 torchvision==0.14.1+cu116 torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cu116
```
If you want to install by poetry, you should add this to pyproject.toml
```
[tool.poetry.dependencies]
python = "^3.9"
torch = {version = "1.13.1+cu116", source = "pytorch-gpu-src"}
torchvision = {version = "0.14.1+cu116", source = "pytorch-gpu-src"}
[[tool.poetry.source]]
name = "pytorch-gpu-src"
url = "https://download.pytorch.org/whl/cu116"
priority = "explicit"
```
Then run
```
poetry install
```

#### Connect to EC2 instance AWS:
Follow this tutorial
```
https://medium.com/@christyjacob4/using-vscode-remotely-on-an-ec2-instance-7822c4032cff
```
Then add this to the log file as mentioned in the above link
```
Host CurieGPT_web_server
  HostName 13.37.215.79
  User ubuntu
  IdentityFile C:\key_ssh\aviary_aws\aviary_ubuntu_key.pem
```
Then you need to fix the permission issuse in window
```
icacls aviary_ubuntu_key.pem /inheritance:r
icacls aviary_ubuntu_key.pem /grant:r "<your_username_here>":F
```
Finally, do CTRL + Shift + P to choose the host name then connect to EC2 instance.
Note:
Remember that everytime you shut down an EC2 instance and relaunch it, the IP address change => should configure

#### Install git lfs
Adding the packagecloud repository
```
(. /etc/lsb-release &&
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh |
sudo env os=ubuntu dist="${DISTRIB_CODENAME}" bash)
```
Installing packages
```
sudo apt-get install git-lfs
```
Check if it's installed successfully
```
git lfs version
```
Reference :
```
https://github.com/git-lfs/git-lfs/blob/main/INSTALLING.md
```

#### Organize a good deeplearning project
```
https://neptune.ai/blog/how-to-organize-deep-learning-projects-best-practices
```
Install cookiecutter
```
pip install cookiecutter
cookiecutter https://github.com/drivendata/cookiecutter-data-science
```

#### Attach volumn to docker and connect to docker container by vscode
Need to be updated
```
docker run --gpus all -it --name nvidia-cuda -v /home/tkdang/Assytem_projects/E-cataloging-v2/ms3-stamp-signature-detection:/home
 nvidia/cuda:11.7.1-devel-ubuntu22.04
```

#### Error about CUDA
- When ever you have error related to CUDA, try to use CPU first to debug.
- Any errors related to 'srcIndex < srcSelectDimsiz' might be because of the dimension of tokenizer is not match to number of the features input of the pretrained model

#### Note about unicorn and gunicorn
- If you use unicorn, gurnicorn and pyenv to create your virtual environment, remember to install unicorn, gurnicorn after you create virtualenv, dont install these lib on pyenv, otherwise gunicorn/uvicorn will keep using the library in pyenv eventhough you already activate virtual environment.
- If you already install unicorn/gurnicorn in pyenv, uninstall them

#### Debugging by command line python 
To run a command line program but stop at a breakpoint, you can use a debugger. Python comes with a built-in debugger called pdb (Python DeBugger).
- First, insert this line in your code where you want the execution to stop:
```
import pdb; pdb.set_trace()
```
- Then, run your Python script from the command line like you normally would. The program will execute until it hits the pdb.set_trace() line, and then it will enter the debugger.
```
python your_script.py
```
The program will execute until it hits the pdb.set_trace() line, and then it will enter the debugger. You'll see a (Pdb) prompt where you can type commands to inspect variables, step over lines, etc.

Some useful pdb commands are:
- n(ext): Execute the next line.
- s(tep): Execute and step into function.
- c(ontinue): Continue execution until a breakpoint is encountered.
- p(rint) <expression>: Evaluate and print the Python expression.
- q(uit): Quit the debugger and exit.

Remember to remove or comment out the line import pdb; pdb.set_trace() when you're done debugging.

#### Note when working with huggingface dataset

Sometimes when you work with Hugging Face dataset and use map function. The will be some exception parse. Don't try to return None value in the exception catch. Take a look at the features of the hugging face dataset and put empty value for the exceptional case. Then you can filter by the condition later. If you return None on the exceptional case, you will have the KeyError problem.


#### Debugging in docker running background

Dockerd is the command line to show the logs of docker deamon,very important if you want to debug docker deamon.

For example, if you can not restart docker service or have an error like this:
```
docker: Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?.
```
you should use this command to see the log
```
sudo dockerd
```
Normally the solution is this(try and type dockerd again to see if it resolved)
```
sudo update-alternatives --set iptables /usr/sbin/iptables-legacy
sudo update-alternatives --set ip6tables /usr/sbin/ip6tables-legacy
```
Reference:
```
https://forums.docker.com/t/failing-to-start-dockerd-failed-to-create-nat-chain-docker/78269
```
### Note about gitlab push

If you use ssh to push instead of HTTP, you don't have to enter your id and pass again and again 

