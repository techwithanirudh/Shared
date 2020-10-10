# ffmpeg -i input.mp4 output.mp4

from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
import cv2
from fpdf import FPDF
import threading

TITLE = 'Desktop Scanner'

def splashScreen():
    global splashScreenTk
    splashScreenTk = tk.Tk()
    splashScreenTk.geometry('600x400+500+250')
    splashScreenTk.overrideredirect(1)
    splashScreenTk.configure(bg='darkblue')

    lblTitle = tk.Label(splashScreenTk, fg='white', bg='darkblue', font=('arial', 40, 'bold'), text='\n' * 2 + TITLE) 
    lblTitle.pack() 

    lblCreatedBy = tk.Label(splashScreenTk, fg='white', bg='darkblue', font=('arial', 15, 'bold'), text='\n' * 6 + '© 2020 Anirudh Sriram')
    lblCreatedBy.pack()

    splashScreenTk.mainloop()

_splashScreen = threading.Thread(target=splashScreen)
_splashScreen.start()
cam = cv2.VideoCapture(0)
splashScreenTk.withdraw()
saveWin = filedialog.Tk()
saveWin.withdraw()
imglist = []

while True:
    ret, frame = cam.read()
    if not ret:
        break

    cv2.imshow(TITLE, frame)
    key = cv2.waitKey(25)

    if key == 27:
        break
    elif key == ord('s'):
        cv2.destroyAllWindows()
        imgname = filedialog.asksaveasfilename(filetypes=[('PNG', '*.png')])

        if imgname != '':
            if not imgname.endswith('.png'):
                imgname = imgname + '.png'

            cv2.imwrite(imgname, frame) 
            imglist.append(imgname)
    elif key == ord('p'):
        if imglist:
            cv2.destroyAllWindows()
            pdfpath = filedialog.asksaveasfilename(filetypes=[('PDF Files', '*.pdf')])

            if pdfpath != '':
                if not pdfpath.endswith('.pdf'):
                    pdfpath = pdfpath + '.pdf'

                    pdf = FPDF()

                    for img in imglist:
                        pdf.add_page()
                        pdf.image(img, 30, 20, 150, 150)

                    pdf.output(pdfpath, 'F') 
                    imglist = []
        else:
            messagebox.showerror(TITLE, 'Cannot Convert Images To PDF Because No Images Were Saved!')

cam.release()
cv2.destroyAllWindows()