from logging import root
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from details import Details
from tkinter import messagebox
import os
import numpy as np
import cv2

class Developer:
    def __init__(self, root):                     # root=Current_Window
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendance System")
        
        Title_label=Label(self.root,text="DEVELOPER",relief="groove",font=("Times New Roman",25,"bold"),fg="White",bg="Grey")
        Title_label.place(x=0,y=0,width=1530,height=45) 
        
        imagebg = Image.open(r"Face_Image\Developer1.jpg")
        imagebg = imagebg.resize((1530, 790), Image.LANCZOS)
        self.photoimagebg = ImageTk.PhotoImage(imagebg)

        top_img = Label(self.root, image=self.photoimagebg)
        top_img.place(x=0, y=45, width=1320, height=745)

        main_frame=Frame(self.root,bg="Grey")
        main_frame.place(x=1150,y=45,width=400,height=745)
        
        ################   inside main frame ################
        
        imageSelf = Image.open(r"Face_Image\Abhi.D Cartoon.png")
        imageSelf = imageSelf.resize((220, 250), Image.LANCZOS)
        self.photoimageSelf = ImageTk.PhotoImage(imageSelf)
        
        top_imgself = Label(main_frame, image=self.photoimageSelf)
        top_imgself.place(x=70, y=30, width=220, height=250)      
        
        Title_label1=Label(main_frame,text=" Hello this is Abhishek.D    ",font=("Times New Roman",25,"bold"),bg="Grey",fg="White")
        Title_label1.place(x=0,y=302) 
        
        Title_label2=Label(main_frame,text="(Developer of this Model)   ",font=("Times New Roman",25,"bold"),bg="Grey",fg="White")
        Title_label2.place(x=0,y=355) 
        
        imagetitle = Image.open(r"Face_Image\Dev.jpg")
        imagetitle = imagetitle.resize((380, 325), Image.LANCZOS)
        self.photoimagetitle = ImageTk.PhotoImage(imagetitle)

        topright_img = Label(self.root, image=self.photoimagetitle)
        topright_img.place(x=1150, y=465, width=380, height=325)
               
if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
