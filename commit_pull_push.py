import os
import time

os.chdir("/home/root/DoeIce/remote_uploads")
time.sleep(0.5)
os.system("git add images/*")
os.system("git commit -am 'Automatically uploading files'")
os.system("git pull")
os.system("git push")
