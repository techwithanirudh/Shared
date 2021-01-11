import psutil
from tkinter import messagebox
import tkinter
import math
import time
# import subprocess

tkinter.Tk().withdraw()

cpu = 16
memory = '100 MB'
task = 'Teams.exe'
memory = [memory.split(' ')[0], memory.split(' ')[1]]

def bytesToSize(_bytes):
    sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
    if _bytes == 0:
        return '0 Byte';
    i = int(math.floor(math.log(_bytes) / math.log(1024)));
    return str(round(_bytes / math.pow(1024, i), 2)) + ' ' + sizes[i];

def convert(_memory):
    _memory = bytesToSize(int(_memory))
    _memory = _memory.split(' ')
    print(_memory)
    conds1 = [_memory[1] == memory[1], int(float(_memory[0])) - 1 > int(float(memory[0]))]
    print(_memory, memory)
    if all(conds1):
        return True
    return False

while True:
    for p in psutil.process_iter():
        if task in p.name():
            time.sleep(1)
            conds = [int(p.cpu_percent(0.1)) / 4 > cpu, convert(p.memory_info_ex()[0])]
            print(int(p.cpu_percent(0.1)) / 4, convert(p.memory_info_ex()[0]))
            if all(conds):
                if messagebox.askquestion('Close', f'Do You Want To Close {task}') != 'no':
                    messagebox.showinfo('Done', 'Closed')
                    # subprocess.call(["taskkill", "/F", "/IM", f"Teams.exe"])
                    # replace sub-proc-ess with subprocess  
