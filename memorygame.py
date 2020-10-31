testing = False
safe = True

from random import *
import time
import turtle
from tkinter import messagebox
import os
from myModules import certifi
from distutils.sysconfig import get_python_lib
import cv2
from fpdf import FPDF

imageFolder = 'data/Images/3'
pics = [0, 2]
dir = os.path.dirname(__file__) + '/' + imageFolder
os.chdir(dir)

img = '{}.gif'.format(randint(pics[0], pics[1]))
tiles = list(range(32)) * 2
correct = 0
state = {'mark': None}
hide = [True] * 64

def square(x, y):
    'Draw white square with black outline at (x, y).'
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.color('black', 'white')
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(50)
        turtle.left(90)
    turtle.end_fill()

def index(x, y):
    'Convert (x, y) coordinates to tiles index.'
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    'Convert tiles count to (x, y) coordinates.'
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    'Update mark and hidden tiles based on tap.'
    global correct, spot
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        correct += 1

    win = 31
    if testing:
        win = -2
    if correct > win:
        for _ in range(6):
            root.geometry('500x500+600+200')
            turtle.bgcolor('blue')
            time.sleep(0.5)
            turtle.bgcolor('green')
            time.sleep(0.5)

        date = time.strftime('%x')
        certifiPath = get_python_lib() + '/' + 'myModules' + '/' + 'certifi'
        certi = certifi.certifi(username, date, 'Anirudh Sriram', 'For Winning The \ln Memory Game')
        path = os.path.dirname(__file__) + '/{}Certificate.pdf'.format(username)
        while True:
            if os.path.isfile(path):
                replace = messagebox.askyesno('Replace', 'Do You Want To Replace {} With The Certificate?'.format(path))
                if replace:
                    break
                else:
                    if not safe:
                        while True:
                            path = turtle.textinput('Rename', 'Enter The Filename')
                            if path != None and path != '':
                                try:
                                    print(path.split('.pdf')[1])
                                except IndexError:
                                    path = path + '.pdf'
                                break
            else:
                break
        pdf = FPDF()
        imgpdf = '{}/tmp.png'.format(certifiPath)
        cv2.imwrite(imgpdf, certi)
        pdf.add_page()
        pdf.image(imgpdf, 10, 100, w=190, h=130)
        pimg = img
        pdf.add_page()
        pdf.image(pimg, 30, 100)
        pdf.output(path, 'F') 
        prev = messagebox.askyesno('Done', ('You Completed The Puzzle\nYou can find your certificate and image for winning the puzzle at {}\nWould You Like To Preview'.format(path)))
        if prev:
            cv2.imshow('Certificate', certi)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        rerun = messagebox.askyesno('Run', 'Would you like to re run the program?')
        if rerun == True:
            os.execl(os.sys.executable, os.sys.executable, *os.sys.argv)
        else:
            exit()

def complete():
    'Complete the puzzle'
    com = messagebox.askyesno('Complete', 'Are You Sure You Want To Complete the The Puzzle?')
    if com:
        index = 0
        for _ in range(64):
            hide[index] = False
            state['mark'] = None
            index += 1
    messagebox.showinfo('Exit', 'Click Ok To Exit')
    exit()

def draw():
    'Draw image and tiles.'
    turtle.clear()
    turtle.goto(0, 0)
    turtle.shape(img)
    turtle.stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)
    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        turtle.up()
        turtle.goto(x + 2, y)
        turtle.color('black')
        turtle.write(tiles[mark], font=('Arial', 30, 'normal'))

    turtle.update()
    turtle.ontimer(draw, 100)

def kOpen():
    messagebox.showinfo('Resume', 'Press Ok To Resume Game')

try:
    shuffle(tiles)
    canvas = turtle.getcanvas()
    root = canvas.winfo_toplevel()
    root.overrideredirect(1)
    root.geometry('420x420+600+250')
    turtle.addshape(img)
    turtle.hideturtle()
    turtle.tracer(False)
    turtle.onscreenclick(tap)
    draw()
    if not testing:
        while True:
            username = turtle.textinput('Name', 'Enter Your Name')
            if username != None and username != '' and len(username) > 5 and len(username) < 11:
                username = username.title()
                username = username.replace('%', '')
                break
    username = 'Tester'
    turtle.onkey(complete, 'c') 
    turtle.onkey(kOpen, 'space')
    turtle.listen() 
    turtle.done()
except Exception as e:
    print('Error: ', e)