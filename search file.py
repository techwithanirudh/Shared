# !unzip /content/term1-simulator-linux.zip
# !sudo apt install libgtk2.0-0 libsoup2.4-1 libarchive13 libpng16-16 libgconf-2-4 lib32stdc++6 libcanberra-gtk-module
# !~/Downloads/UnitySetup-2018.2.7f1
from os import walk

path = 'libGLU.so'

for (dirpath, dirnames, filenames) in walk('/'):
    conds0 = [len(dirpath) > 0, len(dirnames) > 0, len(filenames) > 0]
    conds1 = []
    if any(conds0):
      if len(dirpath) > 0:
        for path1 in dirpath:
          # print(path1)
          conds1.append(path1 == path)
      if len(dirnames) > 0:
        for path1 in dirnames:
          # print(path1)
          conds1.append(path1 == path)
      if len(filenames) > 0:
        for path1 in filenames:
          # print(path1)
          conds1.append(path1 == path)
      # print(conds1)
      if any(conds1):
        print('DirPath:', dirpath[0], 'DirName:', dirnames[0], 'Fname:', filenames[0])
      # print(dirpath[0], dirnames[0], filenames[0])
    # break
