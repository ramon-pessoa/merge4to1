Merge4to1 system
===========================

## Merge4to1 system - Installation and Usage

System to merge 4 videos in 1 video.

![Merge 4 videos in 1 video](https://github.com/ramon-pessoa/merge4to1/blob/master/images/1-four_merged_videos.png)

### Table of contents

* [Merge4to1 installation steps on Windows](#merge4to1-installation-steps-on-windows)
* [Running the Merge4to1 system](#running-the-merge4to1-system)

#### Merge4to1 installation steps on Windows

1. Download the *merge4to1.py*, *videos.txt*, *requirements.txt* files available in
https://github.com/ramon-pessoa/merge4to1

2. Create a folder in your computer (for example *C:\merge_videos* folder) and put
the *merge4to1.py*, *requirements.txt*, and *videos.txt* files inside this folder.

![Create a folder in your computer](https://github.com/ramon-pessoa/merge4to1/blob/master/images/2.png)

3. Install python 3 (for example: Python 3.7.2) in your computer (To install python:
https://www.python.org/downloads/ )

![Install python 3](https://github.com/ramon-pessoa/merge4to1/blob/master/images/3.png)

    * Choose *Customize installation* and *Add Python 3.7 to PATH*

![Install python 3](https://github.com/ramon-pessoa/merge4to1/blob/master/images/4.png)

![Install python 3](https://github.com/ramon-pessoa/merge4to1/blob/master/images/5.png)

	* Change *Customize install location* to *C:\Python37* and press Install

![Install python 3](https://github.com/ramon-pessoa/merge4to1/blob/master/images/6.png)

![Install python 3](https://github.com/ramon-pessoa/merge4to1/blob/master/images/7.png)

![Install python 3](https://github.com/ramon-pessoa/merge4to1/blob/master/images/8.png)

4. Open the terminal/prompt/command line (Windows button > run > cmd > OK)

![Open the terminal](https://github.com/ramon-pessoa/merge4to1/blob/master/images/9.png)

5. Install *virtualenv* in your computer (*pip install virtualenv*)

![Install virtualenv](https://github.com/ramon-pessoa/merge4to1/blob/master/images/10.png)

6. Open the folder where the *merge4to1.py* is (for example, inside the command line,
*cd C:\merge_videos*)

![Open the folder](https://github.com/ramon-pessoa/merge4to1/blob/master/images/11.png)

7. In the command line (*C:\merge_videos*), type *virtualenv venv* to create a virtual environment

![Type virtualenv venv](https://github.com/ramon-pessoa/merge4to1/blob/master/images/12.png)

8. In the command line (*C:\merge_videos*), type *venv\Scripts\activate.bat* to activate
the virtual environment

![Activate
the virtual environment](https://github.com/ramon-pessoa/merge4to1/blob/master/images/13.png)

9. In the command line (*C:\merge_videos*), type *pip install -r requirements.txt* to install
the system requirements (*moviepy* dependency).

![pip install -r requirements.txt](https://github.com/ramon-pessoa/merge4to1/blob/master/images/14.png)

10. In the command line (*C:\merge_videos*), type *deactivate* to deactivate the virtual
environment

![Deactivate
the virtual environment](https://github.com/ramon-pessoa/merge4to1/blob/master/images/15.png)

**Note:** After all the above steps the *Merge4to1 system* will be installed and ready to use.

#### Running the Merge4to1 system

1. Open the terminal/prompt/command line (Windows button > run > cmd > OK)

![Open the terminal](https://github.com/ramon-pessoa/merge4to1/blob/master/images/9.png)

2. Open the folder where the *merge4to1.py* is (for example, inside the command line, *cd
C:\merge_videos*)

![Open the folder](https://github.com/ramon-pessoa/merge4to1/blob/master/images/11.png)

3. In the command line (*C:\merge_videos*), type *venv\Scripts\activate.bat* to activate the
virtual environment

![Activate
the virtual environment](https://github.com/ramon-pessoa/merge4to1/blob/master/images/13.png)

4. Update the *videos.txt* with the full path of the 4 videos (I recommend you copy the 4
videos to the folder (*C:\merge_videos*) and just type the name of the 4 videos in the
*videos.txt* file)

5. In the command line (C:\merge_videos), type: *python merge4to1.py* and press enter
    * The new merged video will be created in the same folder with the name
"YYYY-MM-DD HH:MM:SS.Millisecs#merge4to1.mp4" (for example: 2019-02-20
20-44-30.106004#merge4to1.mp4)

![python merge4to1.py](https://github.com/ramon-pessoa/merge4to1/blob/master/images/16.png)

#### Final notes

The system also works in Linux and MacOS

* Linux and MacOS commands:
    * Instead of **venv\Scripts\activate.bat**, use **source venv/bin/activate**