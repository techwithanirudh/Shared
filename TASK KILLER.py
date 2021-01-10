import psutil
from tkinter import messagebox
import tkinter
# import subprocess

tkinter.Tk().withdraw()

cpu = 10
memory = 1
task = 'Teams.exe'

while True:
    for p in psutil.process_iter():
        if task in p.name():
            conds = [int(p.cpu_percent(0.1)) / 4 > cpu, p.memory_percent() > memory]
            if all(conds):
                if messagebox.askquestion('Close', 'Do You Want To Close MS Teams') != 'no':
                    messagebox.showinfo('Done', 'Closed')
                    # sub-proc-ess.call(["taskkill", "/F", "/IM", f"{task}.exe"])
                    # replace sub-proc-ess with subprocess
