from logging import root
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import os
from details import Details
from train import Train
from face_recognition import Face_recognition
from developer import Developer
from attendance import Attendance

class Face_Recognition_System:
    def __init__(self, root):                     # root=Current_Window
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendance System")
        
        image=Image.open(r"Face_Image\Image1.png")
        image=image.resize((300,150),Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(image)
        
        f_label=Label(self.root,image=self.photoimage)
        f_label.place(x=0,y=0,width=260,height=130)
        
        image1=Image.open(r"Face_Image\Image4.png")
        image1=image1.resize((300,150),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(image1)
        
        f_label=Label(self.root,image=self.photoimage1)
        f_label.place(x=260,y=0,width=260,height=130)
        
        image2=Image.open(r"Face_Image\Image6.png")
        image2=image2.resize((500,150),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(image2)
        
        f_label=Label(self.root,image=self.photoimage2)
        f_label.place(x=520,y=0,width=500,height=130)
        
        image3=Image.open(r"Face_Image\Image5.png")
        image3=image3.resize((300,150),Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(image3)
        
        f_label=Label(self.root,image=self.photoimage3)
        f_label.place(x=1020,y=0,width=275,height=130)  
        
        image4=Image.open(r"Face_Image\Image3.png")
        image4=image4.resize((300,150),Image.LANCZOS)
        self.photoimage4=ImageTk.PhotoImage(image4)
        
        f_label=Label(self.root,image=self.photoimage4)
        f_label.place(x=1295,y=0,width=275,height=130) 
          
        #Background Image
        imagebg=Image.open(r"Face_Image\BG1.jpg")
        imagebg=imagebg.resize((1540,710),Image.LANCZOS)
        self.photoimagebg=ImageTk.PhotoImage(imagebg)
        
        bg_img=Label(self.root,image=self.photoimagebg)
        bg_img.place(x=0,y=130,width=1540,height=710)  
        
        Title_label=Label(bg_img,text="FACIAL  RECOGNITION  ATTENDANCE  SYSTEM",font=("Times New Roman",35,"bold"),fg="white",bg="red")
        Title_label.place(x=0,y=0,width=1530,height=45)  
        
        #Details Section_1
        imagedetails=Image.open(r"Face_Image\Employee_Details.PNG")
        imagedetails=imagedetails.resize((180,180),Image.LANCZOS)
        self.imagedetails=ImageTk.PhotoImage(imagedetails)
        
        btn1=Button(bg_img,command=self.employee_details,image=self.imagedetails,cursor="hand2")
        btn1.place(x=200,y=100,width=180,height=180)
        
        btn1_Label=Button(bg_img,text="Details",command=self.employee_details,cursor="hand2",font=("Times New Roman",18,"bold"),fg="white",bg="NavyBlue")
        btn1_Label.place(x=200,y=280,width=180,height=30)
        
        imageDetection=Image.open(r"Face_Image\Image7.PNG")
        imageDetection=imageDetection.resize((180,180),Image.LANCZOS)
        self.imageDetection=ImageTk.PhotoImage(imageDetection)
        
        btn2=Button(bg_img,image=self.imageDetection,command=self.face_data,cursor="hand2")
        btn2.place(x=520,y=100,width=180,height=180)
        
        btn2_Label=Button(bg_img,text="Face Detection",cursor="hand2",command=self.face_data,font=("Times New Roman",18,"bold"),fg="white",bg="NavyBlue")
        btn2_Label.place(x=520,y=280,width=180,height=30)
        
        imageAttendance=Image.open(r"Face_Image\attendance.PNG")
        imageAttendance=imageAttendance.resize((180,180),Image.LANCZOS)
        self.imageAttendance=ImageTk.PhotoImage(imageAttendance)
        
        btn3=Button(bg_img,image=self.imageAttendance,cursor="hand2",command=self.attendance)
        btn3.place(x=860,y=100,width=180,height=180)
        
        btn3_Label=Button(bg_img,text="Attendance",cursor="hand2",font=("Times New Roman",18,"bold"),fg="white",bg="NavyBlue")
        btn3_Label.place(x=860,y=280,width=180,height=30)
        
        imageTraining=Image.open(r"Face_Image\Train.PNG")
        imageTraining=imageTraining.resize((180,180),Image.LANCZOS)
        self.imageTraining=ImageTk.PhotoImage(imageTraining)
        
        btn4=Button(bg_img,image=self.imageTraining,cursor="hand2",command=self.train)
        btn4.place(x=1200,y=100,width=180,height=180)
        
        btn4_Label=Button(bg_img,text="Training Data",command=self.train,cursor="hand2",font=("Times New Roman",18,"bold"),fg="white",bg="NavyBlue")
        btn4_Label.place(x=1200,y=280,width=180,height=30)
        
        imagePhotos=Image.open(r"Face_Image\Photos.PNG")
        imagePhotos=imagePhotos.resize((220,220),Image.LANCZOS)
        self.imagePhotos=ImageTk.PhotoImage(imagePhotos)
               
        btn5=Button(bg_img,image=self.imagePhotos,cursor="hand2",command=self.open_img)
        btn5.place(x=250,y=380,width=180,height=180)
        
        btn5_Label=Button(bg_img,text="Photos",cursor="hand2",font=("Times New Roman",20,"bold"),fg="white",bg="NavyBlue",command=self.open_img)
        btn5_Label.place(x=250,y=560,width=180,height=30)
        
        imageDeveloper=Image.open(r"Face_Image\Dev1.jpg")
        imageDeveloper=imageDeveloper.resize((220,220),Image.LANCZOS)
        self.imageDeveloper=ImageTk.PhotoImage(imageDeveloper)
               
        btn6=Button(bg_img,image=self.imageDeveloper,cursor="hand2",command=self.developer)
        btn6.place(x=650,y=380,width=180,height=180)
        
        btn6_Label=Button(bg_img,text="Developer",cursor="hand2",font=("Times New Roman",20,"bold"),fg="white",bg="NavyBlue",command=self.developer)
        btn6_Label.place(x=650,y=560,width=180,height=30)
        
        imageExit=Image.open(r"Face_Image\Exit1.jpg")
        imageExit=imageExit.resize((180,180),Image.LANCZOS)
        self.imageExit=ImageTk.PhotoImage(imageExit)
        
        btn7=Button(bg_img,image=self.imageExit,cursor="hand2",command=self.iExit)
        btn7.place(x=1080,y=380,width=180,height=180)
        
        btn7_Label=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("Times New Roman",20,"bold"),fg="white",bg="NavyBlue")
        btn7_Label.place(x=1080,y=560,width=180,height=30)
                 
    def open_img(self):
        data_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Data")
        if os.path.exists(data_directory):
            os.startfile(data_directory)
        else:
            messagebox.showerror("Error", f"The directory 'Data' was not found.\nExpected location: {data_directory}")
    
    def iExit(self):
        self.iExit=messagebox.askyesno("Face_Recognition","Do you want to exit",parent=self.root)
        if(self.iExit>0):
            self.root.destroy() 
        else:
            return    
                            
 ####################  Details_call ##########################     
    
    def employee_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Details(self.new_window)                 
          
    def train(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window)
        
    def developer(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
    
    def attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)   
       
if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()