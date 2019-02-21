#!/usr/bin/env python

"""merge4to1.py: Merge 4 videos in 1 video."""

__author__      = "Ramon Figueiredo Pessoa"
__copyright__   = "Copyright 2019, RFP Intelligent Systems"
__credits__ = ["Ramon Figueiredo Pessoa"]
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = "Ramon Figueiredo Pessoa"
__email__ = "ramon.fgrd@gmail.com"
__status__ = "Production"

from moviepy.editor import VideoFileClip, clips_array
from datetime import datetime

print(__doc__, "Version: " + __version__)

video_list = []
file = open("videos.txt")
for f in file:
    video_list.append(f)
file.close()

clip1 = VideoFileClip(video_list[0].replace("\n", ""))
clip2 = VideoFileClip(video_list[1].replace("\n", ""))
clip3 = VideoFileClip(video_list[2].replace("\n", ""))
clip4 = VideoFileClip(video_list[3].replace("\n", ""))
final_clip = clips_array([[clip1, clip2],
                          [clip3, clip4]])

output_filename = str(datetime.today()).replace(":", "-") + "#merge4to1.mp4"

final_clip.resize(width=988).write_videofile(output_filename)