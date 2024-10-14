import threading
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import os
import cv2
import mysql.connector
# from mtcnn import MTCNN
import concurrent.futures
import time

class Attendance:
    def __init__(self, root):  # root=Current_Window
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendance System")
        
        Title_label=Label(self.root,text="Attendance Management System",font=("Times New Roman",35,"bold"),bg="Red",fg="White")
        Title_label.place(x=0,y=0,width=1530,height=50)  
    
        image1=Image.open(r"Face_Image\Attendance8.png")
        image1=image1.resize((510,300),Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(image1)
        
        f_label1=Label(self.root,image=self.photoimage)
        f_label1.place(x=510,y=50,width=510,height=300)  
        
        image2=Image.open(r"Face_Image\Attendance.jpeg")
        image2=image2.resize((510,300),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(image2)
        
        f_label2=Label(self.root,image=self.photoimage2)
        f_label2.place(x=0,y=51,width=510,height=300) 
        
        image3=Image.open(r"Face_Image\new_attend.png")
        image3=image3.resize((510,300),Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(image3)
        
        f_label3=Label(self.root,image=self.photoimage3)
        f_label3.place(x=1020,y=51,width=510,height=300) 
        
        main_frame_left=Frame(self.root,border=1)
        main_frame_left.place(x=0,y=351,width=525,height=385)
        
        Left_frame=LabelFrame(main_frame_left,bd=2,text="Employee Attendance",relief="groove",font=("Times New Roman",15,"bold"))
        Left_frame.place(x=10,y=10,width=515,height=270)
        
        Name_frame_lbl=Label(Left_frame,text="Name",font=("times new roman",12,"bold"))
        Name_frame_lbl.grid(row=0,column=1,padx=3,pady=2,sticky=NSEW) 
        
        Entry_field_Name=ttk.Entry(Left_frame,width=20,font=("times new roman",12,"bold"))
        Entry_field_Name.grid(row=0,column=2,padx=3,pady=15,sticky=NSEW)
        
        Id_frame_lbl=Label(Left_frame,text="ID",font=("times new roman",12,"bold"))
        Id_frame_lbl.grid(row=0,column=3,padx=3,pady=2,sticky=NSEW)

        Entry_field_Id = ttk.Entry(Left_frame, width=20, font=("times new roman", 12, "bold"))
        Entry_field_Id.grid(row=0, column=4, padx=3, pady=15, sticky=NSEW)
        
        Dept_frame_lbl=Label(Left_frame,text="Department",font=("times new roman",12,"bold"))
        Dept_frame_lbl.grid(row=1,column=1,padx=5,pady=2,sticky=NSEW)
        
        Entry_field_Dept = ttk.Entry(Left_frame, width=20, font=("times new roman", 12, "bold"))
        Entry_field_Dept.grid(row=1, column=2, padx=3, pady=15, sticky=NSEW)
        
        Time_frame_lbl=Label(Left_frame,text="Time",font=("times new roman",12,"bold"))
        Time_frame_lbl.grid(row=2,column=3,padx=3,pady=2,sticky=NSEW)
        
        Entry_field_Time = ttk.Entry(Left_frame, width=20, font=("times new roman", 12, "bold"))
        Entry_field_Time.grid(row=2, column=4, padx=3, pady=15, sticky=NSEW)
        
        Date_frame_lbl=Label(Left_frame,text="Date",font=("times new roman",12,"bold"))
        Date_frame_lbl.grid(row=2,column=1,padx=3,pady=2,sticky=NSEW)
        
        Entry_field_Date = ttk.Entry(Left_frame, width=20, font=("times new roman", 12, "bold"))
        Entry_field_Date.grid(row=2, column=2, padx=3, pady=15, sticky=NSEW)        
        
        Attendance_Status_lbl=Label(Left_frame,text="Status",font=("times new roman",12,"bold"))
        Attendance_Status_lbl.grid(row=3,column=1,padx=3)  
        
        Attendance_Status_combo=ttk.Combobox(Left_frame,font=("times new roman",12,"bold "),state="read only")
        Attendance_Status_combo["values"]=("Select Status","Present","Absent","Left")
        #Attendance_Status_combo.current(0)
        Attendance_Status_combo.grid(row=3,column=2,padx=5,pady=15)  
        
        btn_frame=Frame(self.root,bd=1,relief="ridge") 
        btn_frame.place(x=15,y=640,width=495,height=50)
        
        btn_save=Button(btn_frame,bd=2,text="Save",width=15,fg="Red",bg="White",font=("times new roman",10,"bold"))
        btn_save.grid(row=1,column=1,padx=2)
        
        btn_Update=Button(btn_frame,bd=2,text="Update",width=16,fg="Red",bg="White",font=("times new roman",10,"bold"))
        btn_Update.grid(row=1,column=2,padx=2)
        
        btn_Del=Button(btn_frame,bd=2,text="Delete",width=16,fg="Red",bg="White",font=("times new roman",10,"bold"))
        btn_Del.grid(row=1,column=3,padx=1)
        
        btn_Reset=Button(btn_frame,bd=2,text="Reset",width=15,fg="Red",bg="White",font=("times new roman",10,"bold"))
        btn_Reset.grid(row=1,column=4,padx=2)
        
        main_frame_right=Frame(self.root,border=2)
        main_frame_right.place(x=530,y=355,width=995,height=440)
        
        Table_frame=Frame(main_frame_right,border=2,relief="ridge")
        Table_frame.place(x=5,y=15,width=980,height=400)
        
        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        
        self.employee_table=ttk.Treeview(Table_frame,column=("Dept","ID","Designation","Name","Gender","DOB","Address","Phone_No"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)          
        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)
           
        
        # Right_frame=LabelFrame(main_frame_right,bd=2,background="wHITE",text="Employee Attendance",relief=RIDGE,font=("Times New Roman",15,"bold"))
        # Right_frame.place(x=950,y=51,width=400,height=710)
        
        # imagebg=Image.open(r"Face_Image\bg.png")
        # imagebg=imagebg.resize((550,790),Image.LANCZOS)
        # self.photoimagebg=ImageTk.PhotoImage(imagebg)
        
        # bg_img=Label(self.root,image=self.photoimagebg)
        # bg_img.place(x=0,y=51,width=550,height=790)  
        
        #main_frame=Frame(self.root,border=2)
        #main_frame.place(x=0,y=51,width=500,height=410)
        
        # Left_frame=LabelFrame(main_frame,bd=2,text="Employee Details",relief="flat",font=("Times New Roman",15,"bold"))
        # Left_frame.place(x=10,y=10,width=680,height=580)
        
        # main_frame=Frame(bg_img,border=2)
        # main_frame.place(x=0,y=51,width=1530,height=710)
        
        # Left_frame=LabelFrame(main_frame,bd=2,text="Employee Details",relief="flat",font=("Times New Roman",15,"bold"))
        # # Left_frame.place(x=10,y=10,width=740,height=580)

        # imageLeft=Image.open(r"Face_Image\Details.png")
        # imageLeft=imageLeft.resize((720,190),Image.LANCZOS)
        # self.photoimageLeft=ImageTk.PhotoImage(imageLeft)
        
        # Leftimg_lbl=Label(Left_frame,image=self.photoimageLeft)
        # Leftimg_lbl.place(x=10,y=5,width=720,height=190)  



if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()