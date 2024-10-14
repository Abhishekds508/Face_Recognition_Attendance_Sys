from logging import root
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from details import Details
from tkinter import messagebox
import os
import numpy as np
import cv2

class Train:
    def __init__(self, root):                     # root=Current_Window
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendance System")

        imagetop=Image.open(r"Face_Image\Train4.jpg")
        imagetop=imagetop.resize((1530,300),Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(imagetop)
        
        f_label=Label(self.root,image=self.photoimage)
        f_label.place(x=0,y=0,width=1530,height=300)   
        
        btn_train=Button(self.root,bd=2,text="TRAIN DATA ",relief="groove",command=self.train_classifier,cursor="hand2",fg="RED",bg="White",font=("times new roman",22,"bold"))
        btn_train.place(x=0,y=300,width=1530,height=45)             
                
        imagebottom=Image.open(r"Face_Image\Face_recog5.jpg")
        imagebottom=imagebottom.resize((1530,520),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(imagebottom)
        
        f_label=Label(self.root,image=self.photoimage2)
        f_label.place(x=0,y=340,width=1530,height=450)

       ######## #######   Training the Clssifier  ########  ########
   
    def train_classifier(self):
    # Get the directory of the current script
        script_directory = os.path.dirname(os.path.abspath(__file__))      
        data_dir = os.path.join(script_directory, "Data")
        
        # List all files in the data directory
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        faces = []
        ids = []

        for image in path:
            try:
                # Convert image to grayscale
                img = Image.open(image).convert("L")
                imageNp = np.array(img, 'uint8')

                # Extract the ID from the filename (e.g., 'user.1.1.jpg' -> ID = 1)
                #filename = os.path.split(image)[1]
                id = int(os.path.split(image)[1].split('.')[1])  # Assuming the ID is the second part                
                faces.append(imageNp)
                ids.append(id)
                cv2.imshow("Training", imageNp)
                cv2.waitKey(1)
            except ValueError:
               # print(f"Filename '{filename}' does not contain a valid integer ID. Skipping this file.")
                continue
            
        ids = np.array(ids)
        # Check if there is enough data to train
        if len(faces) == 0 or len(ids) == 0:
            print("No valid training data found. Ensure that filenames are correctly formatted.")
            messagebox.showerror("Error", "No valid training data found.")
            return

        # Create LBPH face recognizer and train it with the images and IDs
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        classifier_path = os.path.join(script_directory, "Classifier.xml")
        clf.write(classifier_path)
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Datasets Completed")

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    #obj.train_classifier()
    root.mainloop()
