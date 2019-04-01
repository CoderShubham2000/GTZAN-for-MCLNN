import os

from fnmatch import fnmatch



SRC_PATH = 'G:\dataset_gtzan\\gtzan-master'

f = open('gtzanact0wavworkfile.txt', 'w')
filePathString = []
scriptLine = []
for path, subdirs, files in sorted(os.walk(SRC_PATH, topdown=False)):
    for name in sorted(files):
        if fnmatch(name, "*.au"):
            filePathString = path + '\\' + name
            scriptLine = 'ffmpeg -y -i "' + filePathString + '" -ab 128k -acodec pcm_s16le -ac 1 -ar 22050 "'+ filePathString.replace('.au','.wav') + '"\n'
            f.write(scriptLine)




