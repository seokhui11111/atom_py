import os
import subprocess
import pytube

yt=pytube.YouTube("https://youtu.be/CTRO5NXmAp8")
vids=yt.streams.all()

for i in range(len(vids)):
    print(i,',',vids[i])

new_filename
parentt_dir="D:/atom_py/"

vids[0].download(parent_dir)

default_filename=vids[0].default_filename
subprocess.call(['ffmpeg','-i',os.path.join(parent_dir,default_filename),os.path.join(parent_dir,new_m)])

print('동영상 다운로드 및 변환 완료')
