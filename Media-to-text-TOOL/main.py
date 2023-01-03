#=====================================
# from image & video to TEXT == TOOLS
#=====================================
from tkinter import *
import os.path
from tkinter import filedialog
import pytesseract
from PIL import Image
from tkinter import messagebox
#-------------------------------------
window1 = Tk()
window1.geometry('592x392')
window1.title('Media2Text')
window1.resizable(False, False)
window1.configure(bg='white')
#=====================================
# Please Download |
# https://osdn.net/projects/sfnet_tesseract-ocr-alt/downloads/tesseract-ocr-setup-3.02.02.exe/
#=== Define ==========================
def imo():
    file = filedialog.askopenfile(mode='r', filetypes=[('PNG Files','*.png')])
    if file:
        filepath = os.path.abspath(file.name)
        En1.insert(0,filepath)
#-------------------------------------
def ORC():
        pytesseract.pytesseract.tesseract_cmd= r"C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
        file = En1.get()
        savo = En2.get()
        lang = En3.get()
        img = Image.open(file)
        txt = pytesseract.image_to_string(img)
        with open(savo,"w") as f:
                f.write(txt)
        messagebox.showinfo('Umbrella','\n The File Saved')
#=== TOOLS----------------------------
F1 = Frame(window1,
        width=590,  
        height=395, 
        bg='white',
        bd=1,
        relief=SOLID)
F1.place(x=1,y=1)
text = Label(F1, 
             text='PROJ.pyEXTRACT TEXT FROM MEDIA|By Adel MD|wa.+967733477848',
             font=('times for roman', 13,'bold'),
             fg='black',
             bg='white')
text.place(x=1, y=4)
#-------------------------------------
En1_text = Label(F1, 
                 text='Image Path: ',
                 font=('times for roman', 11,'bold'), 
                 fg='black', 
                 bg='white')
En1_text.place(x=10,y=50)
En1 = Entry(F1, font=('times for roman', 16), width=30, bd=1, relief=SOLID)
En1.place(x=100,y=50)
#-------------------------------------------
btn1 = Button(F1, text='+', cursor='hand2', command=imo)
btn1.place(x=445,y=51)
#-------------------------------------------
En2_savo = Label(F1, 
                 text='Save  Path: ',
                 font=('times for roman', 11,'bold'), 
                 fg='black', 
                 bg='white')
En2_savo.place(x=10,y=84)
En2 = Entry(F1, font=('times for roman', 16), width=30, bd=1, relief=SOLID)
En2.place(x=100,y=84)
#-------------------------------------
En3_lang = Label(F1, 
                 text='Language : ',
                 font=('times for roman', 11,'bold'), 
                 fg='white', 
                 bg='green')
En3_lang.place(x=10,y=117)
En3 = Entry(F1, font=('times for roman', 16), width=30, bd=1, relief=SOLID)
En3.place(x=100,y=117)
#--------------------------------------
btn2 = Button(F1, text='EXTRACT TEXT', 
              fg='white', width=12, height=6, 
              bg='#393939', cursor='hand2', command=ORC) 
btn2.place(x=480,y=49)
#--------------------------------------
logo = PhotoImage(file='11.png')
logo_lbl = Label(window1,image=logo)
logo_lbl.place(x=100,y=158)
#--------------------------------------
window1.mainloop()
#--------------------------------------