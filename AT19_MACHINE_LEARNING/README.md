# AT19_MACHINE_LEARNING
# Requirements needed to run the code
* Precondition. 
    - Python 3.8.8
    - If you have a Windows operating system, you should be installed Visual Studio (c++ Desktop package). to run Face_recognition.
    <https://visualstudio.microsoft.com/>

* Download the pretrained models(mobilenet, resnet,inception,densenet and frontalface).
    <https://github.com/OlafenwaMoses/ImageAI/releases/download/3.0.0-pretrained/mobilenet_v2-b0353104.pth/>
    <https://github.com/OlafenwaMoses/ImageAI/releases/download/3.0.0-pretrained/resnet50-19c8e357.pth/>
    <https://github.com/OlafenwaMoses/ImageAI/releases/download/3.0.0-pretrained/inception_v3_google-1a9a5a14.pth/>
    <https://github.com/OlafenwaMoses/ImageAI/releases/download/3.0.0-pretrained/densenet121-a639ec97.pth/>
    <https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml>

* Create a new folder into AT19_MACHINE_LEARNING with a name "/files/NNM" and page the model files into NNM folder.

* on .env file you have to puth your paths acording to your pc.
    NNM_PATH=...........\AT19_MACHINE_LEARNING\files\NNM
    UPLOADS_PATH=...........\AT19_MACHINE_LEARNING\files\uploads
    RESPONSES_PATH=...........\AT19_MACHINE_LEARNING\files\responses

    PORT_ML=5000
    HOST_ML=127.0.0.1

* Create a virtual environment with version 3.8.8 of python and install the requirements.txt:
    python -m pip install virtualenv
    python -m virtualenv -p 3.8 venv
    source venv/scripts/activate  (BASH Console)   or      venv/scripts/active (CMD console)
    pip install cmake
    pip install -r requirements.txt

  Have a good day! :smiley:

NOTES.

We use 3 differents machine learning libraries, face_recognition, Imageai and deepface.
all of them suported by opencv. All the information below.

https://omes-va.com/deteccion-de-rostros-con-haar-cascades-python-opencv/
https://imageai.readthedocs.io/en/latest/index.html
https://github.com/serengil/deepface
https://github.com/ageitgey/face_recognition

---
---

# If the command pip list -r requirements.txt shows you installation errors, try it step by step:
pip install flask==2.2.2
pip install flask-restful==0.3.9
pip install deepface==0.0.75
pip install cmake==3.25.0
pip install face-recognition==1.3.0
pip install python-dotenv==0.21.0
pip install flask-swagger-ui==4.11.1
pip install cython pillow>=7.0.0 numpy>=1.18.1 opencv-python>=4.1.2 torch>=1.9.0 --extra-index-url https://download.pytorch.org/whl/cpu torchvision>=0.10.0 --extra-index-url https://download.pytorch.org/whl/cpu pytest==7.1.3 tqdm==4.64.1 scipy>=1.7.3 matplotlib>=3.4.3 mock==4.0.3
pip install imageai --upgrade
pip install opencv-python==4.6.0.66
pip install numpy==1.20.3pip install pymongo==4.3.3
pip install zope.interface==5.5.2pip install pytest-cov==4.0.0