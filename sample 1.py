from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
import cv2
from fpdf import FPDF
import time
import numpy as np
import requests

requests.urllib3.disable_warnings()

TITLE = 'Desktop Scanner'
END = 'end-1c'

def read(ip):
    '''
    Give the current Ip of IpWebcam and it will return the current frame
    '''
    url = f'https://{ip}:8080/shot.jpg'

    while True:
        raw_data = requests.get(url, verify=False)
        image_array = np.array(bytearray(raw_data.content), dtype=np.uint8)
        frame = cv2.imdecode(image_array, -1)
        frame = cv2.resize(frame, (640, 380))
        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)

        return frame

splashScreen = tk.Tk()
splashScreen.geometry('600x400+500+250')
splashScreen.overrideredirect(1)
splashScreen.configure(bg='darkblue')

lblTitle = tk.Label(splashScreen, fg='white', bg='darkblue', font=('arial', 40, 'bold'), text='\n' * 2 + TITLE) 
lblTitle.pack() 

lblCreatedBy = tk.Label(splashScreen, fg='white', bg='darkblue', font=('arial', 15, 'bold'), text='\n' * 6 + '© 2020 Anirudh Sriram')
lblCreatedBy.pack()

def destroySp():
    splashScreen.destroy()

splashScreen.after(6000, destroySp)
splashScreen.mainloop()

ipTk = tk.Tk()
ipTk.geometry('125x50+750+500')
ipTk.overrideredirect(1)
ipTk.title('Localhost Address For Connecting')
ipTxtBox = tk.Text(ipTk, font=('arial', 12, 'bold'), width=14, height=1)
ipTxtBox.pack()

def destroyIp():
    global ip

    ip = ipTxtBox.get(1.0, END)
    ipTk.withdraw()
    messagebox.showinfo('Info', 'Connecting. Please Wait...')
    ipTk.destroy()

connectBtn = tk.Button(ipTk, command=destroyIp, text='Connect')
connectBtn.pack()
ipTk.mainloop()

saveWin = filedialog.Tk()
saveWin.withdraw()
imglist = []

while True:
    ex = False
    mTime = 59
    sTime = time.time()

    while True:
        try:
            frame = read(ip)
            break
        except:
            cTime = time.time()
            if cTime - sTime > mTime:
                messagebox.showerror('Error', f'Could\'nt Connect To {ip} Please Try Again Later.')
                ex = True
                break

    if ex:
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
                        # pdf.image(img, 30, 20, 150, 150)
                        pdf.image(img, 30, 20)

                    pdf.output(pdfpath, 'F') 
                    imglist = []
        else:
            messagebox.showerror(TITLE, 'Cannot Convert Images To PDF Because No Images Were Saved!')

cv2.destroyAllWindows()