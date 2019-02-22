Merge4to1 system
===========================

## Merge4to1 system - Installation and Usage

System to merge 4 videos in 1 video.

![Merge 4 videos in 1 video](https://github.com/ramon-pessoa/merge4to1#running-the-merge4to1-system/images/1-four_merged_videos.png)

### Table of contents

* [Merge4to1 installation steps on Windows](#merge4to1-installation-steps-on-windows)
* [Running the Merge4to1 system](#running-the-merge4to1-system)

#### Merge4to1 installation steps on Windows

1. Download the *merge4to1.py*, *videos.txt*, *requirements.txt* files available in
https://github.com/ramon-pessoa/merge4to1

2. Create a folder in your computer (for example *C:\merge_videos* folder) and put
the *merge4to1.py*, *requirements.txt*, and *videos.txt* files inside this folder.

3. Install python 3 (for example: Python 3.7.2) in your computer (To install python:
https://www.python.org/downloads/ )

    * Choose *Customize installation* and *Add Python 3.7 to PATH*
    * Change *Customize install location* to *C:\Python37* and press Install

4. Open the terminal/prompt/command line (Windows button > run > cmd > OK)

5. Install *virtualenv* in your computer (*pip install virtualenv*)

6. Open the folder where the *merge4to1.py* is (for example, inside the command line,
*cd C:\merge_videos*)

7. In the command line (*C:\merge_videos*), type *virtualenv venv* to create a virtual environment

8. In the command line (*C:\merge_videos*), type *venv\Scripts\activate.bat* to activate
the virtual environment

9. In the command line (*C:\merge_videos*), type *pip install -r requirements.txt* to install
the system requirements (*moviepy* dependency).

10. In the command line (*C:\merge_videos*), type *deactivate* to deactivate the virtual
environment

**Note:** After all the above steps the *Merge4to1 system* will be installed and ready to use.

#### Running the Merge4to1 system

1. Open the terminal/prompt/command line (Windows button > run > cmd > OK)

2. Open the folder where the *merge4to1.py* is (for example, inside the command line, *cd
C:\merge_videos*)

3. In the command line (*C:\merge_videos*), type *venv\Scripts\activate.bat* to activate the
virtual environment

4. Update the *videos.txt* with the full path of the 4 videos (I recommend you copy the 4
videos to the folder (*C:\merge_videos*) and just type the name of the 4 videos in the
*videos.txt* file)

5. In the command line (C:\merge_videos), type: *python merge4to1.py* and press enter
    * The new merged video will be created in the same folder with the name
"YYYY-MM-DD HH:MM:SS.Millisecs#merge4to1.mp4" (for example: 2019-02-20
20-44-30.106004#merge4to1.mp4)

#### Final notes

The system also works in Linux and MacOS

* Linux and MacOS commands:
    * Instead of **venv\Scripts\activate.bat**, use **source venv/bin/activate**