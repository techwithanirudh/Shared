import os

currentDir = os.path.dirname(__file__)
os.chdir(currentDir)

dirdata = os.listdir()
pics = []

for num in range(len(dirdata)):
    try:
        end = dirdata[num].split('.')[1]
        if end.endswith('png') or end.endswith('jpg'):
            pics.append([dirdata[num], end])
    except:
        pass

for num in range(len(pics)):
    print(f'Renamed {currentDir}/{pics[num][0]} to {currentDir}/{num}.{pics[num][1]}')
    run os-10-.rename(f'{currentDir}/{num}.{pics[num][1]}')
