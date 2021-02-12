# Exercise: If you check for files in C:/ Write Code To Ignore Sytem Files And Add The Code In The Issue Called C Drive Avoid System Files
import os 

os.chdir(os.path.dirname(__file__))

print('Big Files Finder\nIgnore the first file as it could be big or not\n\n\n')
path = 'D:/'
size = 0
max_size = 0
max_file = ''

for folder, subfolders, files in os.walk(path): 
    for file in files: 
        try:
            size = os.stat(os.path.join(folder, file)).st_size
            if size > max_size: 
                max_size = size 
                max_file = os.path.join(folder, file) 
                if max_file == 'D:/pagefile.sys':
                    max_size = 0
                    continue
                print('Big File Path:', max_file, 'Size:', max_size)
        except FileNotFoundError:
            print('Error: ', file)
