import os
import threading
import time
import tkinter.messagebox
from tkinter import *
from tkinter import filedialog
import moviepy.editor as mp
from tkinter import ttk
from ttkthemes import themed_tk as tk
from pygame import mixer
os.add_dll_directory(os.path.dirname(__file__) + '/VLC')
import vlc

os.chdir(os.path.dirname(__file__))

root = tk.ThemedTk()
root.get_themes()                 # Returns a list of all themes that can be set
root.set_theme("radiance")         # Sets an available theme

# Fonts - Arial (corresponds to Helvetica), Courier New (Courier), Comic Sans MS, Fixedsys,
# MS Sans Serif, MS Serif, Symbol, System, Times New Roman (Times), and Verdana
#
# Styles - normal, bold, roman, italic, underline, and overstrike.

# Create the menubar
menubar = Menu(root)
root.config(menu=menubar)

# Create the submenu

subMenu = Menu(menubar, tearoff=0)

playlist = []
played = False
paused = False
paused1 = True
stop = False
first = 1
first1 = True

# playlist - contains the full path + filename
# playlistbox - contains just the filename
# Fullpath + filename is required to play the music inside play_music load function

def browse_file():
    global filename_path
    filename_path = filedialog.askopenfilename()
    add_to_playlist(filename_path)

def add_to_playlist(filename):
    filename = os.path.basename(filename)
    index = 0
    playlistbox.insert(index, filename)
    playlist.insert(index, filename_path)
    index += 1


menubar.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Open", command=browse_file)
subMenu.add_command(label="Exit", command=root.destroy)


def about_us():
    tkinter.messagebox.showinfo('About Melody', 'This is a music media_player build using Python Tkinter by @attreyabhatt')


subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=subMenu)
subMenu.add_command(label="About Us", command=about_us)

mixer.init()  # initializing the mixer

root.title("Melody")
root.iconbitmap(r'images/melody.ico')

# Root Window - StatusBar, LeftFrame, RightFrame
# LeftFrame - The listbox (playlist)
# RightFrame - TopFrame,MiddleFrame and the BottomFrame

leftframe = Frame(root)
leftframe.pack(side=LEFT, padx=30, pady=30)

playlistbox = Listbox(leftframe)
playlistbox.pack()

addBtn = ttk.Button(leftframe, text="+ Add", command=browse_file)
addBtn.pack(side=LEFT)


def del_song():
    selected_song = playlistbox.curselection()
    selected_song = int(selected_song[0])
    playlistbox.delete(selected_song)
    playlist.pop(selected_song)


delBtn = ttk.Button(leftframe, text="- Del", command=del_song)
delBtn.pack(side=LEFT)

rightframe = Frame(root)
rightframe.pack(pady=30)

topframe = Frame(rightframe)
topframe.pack()

lengthlabel = ttk.Label(topframe, text='Total Length : --:--')
lengthlabel.pack(pady=5)

currenttimelabel = ttk.Label(topframe, text='Current Time : --:--', relief=GROOVE)
currenttimelabel.pack()


def show_details(play_song):
    global clip, t1
    file_data = os.path.splitext(play_song)
    types = ['.mp4', '.mov', '.mpg', '.wmv', '.rm']
    if file_data[1].lower() in types:
        clip = mp.VideoFileClip(play_song)
        total_length = clip.duration
    else:
        clip = mp.AudioFileClip(play_song)
        total_length = clip.duration
    # div - total_length/60, mod - total_length % 60
    mins, secs = divmod(total_length, 60)
    mins = round(mins)
    secs = round(secs)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    lengthlabel['text'] = "Total Length" + ' - ' + timeformat

    t1 = threading.Thread(target=start_count, args=(total_length,))
    t1.start()


def start_count(t):
    global first1, current_time, stop
    # mixer.music.get_busy(): - Returns False when we press the stop button (music stop playing)
    # Continue - Ignores all of the statements below it. We check if music is paused or not.
    current_time = 0
    while current_time <= t:
        # print('yo', paused)
        if not paused:
            print('playing', paused)
            mins, secs = divmod(current_time, 60)
            mins = round(mins)
            secs = round(secs)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            currenttimelabel['text'] = "Current Time" + ' - ' + timeformat
            time.sleep(1)
            current_time += 1
        if stop: 
            break

def play_music():
    global media_player, played, paused1, playBtn, first, paused, stop

    # stop_music()
    # time.sleep(1)
    if not played:
        stop = False
        selected_song = playlistbox.curselection()
        selected_song = int(selected_song[0])
        play_it = playlist[selected_song]
        show_details(play_it)
        media_player = vlc.MediaPlayer(play_it)
        media_player.play() 
        media_player.audio_set_volume(70)
        played = True
        first -= 1
        playBtn.config(image=pausePhoto)
    else:
        while True:
            print(first)
            if first < 1:
                playBtn.config(image=playPhoto)
                first = 2
                paused = True
                print('non in ai1')
                break
            if not paused1:
                paused1 = True
                paused = True
                playBtn.config(image=playPhoto)
                print('non in')
                break
            if paused1:
                paused1 = False
                playBtn.config(image=pausePhoto)
                paused = False
                print('inomamabrosyo', paused)
                break
        media_player.pause()

def stop_music():
    global played, playBtn, paused, current_time, playlist, first, first1, paused1, t1, stop, lengthlabel, currenttimelabel
    # mixer.music.stop()
    played = False
    paused = False
    paused1 = True
    first = 1
    first1 = True
    stop = True
    t1.join() 
    lengthlabel.config(text='Total Length : --:--')
    currenttimelabel.config(text='Current Time : --:--')
    media_player.stop()
    playBtn.config(image=playPhoto)

def rewind_music():
    play_music()

def set_vol(val):
    global volume
    volume = int(float(val))
    media_player.audio_set_volume(volume)
    # set_volume of mixer takes value only from 0 to 1. Example - 0, 0.1,0.55,0.54.0.99,1

muted = False

def mute_music():
    global muted
    if muted:  # Unmute the music
        media_player.audio_set_volume(70)
        volumeBtn.configure(image=volumePhoto)
        scale.set(70)
        muted = False
    else:  # mute the music
        media_player.audio_set_volume(0)
        volumeBtn.configure(image=mutePhoto)
        scale.set(0)
        muted = True

middleframe = Frame(rightframe)
middleframe.pack(pady=30, padx=30)

playPhoto = PhotoImage(file='images/play.png')
pausePhoto = PhotoImage(file='images/pause.png')
playBtn = ttk.Button(middleframe, image=playPhoto, command=play_music)
playBtn.grid(row=0, column=0, padx=10)

stopPhoto = PhotoImage(file='images/stop.png')
stopBtn = ttk.Button(middleframe, image=stopPhoto, command=stop_music)
stopBtn.grid(row=0, column=1, padx=10)

# pauseBtn = ttk.Button(middleframe, image=pausePhoto, command=pause_music)
# pauseBtn.grid(row=0, column=2, padx=10)

# Bottom Frame for volume, rewind, mute etc.

bottomframe = Frame(rightframe)
bottomframe.pack()

# rewindPhoto = PhotoImage(file='images/rewind.png')
# rewindBtn = ttk.Button(bottomframe, image=rewindPhoto, command=rewind_music)
# rewindBtn.grid(row=0, column=0)

mutePhoto = PhotoImage(file='images/mute.png')
volumePhoto = PhotoImage(file='images/volume.png')
volumeBtn = ttk.Button(bottomframe, image=volumePhoto, command=mute_music)
volumeBtn.grid(row=0, column=1)

scale = ttk.Scale(bottomframe, from_=0, to=150, orient=HORIZONTAL, command=set_vol)
scale.set(70)  # implement the default value of scale when music media_player starts
scale.grid(row=0, column=2, pady=15, padx=30)


def on_closing():
    stop_music()
    root.destroy()


root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
