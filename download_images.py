#!/usr/bin/python

import os
import time
import datetime

os.chdir("/home/root/DoeIce/scripts")

print("Removing any old images and downloading new one")
os.system("rm video.jpg")
os.system("wget http://root:root123@192.168.50.15/cgi-bin/viewer/video.jpg")
timestamp = time.time()
os.system("mv video.jpg ../remote_uploads/images/IMG_%s.jpg" % datetime.datetime.fromtimestamp(timestamp).strftime('%Y_%m_%d__%H_%M_%S'))
print("Got first image and moved to git repository. About to sleep")
time.sleep(5)

print("Removing first image and downloading new one")
os.system("rm video.jpg")
os.system("wget http://root:root123@192.168.50.16/cgi-bin/viewer/video.jpg")
timestamp = time.time()
os.system("mv video.jpg ../remote_uploads/images/IMG_%s.jpg" % datetime.datetime.fromtimestamp(timestamp).strftime('%Y_%m_%d__%H_%M_%S'))
print("Got second image and moved to git repository. About to sleep")
time.sleep(5)
print("Removing second image")
os.system("rm video.jpg")
