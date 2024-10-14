
############ All OK   ###############

from logging import root
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os

class Details:
    def __init__(self, root):                     
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendance System")
        
        self.variable_dept=StringVar()
        self.variable_id=StringVar()
        self.variable_designation=StringVar()
        self.variable_name=StringVar()
        self.variable_Gender=StringVar()
        self.variable_DOB=StringVar()
        self.variable_Phone_No=StringVar()
        self.variable_Address=StringVar() 
        
        image=Image.open(r"Face_Image\Employee1.png")
        image=image.resize((300,150),Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(image)
        
        f_label=Label(self.root,image=self.photoimage)
        f_label.place(x=0,y=0,width=260,height=130)
        
        image1=Image.open(r"Face_Image\Employee5.png")
        image1=image1.resize((300,150),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(image1)
        
        f_label=Label(self.root,image=self.photoimage1)
        f_label.place(x=260,y=0,width=260,height=130)
        
        image2=Image.open(r"Face_Image\Employee_3.png")
        image2=image2.resize((500,150),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(image2)
        
        f_label=Label(self.root,image=self.photoimage2)
        f_label.place(x=520,y=0,width=500,height=130)
        
        image3=Image.open(r"Face_Image\Employee3.png")
        image3=image3.resize((300,150),Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(image3)
        
        f_label=Label(self.root,image=self.photoimage3)
        f_label.place(x=1020,y=0,width=275,height=130)  
        
        image4=Image.open(r"Face_Image\Employee2.png")
        image4=image4.resize((300,150),Image.LANCZOS)
        self.photoimage4=ImageTk.PhotoImage(image4)
        
        f_label=Label(self.root,image=self.photoimage4)
        f_label.place(x=1295,y=0,width=275,height=130) 
        
        imagebg=Image.open(r"Face_Image\bg.png")
        imagebg=imagebg.resize((1530,790),Image.LANCZOS)
        self.photoimagebg=ImageTk.PhotoImage(imagebg)
        
        bg_img=Label(self.root,image=self.photoimagebg)
        bg_img.place(x=0,y=130,width=1530,height=710)  
        
        Title_label=Label(bg_img,text="Employee Details",font=("Times New Roman",35,"bold"),fg="Black",bg="White")
        Title_label.place(x=0,y=0,width=1530,height=50)  
        
        main_frame=Frame(bg_img,border=2)
        main_frame.place(x=0,y=51,width=1530,height=710)
        
        Left_frame=LabelFrame(main_frame,bd=2,text="Employee Details",relief="flat",font=("Times New Roman",15,"bold"))
        Left_frame.place(x=10,y=10,width=740,height=580)

        imageLeft=Image.open(r"Face_Image\Details.png")
        imageLeft=imageLeft.resize((720,190),Image.LANCZOS)
        self.photoimageLeft=ImageTk.PhotoImage(imageLeft)
        
        Leftimg_lbl=Label(Left_frame,image=self.photoimageLeft)
        Leftimg_lbl.place(x=10,y=5,width=720,height=190)  
        
        #Inside Left frame
        Dept_frame=LabelFrame(Left_frame,text="Department",relief=RIDGE,font=("Times New Roman",15,"bold"))
        Dept_frame.place(x=10,y=195,width=720,height=100)
        
        Dept_frame_lbl=Label(Dept_frame,text="Department",font=("times new roman",12,"bold"))
        Dept_frame_lbl.grid(row=0,column=0,padx=10)  
        
        Dept_combo=ttk.Combobox(Dept_frame,textvariable=self.variable_dept,font=("times new roman",12,"bold "),state="read only")
        Dept_combo["values"]=("Select Department","Production","IT","AI")
        Dept_combo.current(0)
        Dept_combo.grid(row=0,column=1,padx=20,pady=15)
        
        Designation_frame_lbl=Label(Dept_frame,text="Designation",font=("times new roman",12,"bold"))
        Designation_frame_lbl.grid(row=0,column=2,padx=20,pady=2,sticky=W) 
        
        Entry_field_Designation=ttk.Entry(Dept_frame,textvariable=self.variable_designation,width=20,font=("times new roman",12,"bold"))
        Entry_field_Designation.grid(row=0,column=3,padx=20,pady=15,sticky=NSEW)
        
        Info_frame=LabelFrame(Left_frame,text="Information",relief=RIDGE,font=("Times New Roman",15,"bold"))
        Info_frame.place(x=10,y=300,width=720,height=190)
        
        #Inside Informtion Frame on Name field 
        Info_frame_Name=Label(Info_frame,text="Name",font=("times new roman",12,"bold"))
        Info_frame_Name.grid(row=0,column=0,padx=10,pady=5)
        
        Entry_field_Name=ttk.Entry(Info_frame,textvariable=self.variable_name,width=20,font=("times new roman",12,"bold"))
        Entry_field_Name.grid(row=0,column=1,padx=20,pady=7,sticky=NSEW)
        
        Info_frame_Id=Label(Info_frame,text="ID",font=("times new roman",12,"bold"))
        Info_frame_Id.grid(row=0,column=2,padx=10,pady=5)
        
        # repopulate the ID with "BG"
        def validate_id(action, value_if_allowed):
            # Allow only numeric input after "BG"
            if action == '1':  # If insertion is happening
                if len(value_if_allowed) > 3 and value_if_allowed[:3] == "BG0":
                    return value_if_allowed[3:].isdigit()  # Only allow digits after "BG"t
            return True  # Allow deletion of numbers but not "BG"

        # Prevent the user from deleting or altering "BG"
        def on_entry_change(*args):
            current_value = self.variable_id.get()
            if not current_value.startswith("BG0"):
                self.variable_id.set("BG0")
        
        # Create the validation command for the entry field
        validate_id_cmd = (Info_frame.register(validate_id), '%d', '%P')
        self.variable_id.trace_add('write', on_entry_change)

        # Place the Entry field with the correct grid settings
        Entry_field_Id = ttk.Entry(Info_frame, textvariable=self.variable_id, width=20, font=("times new roman", 12, "bold"), validate='key', validatecommand=validate_id_cmd)
        Entry_field_Id.grid(row=0, column=3, padx=20, pady=7, sticky=NSEW)

        # Prepopulate the Entry field with 'BG' initially
        self.variable_id.set("BG0")
        self.variable_id.trace_add('write', on_entry_change)
        
        Info_frame_Gender=Label(Info_frame,text="Gender",font=("times new roman",12,"bold"))
        Info_frame_Gender.grid(row=1,column=0,padx=10,pady=5)
   
        Gender_combo=ttk.Combobox(Info_frame,textvariable=self.variable_Gender,font=("times new roman",12,"bold "),state="read only")
        Gender_combo["values"]=("Select Gender","Male","Female","Other")
        Gender_combo.current(0)
        Gender_combo.grid(row=1,column=1,padx=20,pady=15,sticky=NSEW)
        
        Info_frame_DOB=Label(Info_frame,text="DOB",font=("times new roman",12,"bold"))
        Info_frame_DOB.grid(row=1,column=2,padx=10,pady=5)
        
        Entry_field_DOB=ttk.Entry(Info_frame,width=20,textvariable=self.variable_DOB,font=("times new roman",12,"bold"))
        Entry_field_DOB.grid(row=1,column=3,padx=20,pady=15,sticky=NSEW)
        
        Info_frame_Address=Label(Info_frame,text="Address",font=("times new roman",12,"bold"))
        Info_frame_Address.grid(row=2,column=0,padx=10,pady=5)
        
        Entry_field_Address=ttk.Entry(Info_frame,textvariable=self.variable_Address,width=20,font=("times new roman",12,"bold"))
        Entry_field_Address.grid(row=2,column=1,padx=20,pady=10,sticky=NSEW)
        
        Info_frame_Phn=Label(Info_frame,text="Phone Number",font=("times new roman",12,"bold"))
        Info_frame_Phn.grid(row=2,column=2,padx=10,pady=5)
        
        Entry_field_Phn=ttk.Entry(Info_frame,textvariable=self.variable_Phone_No,width=20,font=("times new roman",12,"bold"))
        Entry_field_Phn.grid(row=2,column=3,padx=20,pady=10,sticky=NSEW)
        
        #Radiobutton 
        self.variable_radiobtn = StringVar()
        radiobutton1 = ttk.Radiobutton(Info_frame, variable=self.variable_radiobtn,text="Take photo sample", value="Yes")
        radiobutton1.grid(row=3, column=1, sticky=NSEW)

        radiobutton2 = ttk.Radiobutton(Info_frame,variable=self.variable_radiobtn, text="No photo sample", value="No")
        radiobutton2.grid(row=3, column=2, sticky=NSEW)
        
        #Frame Button
        btn_frame=Frame(Left_frame,bd=2,relief="ridge") 
        btn_frame.place(x=12,y=495,width=720,height=30)
        
        btn_save=Button(btn_frame,command=self.add_data,bd=2,text="Save",width=25,bg="NavyBlue",fg="White",font=("times new roman",10,"bold"))
        btn_save.grid(row=0,column=0)
        
        btn_Update=Button(btn_frame,command=self.update_data,bd=2,text="Update",width=25,bg="NavyBlue",fg="White",font=("times new roman",10,"bold"))
        btn_Update.grid(row=0,column=1)
        
        btn_Del=Button(btn_frame,command=self.delete_data,bd=2,text="Delete",width=25,bg="NavyBlue",fg="White",font=("times new roman",10,"bold"))
        btn_Del.grid(row=0,column=2)
        
        btn_Reset=Button(btn_frame,command=self.reset_data,bd=2,text="Reset",width=22,bg="NavyBlue",fg="White",font=("times new roman",10,"bold"))
        btn_Reset.grid(row=0,column=3)
        
        btn_frame_new=Frame(Left_frame,bd=2,relief="ridge")
        btn_frame_new.place(x=12,y=522,width=720,height=29)
        
        btn_Photo_sample=Button(btn_frame_new,command=self.generate_dataset,bd=2,text="Take Photo Sample",width=49,bg="NavyBlue",fg="White",font=("times new roman",10,"bold"))
        btn_Photo_sample.grid(row=1,column=0)
        
        btn_Update_Sample=Button(btn_frame_new,bd=2,text="Update Photo Sample",width=51,bg="NavyBlue",fg="White",font=("times new roman",10,"bold"))
        btn_Update_Sample.grid(row=1,column=1)
        
        #Right_Frame
        Right_frame=LabelFrame(main_frame,bd=2,text="Employee Details",relief=RIDGE,font=("Times New Roman",15,"bold"))
        Right_frame.place(x=755,y=10,width=750 ,height=580)
        
        #First_segment
        imageRight=Image.open(r"Face_Image\Employee5.jpg")
        imageRight=imageRight.resize((720,190),Image.LANCZOS)
        self.photoimageRight=ImageTk.PhotoImage(imageRight)
        
        imageRight_lbl=Label(Right_frame,image=self.photoimageRight)
        imageRight_lbl.place(x=10,y=5,width=720,height=190)  
        
        #Second_segment
        Search_frame=LabelFrame(Right_frame,text="Search System",relief=RIDGE,font=("Times New Roman",15,"bold"))
        Search_frame.place(x=10,y=195,width=720,height=90)
        
        Search_frame_lbl=Label(Search_frame,text="Search By: ",padx=5,pady=5,font=("times new roman",12,"bold"))
        Search_frame_lbl.grid(row=0,column=0,padx=10)  
        
        Search_combo=ttk.Combobox(Search_frame,font=("times new roman",12,"bold "),state="read only")
        Search_combo["values"]=("Select" ,"ID","Phone_Number")
        Search_combo.current(0)
        Search_combo.grid(row=0,column=1,padx=5,pady=5,sticky=NSEW)
        
        Search_combo_field=ttk.Entry(Search_frame,width=20,font=("times new roman",12,"bold "))
        Search_combo_field.grid(row=0,column=2)
        
        btn_Search=Button(Search_frame,bd=2,text="Search",width=12,bg="Red",fg="White",font=("times new roman",12,"bold"))
        btn_Search.grid(row=0,column=3,padx=5)
        
        btn_Show_all=Button(Search_frame,bd=2,text="Show All",width=10,bg="Red",fg="White",font=("times new roman",12,"bold"))
        btn_Show_all.grid(row=0,column=4)

        #=====================Table Frame================        
        Table_frame=Frame(Right_frame,border=2,relief="ridge")
        Table_frame.place(x=10,y=290,width=720,height=250)
        
        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        
        self.employee_table=ttk.Treeview(Table_frame,column=("Dept","ID","Designation","Name","Gender","DOB","Address","Phone_No"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)          
        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)
           
        self.employee_table.heading("Dept",text="Department")
        self.employee_table.heading("ID",text="ID")
        self.employee_table.heading("Designation",text="Designation")
        self.employee_table.heading("Name",text="Name")
        self.employee_table.heading("Gender",text="Gender")
        self.employee_table.heading("DOB",text="DOB")
        self.employee_table.heading("Address",text="Address")
        self.employee_table.heading("Phone_No",text="Phone No")
        self.employee_table["show"]="headings"
        
        self.employee_table.pack(fill=BOTH )
        
        self.employee_table.column("Dept",width=100)
        self.employee_table.column("ID",width=100)
        self.employee_table.column("Designation",width=100)
        self.employee_table.column("Name",width=100)
        self.employee_table.column("Gender",width=100)
        self.employee_table.column("DOB",width=100)
        self.employee_table.column("Address",width=100)
        self.employee_table.column("Phone_No",width=100)
        
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        self.reset_data()
    
#     def add_data(self):
#         if self.variable_dept.get()=="Select Department" or self.variable_name.get()=="" or self.variable_id.get()=="":
#             messagebox.showerror("Error","All fields are required",parent=self.root)
#         else:
#             try:
#                 full_id = self.variable_id.get()
#                 if full_id.startswith("BG"):
#                     numeric_id = full_id[2:]
                
#                 if numeric_id.isdigit():
#                     conn=mysql.connector.connect(host="localhost",user="root",password="123456",database="face_recognizer")
#                     cursor=conn.cursor()
#                     cursor.execute("""INSERT INTO details (department, id, designation, name, gender, dob, address, phone_no, radiobtn)VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
#     """, (
#     self.variable_dept.get(),
#     #self.variable_id.get(),
#     numeric_id,
#     self.variable_designation.get(),
#     self.variable_name.get(),
#     self.variable_Gender.get(),
#     self.variable_DOB.get(),
#     self.variable_Address.get(),
#     self.variable_Phone_No.get(),
#     self.variable_radiobtn.get()
# ))          
#                     conn.commit()
#                     self.fetch_data()
#                     conn.close()
#                     messagebox.showinfo("Success","Information has been added succesfully",parent=self.root)
           
#             except Exception as e:
#                 messagebox.showinfo("Error",f"Due to :{str(e)}",parent=self.root)
#                 print("ID:", self.variable_id.get())
    def add_data(self):
        if self.variable_dept.get() == "Select Department" or self.variable_name.get() == "" or self.variable_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                # Extract numeric part from ID (assuming all IDs start with "BG")
                full_id = self.variable_id.get()

                # Ensure that the ID starts with 'BG' and then extract the numeric part
                if full_id.startswith("BG0"):
                    numeric_id = full_id[3:]  # Extract the numeric part (e.g., '01031')

                    # Ensure that numeric_id is indeed numeric
                    if numeric_id.isdigit():
                        conn = mysql.connector.connect(host="localhost", user="root", password="123456", database="face_recognizer")
                        cursor = conn.cursor()

                        # Insert only the numeric part into the database
                        cursor.execute("""INSERT INTO details (department, id, designation, name, gender, dob, address, phone_no, radiobtn)
                                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                                    (
                                        self.variable_dept.get(),
                                        numeric_id,  # Insert only the numeric part
                                        self.variable_designation.get(),
                                        self.variable_name.get(),
                                        self.variable_Gender.get(),
                                        self.variable_DOB.get(),
                                        self.variable_Address.get(),
                                        self.variable_Phone_No.get(),
                                        self.variable_radiobtn.get()
                                    ))
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Success", "Information has been added successfully", parent=self.root)
                    else:
                        messagebox.showerror("Error", "ID must contain a numeric part after 'BG'", parent=self.root)
                else:
                    messagebox.showerror("Error", "ID must start with 'BG'", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Due to : {str(e)}", parent=self.root)
  
                
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="123456", database="face_recognizer")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM details")
        data = cursor.fetchall()
        
        if len(data) != 0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("", END, values=i)
            conn.commit()
        conn.close()
        
    def get_cursor(self, event=""):
        cursor_focus = self.employee_table.focus()
        content = self.employee_table.item(cursor_focus)
        data = content["values"]
        
        # Check that the length of data is sufficient
        if len(data) >0:
            self.variable_dept.set(data[0])
            numeric_id = data[1]
            full_id = f"BG0{numeric_id}"  # Add "BG" prefix to the numeric part
            
            self.variable_id.set(full_id)
                
          #  self.variable_id.set(data[1])
            self.variable_designation.set(data[2])
            self.variable_name.set(data[3])
            self.variable_Gender.set(data[4])
            self.variable_DOB.set(data[5])
            self.variable_Address.set(data[6])
            self.variable_Phone_No.set(data[7])
            
            # Check if there are enough elements to access index 8
            if len(data) > 8:
                self.variable_radiobtn.set(data[8])
            else:
                # Handle the case where the radiobutton data is missing
                self.variable_radiobtn.set("")  # Or set to a default value
        else:
            print("Not enough data to populate all fields.")       
   
 #    def update_data(self):
#         if self.variable_dept.get()=="Select Department" or self.variable_name.get()=="" or self.variable_id.get()=="":
#             messagebox.showerror("Error","All fields are required",parent=self.root)
#         else:
#             try:
#                 Update=messagebox.askyesno("Update","Do u want to update these details",parent=self.root)
#                 if  Update>0:
#                     conn = mysql.connector.connect(host="localhost", user="root", password="123456", database="face_recognizer")
#                     cursor = conn.cursor()
#                     cursor.execute("Update details set department=%s,designation=%s,name=%s,Gender=%s,DOB=%s,Address=%s,Phone_no=%s,radiobtn=%s where id=%s", (
#     self.variable_dept.get(), 
#     self.variable_designation.get(),                                                                                                                                                                                               
#     self.variable_name.get(),
#     self.variable_Gender.get(),
#     self.variable_DOB.get(),
#     self.variable_Address.get(),
#     self.variable_Phone_No.get(),
#     self.variable_radiobtn.get(),
#     self.variable_id.get()
# ))
#                 else:
#                     if not Update:
#                         return
#                 messagebox.showinfo("Success","Employee details succesfully update completed",parent=self.root)
#                 conn.commit()
#                 self.fetch_data()
#                 conn.close() 
#             except Exception as e: 
#                 messagebox.showerror("Error",f"Due to :{str(e)}",parent=self.root)
                              
#     def delete_data(self):
#         if self.variable_id.get()=="":
#             messagebox.showerror("Error","Id is required",parent=self.root)
#         else:
#             try:
#                 delete=messagebox.askyesno("Delete","Do u want to delete this id",parent=self.root)
#                 if delete>0:
#                     conn = mysql.connector.connect(host="localhost", user="root", password="123456", database="face_recognizer")
#                     cursor = conn.cursor()
#                     sql="delete from Details where id=%s"
#                     val=(self.variable_id.get(),)
#                     cursor.execute(sql,val)
#                 else:
#                     if not delete:
#                         return
#                 conn.commit()
#                 self.fetch_data()
#                 self.reset_data()
#                 conn.close() 
#                 messagebox.showinfo("Delete","Details succesfully deleted",parent=self.root)
#             except Exception as e: 
#                 messagebox.showerror("Error",f"Due to :{str(e)}",parent=self.root)
    
    def update_data(self):
        if self.variable_dept.get() == "Select Department" or self.variable_name.get() == "" or self.variable_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update these details?", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="123456", database="face_recognizer")
                    cursor = conn.cursor()

                    # Use the full alphanumeric ID (BG01031)
                    full_id = self.variable_id.get()

                    # Ensure the ID starts with 'BG0'
                    if full_id.startswith("BG0"):
                        numeric_id = full_id[3:]  # Extract the numeric part

                        # Update the data in the database using the numeric part of the ID
                        cursor.execute("""UPDATE details SET department=%s, designation=%s, name=%s, Gender=%s, DOB=%s, Address=%s, Phone_no=%s, radiobtn=%s 
                                        WHERE id=%s""",
                                    (
                                        self.variable_dept.get(),
                                        self.variable_designation.get(),
                                        self.variable_name.get(),
                                        self.variable_Gender.get(),
                                        self.variable_DOB.get(),
                                        self.variable_Address.get(),
                                        self.variable_Phone_No.get(),
                                        self.variable_radiobtn.get(),
                                        numeric_id  # Use only the numeric part (e.g., '01031')
                                    ))

                        conn.commit()
                        self.fetch_data()
                        self.reset_data()
                        conn.close()

                        messagebox.showinfo("Success", "Employee details successfully updated", parent=self.root)
                    else:
                        messagebox.showerror("Error", "ID must start with 'BG0'", parent=self.root)
                else:
                    return
            except Exception as e:
                messagebox.showerror("Error", f"Due to: {str(e)}", parent=self.root)


    def delete_data(self):
        if self.variable_id.get() == "":
            messagebox.showerror("Error", "ID is required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete", "Do you want to delete this ID?", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="123456", database="face_recognizer")
                    cursor = conn.cursor()

                    # Use the full alphanumeric ID (BG01031)
                    full_id = self.variable_id.get()

                    # Ensure the ID starts with 'BG0'
                    if full_id.startswith("BG0"):
                        numeric_id = full_id[3:]  # Extract the numeric part

                        # Delete the data using the numeric part
                        sql = "DELETE FROM details WHERE id=%s"
                        cursor.execute(sql, (numeric_id,))  # Use only the numeric part (e.g., '01031')

                        conn.commit()
                        self.fetch_data()
                        self.reset_data()
                        conn.close()

                        messagebox.showinfo("Success", "Details successfully deleted", parent=self.root)
                    else:
                        messagebox.showerror("Error", "ID must start with 'BG0'", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Due to: {str(e)}", parent=self.root)


    def reset_data(self):
        self.variable_dept.set("Select Department")
        self.variable_id.set("")
        self.variable_name.set("")
        self.variable_designation.set("")
        self.variable_Gender.set("Select Gender")
        self.variable_DOB.set("")
        self.variable_Address.set("")
        self.variable_Phone_No.set("")                    
         
#     def generate_dataset(self):
#         if self.variable_dept.get()=="Select Department" or self.variable_name.get()=="" or self.variable_id.get()=="":
#             messagebox.showerror("Error","All fields are required",parent=self.root)
#         else:
#             try:
#                 conn = mysql.connector.connect(host="localhost", user="root", password="123456", database="face_recognizer")
#                 cursor = conn.cursor()
#                 cursor.execute("select * from details")
#                 result=cursor.fetchall()
#                 id=0
#                 for x in result:
#                     id+=1
                
#                 cursor.execute("Update details set department=%s,designation=%s,name=%s,Gender=%s,DOB=%s,Address=%s,Phone_no=%s,radiobtn=%s where id=%s", (
#         self.variable_dept.get(), 
#         self.variable_designation.get(),                                                                                                                                                                                               
#         self.variable_name.get(),
#         self.variable_Gender.get(),
#         self.variable_DOB.get(),
#         self.variable_Address.get(),
#         self.variable_Phone_No.get(),
#         self.variable_radiobtn.get(),
#         self.variable_id.get()

#         #id
#         #self.variable_id.get()==str(id+1)        ###########Truncated incorrect id values when self.variable_id.get()=id+1 is given
# ))
#                 conn.commit()
#                 self.fetch_data()
#                 self.reset_data()
#                 conn.close() 
                  
#                 #####  Face Detection OpenCV ######      
        
#                 script_directory = os.path.dirname(os.path.abspath(__file__))
                
#                 data_directory = os.path.join(script_directory, "Data")
#                 if not os.path.exists(data_directory):
#                     os.makedirs(data_directory)
                
#                 cascade_path = os.path.join(script_directory, "haarcascade_frontalface_default.xml")
#                 face_classifier = cv2.CascadeClassifier(cascade_path)            
                
#                 def face_cropped(img):
#                     gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#                     faces=face_classifier.detectMultiScale(gray,1.3,5)          #scaling_factor==1.3,min_neighbour=5
#                     if len(faces) == 0:
#                         messagebox.showerror("Error","No face detected.")
                    
#                     for (x,y,w,h) in faces:
#                         face_croppped=img[y:y+h,x:x+w]
#                         return face_croppped
                
#                 #cap=cv2.VideoCapture(1)
#                 cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Use the correct index

#                 img_id=0
#                 while True:
#                     ret,my_frame=cap.read()
#                     if face_cropped(my_frame)is not None:
#                         img_id+=1
#                         face=cv2.resize(face_cropped(my_frame),(450,450))
#                         face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY) 
                        

#                         #alphanumeric_id = self.variable_id.get() 
#                         #file_name_path = "Data/user." + str(id) + "." + str(img_id) + ".jpg"
#                         file_name_path = os.path.join(data_directory, "user" +"."+ str(id) + "." + str(img_id) + ".jpg") 
#                         print(file_name_path)                    
                        
#                         if cv2.imwrite(file_name_path,face):
#                             print(f"Image {img_id} saved successfully.")
#                         else:
#                             messagebox.showerror(f"Failed to save image {img_id}.")
                            
#                         cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
#                         cv2.imshow("Cropped_face",face)

#                     if cv2.waitKey(1)==13 or int(img_id)==50:
#                         break
#                 cap.release()
#                 cv2.destroyAllWindows()
#                 messagebox.showinfo("Result","Sample collected successfully")
#             except Exception as e:
#                 messagebox.showinfo("Error",f"Due to :{str(e)}",parent=self.root)               
      
    def generate_dataset(self):
        if self.variable_dept.get() == "Select Department" or self.variable_name.get() == "" or self.variable_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="123456", database="face_recognizer")
                cursor = conn.cursor()

                # Extract only the numeric part of the ID (assuming the ID starts with 'BG0')
                full_id = self.variable_id.get()
                if full_id.startswith("BG0"):
                    numeric_id = full_id[3:]  # Extract numeric part after 'BG0'

                # Ensure the numeric_id is valid (contains only digits)
                if numeric_id.isdigit():
                    cursor.execute("SELECT * FROM details")
                    result = cursor.fetchall()
                    id = 0
                    for x in result:
                        id += 1

                    # Now update the database using only the numeric part of the ID
                    cursor.execute("""UPDATE details SET department=%s, designation=%s, name=%s, Gender=%s, DOB=%s, Address=%s, Phone_no=%s, radiobtn=%s 
                                    WHERE id=%s""",
                                (
                                    self.variable_dept.get(),
                                    self.variable_designation.get(),
                                    self.variable_name.get(),
                                    self.variable_Gender.get(),
                                    self.variable_DOB.get(),
                                    self.variable_Address.get(),
                                    self.variable_Phone_No.get(),
                                    self.variable_radiobtn.get(),
                                    numeric_id  # Insert only the numeric part (e.g., '1031')
                                ))

                    conn.commit()
                    self.fetch_data()
                    self.reset_data()
                    conn.close()

                    ##### Face Detection OpenCV ######
                    script_directory = os.path.dirname(os.path.abspath(__file__))
                    
                    data_directory = os.path.join(script_directory, "Data")
                    if not os.path.exists(data_directory):
                        os.makedirs(data_directory)

                    cascade_path = os.path.join(script_directory, "haarcascade_frontalface_default.xml")
                    face_classifier = cv2.CascadeClassifier(cascade_path)

                    def face_cropped(img):
                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        faces = face_classifier.detectMultiScale(gray, 1.1, 5)
                        if len(faces) == 0:
                            messagebox.showerror("Error", "No face detected.")
                        
                        for (x, y, w, h) in faces:
                            face_cropped = img[y:y + h, x:x + w]
                            return face_cropped
                    
                    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

                    img_id = 0
                    while True:
                        ret, my_frame = cap.read()
                        if face_cropped(my_frame) is not None:
                            img_id += 1
                            face = cv2.resize(face_cropped(my_frame), (640, 480))
                            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                            # Save the image with the numeric ID and image ID
                            file_name_path = os.path.join(data_directory, "user." + str(numeric_id) + "." + str(img_id) + ".jpg")
                            print(file_name_path)

                            if cv2.imwrite(file_name_path, face):
                                print(f"Image {img_id} saved successfully.")
                            else:
                                messagebox.showerror(f"Failed to save image {img_id}.")
                            
                            cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                            cv2.imshow("Cropped_face", face)

                        if ret:
                            cv2.imshow('Camera Feed', my_frame)                        
                        if cv2.waitKey(1) == 13 or int(img_id) == 100:
                            break
                    
                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result", "Sample collected successfully")
                else:
                    messagebox.showerror("Error", "ID must contain a numeric part after 'BG0'", parent=self.root)

            except Exception as e:
                messagebox.showinfo("Error", f"Due to : {str(e)}", parent=self.root)     
                    
if __name__=="__main__":
    root=Tk()
    obj=Details(root)
    root.mainloop() 
    
###############-----------22.09.2024------New one testing 
    
# from logging import root
# from tkinter import*
# from tkinter import ttk
# from PIL import Image,ImageTk
# from tkinter import messagebox
# import mysql.connector
# import cv2
# import os
# from mtcnn import MTCNN

# class Details:
#     def __init__(self, root):                     
#         self.root=root
#         self.root.geometry("1530x790+0+0")
#         self.root.title("Face Recognition Attendance System")
#         self.variable_dept=StringVar()
#         self.variable_id=StringVar()
#         self.variable_designation=StringVar()
#         self.variable_name=StringVar()
#         self.variable_Gender=StringVar()
#         self.variable_DOB=StringVar()
#         self.variable_Phone_No=StringVar()
#         self.variable_Address=StringVar() 
        
#         self.detector = MTCNN()
        
#         image=Image.open(r"Face_Image\Employee1.png")
#         image=image.resize((300,150),Image.LANCZOS)
#         self.photoimage=ImageTk.PhotoImage(image)
        
#         f_label=Label(self.root,image=self.photoimage)
#         f_label.place(x=0,y=0,width=260,height=130)
        
#         image1=Image.open(r"Face_Image\Employee5.png")
#         image1=image1.resize((300,150),Image.LANCZOS)
#         self.photoimage1=ImageTk.PhotoImage(image1)
        
#         f_label=Label(self.root,image=self.photoimage1)
#         f_label.place(x=260,y=0,width=260,height=130)
        
#         image2=Image.open(r"Face_Image\Employee_3.png")
#         image2=image2.resize((500,150),Image.LANCZOS)
#         self.photoimage2=ImageTk.PhotoImage(image2)
        
#         f_label=Label(self.root,image=self.photoimage2)
#         f_label.place(x=520,y=0,width=500,height=130)
        
#         image3=Image.open(r"Face_Image\Employee3.png")
#         image3=image3.resize((300,150),Image.LANCZOS)
#         self.photoimage3=ImageTk.PhotoImage(image3)
        
#         f_label=Label(self.root,image=self.photoimage3)
#         f_label.place(x=1020,y=0,width=275,height=130)  
        
#         image4=Image.open(r"Face_Image\Employee2.png")
#         image4=image4.resize((300,150),Image.LANCZOS)
#         self.photoimage4=ImageTk.PhotoImage(image4)
        
#         f_label=Label(self.root,image=self.photoimage4)
#         f_label.place(x=1295,y=0,width=275,height=130) 
        
#         imagebg=Image.open(r"Face_Image\bg.png")
#         imagebg=imagebg.resize((1530,790),Image.LANCZOS)
#         self.photoimagebg=ImageTk.PhotoImage(imagebg)
        
#         bg_img=Label(self.root,image=self.photoimagebg)
#         bg_img.place(x=0,y=130,width=1530,height=710)  
        
#         Title_label=Label(bg_img,text="Employee Details",font=("Times New Roman",35,"bold"),fg="Black",bg="White")
#         Title_label.place(x=0,y=0,width=1530,height=50)  
        
#         main_frame=Frame(bg_img,border=2)
#         main_frame.place(x=0,y=51,width=1530,height=710)
        
#         Left_frame=LabelFrame(main_frame,bd=2,text="Employee Details",relief="flat",font=("Times New Roman",15,"bold"))
#         Left_frame.place(x=10,y=10,width=740,height=580)

#         imageLeft=Image.open(r"Face_Image\Details.png")
#         imageLeft=imageLeft.resize((720,190),Image.LANCZOS)
#         self.photoimageLeft=ImageTk.PhotoImage(imageLeft)
        
#         Leftimg_lbl=Label(Left_frame,image=self.photoimageLeft)
#         Leftimg_lbl.place(x=10,y=5,width=720,height=190)  
        
#         #Inside Left frame
#         Dept_frame=LabelFrame(Left_frame,text="Department",relief=RIDGE,font=("Times New Roman",15,"bold"))
#         Dept_frame.place(x=10,y=195,width=720,height=100)
        
#         Dept_frame_lbl=Label(Dept_frame,text="Department",font=("times new roman",12,"bold"))
#         Dept_frame_lbl.grid(row=0,column=0,padx=10)  
        
#         Dept_combo=ttk.Combobox(Dept_frame,textvariable=self.variable_dept,font=("times new roman",12,"bold "),state="read only")
#         Dept_combo["values"]=("Select Department","Production","IT","AI")
#         Dept_combo.current(0)
#         Dept_combo.grid(row=0,column=1,padx=20,pady=15)
        
#         Designation_frame_lbl=Label(Dept_frame,text="Designation",font=("times new roman",12,"bold"))
#         Designation_frame_lbl.grid(row=0,column=2,padx=20,pady=2,sticky=W) 
        
#         Entry_field_Designation=ttk.Entry(Dept_frame,textvariable=self.variable_designation,width=20,font=("times new roman",12,"bold"))
#         Entry_field_Designation.grid(row=0,column=3,padx=20,pady=15,sticky=NSEW)
        
#         Info_frame=LabelFrame(Left_frame,text="Information",relief=RIDGE,font=("Times New Roman",15,"bold"))
#         Info_frame.place(x=10,y=300,width=720,height=190)
        
#         #Inside Informtion Frame on Name field 
#         Info_frame_Name=Label(Info_frame,text="Name",font=("times new roman",12,"bold"))
#         Info_frame_Name.grid(row=0,column=0,padx=10,pady=5)
        
#         Entry_field_Name=ttk.Entry(Info_frame,textvariable=self.variable_name,width=20,font=("times new roman",12,"bold"))
#         Entry_field_Name.grid(row=0,column=1,padx=20,pady=7,sticky=NSEW)
        
#         Info_frame_Id=Label(Info_frame,text="ID",font=("times new roman",12,"bold"))
#         Info_frame_Id.grid(row=0,column=2,padx=10,pady=5)
        
#         # repopulate the ID with "BG"
#         def validate_id(action, value_if_allowed):
#             # Allow only numeric input after "BG"
#             if action == '1':  # If insertion is happening
#                 if len(value_if_allowed) > 3 and value_if_allowed[:3] == "BG0":
#                     return value_if_allowed[3:].isdigit()  # Only allow digits after "BG"
#                 return False
#             return True  # Allow deletion of numbers but not "BG"

#         # Prevent the user from deleting or altering "BG"
#         def on_entry_change(*args):
#             current_value = self.variable_id.get()
#             if not current_value.startswith("BG0"):
#                 self.variable_id.set("BG0")
        
#         # Create the validation command for the entry field
#         validate_id_cmd = (Info_frame.register(validate_id), '%d', '%P')
#         self.variable_id.trace_add('write', on_entry_change)

#         # Place the Entry field with the correct grid settings
#         Entry_field_Id = ttk.Entry(Info_frame, textvariable=self.variable_id, width=20, font=("times new roman", 12, "bold"), validate='key', validatecommand=validate_id_cmd)
#         Entry_field_Id.grid(row=0, column=3, padx=20, pady=7, sticky=NSEW)

#         # Prepopulate the Entry field with 'BG' initially
#         self.variable_id.set("BG0")
#         self.variable_id.trace_add('write', on_entry_change)
        
#         Info_frame_Gender=Label(Info_frame,text="Gender",font=("times new roman",12,"bold"))
#         Info_frame_Gender.grid(row=1,column=0,padx=10,pady=5)
   
#         Gender_combo=ttk.Combobox(Info_frame,textvariable=self.variable_Gender,font=("times new roman",12,"bold "),state="read only")
#         Gender_combo["values"]=("Select Gender","Male","Female","Other")
#         Gender_combo.current(0)
#         Gender_combo.grid(row=1,column=1,padx=20,pady=15,sticky=NSEW)
        
#         Info_frame_DOB=Label(Info_frame,text="DOB",font=("times new roman",12,"bold"))
#         Info_frame_DOB.grid(row=1,column=2,padx=10,pady=5)
        
#         Entry_field_DOB=ttk.Entry(Info_frame,width=20,textvariable=self.variable_DOB,font=("times new roman",12,"bold"))
#         Entry_field_DOB.grid(row=1,column=3,padx=20,pady=15,sticky=NSEW)
        
#         Info_frame_Address=Label(Info_frame,text="Address",font=("times new roman",12,"bold"))
#         Info_frame_Address.grid(row=2,column=0,padx=10,pady=5)
        
#         Entry_field_Address=ttk.Entry(Info_frame,textvariable=self.variable_Address,width=20,font=("times new roman",12,"bold"))
#         Entry_field_Address.grid(row=2,column=1,padx=20,pady=10,sticky=NSEW)
        
#         Info_frame_Phn=Label(Info_frame,text="Phone Number",font=("times new roman",12,"bold"))
#         Info_frame_Phn.grid(row=2,column=2,padx=10,pady=5)
        
#         Entry_field_Phn=ttk.Entry(Info_frame,textvariable=self.variable_Phone_No,width=20,font=("times new roman",12,"bold"))
#         Entry_field_Phn.grid(row=2,column=3,padx=20,pady=10,sticky=NSEW)
        
#         #Radiobutton 
#         self.variable_radiobtn = StringVar()
#         radiobutton1 = ttk.Radiobutton(Info_frame, variable=self.variable_radiobtn,text="Take photo sample", value="Yes")
#         radiobutton1.grid(row=3, column=1, sticky=NSEW)
        
#         radiobutton2 = ttk.Radiobutton(Info_frame,variable=self.variable_radiobtn, text="No photo sample", value="No")
#         radiobutton2.grid(row=3, column=2, sticky=NSEW)
        
#         #Frame Button
#         btn_frame=Frame(Left_frame,bd=2,relief="ridge") 
#         btn_frame.place(x=12,y=495,width=720,height=30)
        
#         btn_save=Button(btn_frame,command=self.add_data,bd=2,text="Save",width=25,bg="NavyBlue",fg="White",font=("times new roman",10,"bold"))
#         btn_save.grid(row=0,column=0)
        
#         btn_Update=Button(btn_frame,command=self.update_data,bd=2,text="Update",width=25,bg="NavyBlue",fg="White",font=("times new roman",10,"bold"))
#         btn_Update.grid(row=0,column=1)
        
#         btn_Del=Button(btn_frame,command=self.delete_data,bd=2,text="Delete",width=25,bg="NavyBlue",fg="White",font=("times new roman",10,"bold"))
#         btn_Del.grid(row=0,column=2)
        
#         btn_Reset=Button(btn_frame,command=self.reset_data,bd=2,text="Reset",width=22,bg="NavyBlue",fg="White",font=("times new roman",10,"bold"))
#         btn_Reset.grid(row=0,column=3)
        
#         btn_frame_new=Frame(Left_frame,bd=2,relief="ridge")
#         btn_frame_new.place(x=12,y=522,width=720,height=29)
        
#         btn_Photo_sample=Button(btn_frame_new,command=self.generate_dataset,bd=2,text="Take Photo Sample",width=49,bg="NavyBlue",fg="White",font=("times new roman",10,"bold"))
#         btn_Photo_sample.grid(row=1,column=0)
        
#         btn_Update_Sample=Button(btn_frame_new,bd=2,text="Update Photo Sample",width=51,bg="NavyBlue",fg="White",font=("times new roman",10,"bold"))
#         btn_Update_Sample.grid(row=1,column=1)
        
#         #Right_Frame
#         Right_frame=LabelFrame(main_frame,bd=2,text="Employee Details",relief=RIDGE,font=("Times New Roman",15,"bold"))
#         Right_frame.place(x=755,y=10,width=750 ,height=580)
        
#         #First_segment
#         imageRight=Image.open(r"Face_Image\Employee5.jpg")
#         imageRight=imageRight.resize((720,190),Image.LANCZOS)
#         self.photoimageRight=ImageTk.PhotoImage(imageRight)
        
#         imageRight_lbl=Label(Right_frame,image=self.photoimageRight)
#         imageRight_lbl.place(x=10,y=5,width=720,height=190)  
        
#         #Second_segment
#         Search_frame=LabelFrame(Right_frame,text="Search System",relief=RIDGE,font=("Times New Roman",15,"bold"))
#         Search_frame.place(x=10,y=195,width=720,height=90)
        
#         Search_frame_lbl=Label(Search_frame,text="Search By: ",padx=5,pady=5,font=("times new roman",12,"bold"))
#         Search_frame_lbl.grid(row=0,column=0,padx=10)  
        
#         Search_combo=ttk.Combobox(Search_frame,font=("times new roman",12,"bold "),state="read only")
#         Search_combo["values"]=("Select" ,"ID","Phone_Number")
#         Search_combo.current(0)
#         Search_combo.grid(row=0,column=1,padx=5,pady=5,sticky=NSEW)
        
#         Search_combo_field=ttk.Entry(Search_frame,width=20,font=("times new roman",12,"bold "))
#         Search_combo_field.grid(row=0,column=2)
        
#         btn_Search=Button(Search_frame,bd=2,text="Search",width=12,bg="Red",fg="White",font=("times new roman",12,"bold"))
#         btn_Search.grid(row=0,column=3,padx=5)
        
#         btn_Show_all=Button(Search_frame,bd=2,text="Show All",width=10,bg="Red",fg="White",font=("times new roman",12,"bold"))
#         btn_Show_all.grid(row=0,column=4)

#         #=====================Table Frame================        
#         Table_frame=Frame(Right_frame,border=2,relief="ridge")
#         Table_frame.place(x=10,y=290,width=720,height=250)
        
#         scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
#         scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        
#         self.employee_table=ttk.Treeview(Table_frame,column=("Dept","ID","Designation","Name","Gender","DOB","Address","Phone_No"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
#         scroll_x.pack(side=BOTTOM,fill=X)
#         scroll_y.pack(side=RIGHT,fill=Y)          
#         scroll_x.config(command=self.employee_table.xview)
#         scroll_y.config(command=self.employee_table.yview)
           
#         self.employee_table.heading("Dept",text="Department")
#         self.employee_table.heading("ID",text="ID")
#         self.employee_table.heading("Designation",text="Designation")
#         self.employee_table.heading("Name",text="Name")
#         self.employee_table.heading("Gender",text="Gender")
#         self.employee_table.heading("DOB",text="DOB")
#         self.employee_table.heading("Address",text="Address")
#         self.employee_table.heading("Phone_No",text="Phone No")
#         self.employee_table["show"]="headings"
        
#         self.employee_table.pack(fill=BOTH )
        
#         self.employee_table.column("Dept",width=100)
#         self.employee_table.column("ID",width=100)
#         self.employee_table.column("Designation",width=100)
#         self.employee_table.column("Name",width=100)
#         self.employee_table.column("Gender",width=100)
#         self.employee_table.column("DOB",width=100)
#         self.employee_table.column("Address",width=100)
#         self.employee_table.column("Phone_No",width=100)
        
#         self.employee_table.bind("<ButtonRelease>",self.get_cursor)
#         self.fetch_data()
#         self.reset_data()
    
#     def add_data(self):
#         if self.variable_dept.get() == "Select Department" or self.variable_name.get() == "" or self.variable_id.get() == "":
#             messagebox.showerror("Error", "All fields are required", parent=self.root)
#         else:
#             try:
#                 # Extract numeric part from ID (assuming all IDs start with "BG")
#                 full_id = self.variable_id.get()

#                 # Ensure that the ID starts with 'BG' and then extract the numeric part
#                 if full_id.startswith("BG0"):
#                     numeric_id = full_id[3:]  # Extract the numeric part (e.g., '01031')

#                     # Ensure that numeric_id is indeed numeric
#                     if numeric_id.isdigit():
#                         conn = mysql.connector.connect(host="localhost", user="root", password="123456", database="face_recognizer")
#                         cursor = conn.cursor()

#                         # Insert only the numeric part into the database
#                         cursor.execute("""INSERT INTO details (department, id, designation, name, gender, dob, address, phone_no, radiobtn)
#                                         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""",
#                                     (
#                                         self.variable_dept.get(),
#                                         numeric_id,  # Insert only the numeric part
#                                         self.variable_designation.get(),
#                                         self.variable_name.get(),
#                                         self.variable_Gender.get(),
#                                         self.variable_DOB.get(),
#                                         self.variable_Address.get(),
#                                         self.variable_Phone_No.get(),
#                                         self.variable_radiobtn.get()
#                                     ))
#                         conn.commit()
#                         self.fetch_data()
#                         conn.close()
#                         messagebox.showinfo("Success", "Information has been added successfully", parent=self.root)
#                     else:
#                         messagebox.showerror("Error", "ID must contain a numeric part after 'BG'", parent=self.root)
#                 else:
#                     messagebox.showerror("Error", "ID must start with 'BG'", parent=self.root)
#             except Exception as e:
#                 messagebox.showerror("Error", f"Due to : {str(e)}", parent=self.root)
                
#     def fetch_data(self):
#         conn = mysql.connector.connect(host="localhost", user="root", password="123456", database="face_recognizer")
#         cursor = conn.cursor()
#         cursor.execute("SELECT * FROM details")
#         data = cursor.fetchall()
        
#         if len(data) != 0:
#             self.employee_table.delete(*self.employee_table.get_children())
#             for i in data:
#                 self.employee_table.insert("", END, values=i)
#             conn.commit()
#         conn.close()
        
#     def get_cursor(self, event=""):
#         cursor_focus = self.employee_table.focus()
#         content = self.employee_table.item(cursor_focus)
#         data = content["values"]
        
#         # Check that the length of data is sufficient
#         if len(data) >0:
#             self.variable_dept.set(data[0])
#             numeric_id = data[1]
#             full_id = f"BG0{numeric_id}"  # Add "BG" prefix to the numeric part
            
#             self.variable_id.set(full_id)   
#           #  self.variable_id.set(data[1])
#             self.variable_designation.set(data[2])
#             self.variable_name.set(data[3])
#             self.variable_Gender.set(data[4])
#             self.variable_DOB.set(data[5])
#             self.variable_Address.set(data[6])
#             self.variable_Phone_No.set(data[7])
            
#             # Check if there are enough elements to access index 8
#             if len(data) > 8:
#                 self.variable_radiobtn.set(data[8])
#             else:
#                 # Handle the case where the radiobutton data is missing
#                 self.variable_radiobtn.set("")  # Or set to a default value
#         else:
#             print("Not enough data to populate all fields.")       
            
#     def update_data(self):
#         if self.variable_dept.get() == "Select Department" or self.variable_name.get() == "" or self.variable_id.get() == "":
#             messagebox.showerror("Error", "All fields are required", parent=self.root)
#         else:
#             try:
#                 Update = messagebox.askyesno("Update", "Do you want to update these details?", parent=self.root)
#                 if Update > 0:
#                     conn = mysql.connector.connect(host="localhost", user="root", password="123456", database="face_recognizer")
#                     cursor = conn.cursor()

#                     # Use the full alphanumeric ID (BG01031)
#                     full_id = self.variable_id.get()

#                     # Ensure the ID starts with 'BG0'
#                     if full_id.startswith("BG0"):
#                         numeric_id = full_id[3:]  # Extract the numeric part

#                         # Update the data in the database using the numeric part of the ID
#                         cursor.execute("""UPDATE details SET department=%s, designation=%s, name=%s, Gender=%s, DOB=%s, Address=%s, Phone_no=%s, radiobtn=%s 
#                                         WHERE id=%s""",
#                                     (
#                                         self.variable_dept.get(),
#                                         self.variable_designation.get(),
#                                         self.variable_name.get(),
#                                         self.variable_Gender.get(),
#                                         self.variable_DOB.get(),
#                                         self.variable_Address.get(),
#                                         self.variable_Phone_No.get(),
#                                         self.variable_radiobtn.get(),
#                                         numeric_id  # Use only the numeric part (e.g., '01031')
#                                     ))
#                         conn.commit()
#                         self.fetch_data()
#                         self.reset_data()
#                         conn.close()

#                         messagebox.showinfo("Success", "Employee details successfully updated", parent=self.root)
#                     else:
#                         messagebox.showerror("Error", "ID must start with 'BG0'", parent=self.root)
#                 else:
#                     return
#             except Exception as e:
#                 messagebox.showerror("Error", f"Due to: {str(e)}", parent=self.root)

#     def delete_data(self):
#         if self.variable_id.get() == "":
#             messagebox.showerror("Error", "ID is required", parent=self.root)
#         else:
#             try:
#                 delete = messagebox.askyesno("Delete", "Do you want to delete this ID?", parent=self.root)
#                 if delete > 0:
#                     conn = mysql.connector.connect(host="localhost", user="root", password="123456", database="face_recognizer")
#                     cursor = conn.cursor()

#                     # Use the full alphanumeric ID (BG01031)
#                     full_id = self.variable_id.get()

#                     # Ensure the ID starts with 'BG0'
#                     if full_id.startswith("BG0"):
#                     # Print the full ID to check
#                         print(f"Full ID to delete: {full_id}")

#                         # Try deleting the ID without padding zeros
#                         numeric_id = full_id[3:].lstrip("0")  # Remove leading zeros
#                         id_variations = [full_id, f"BG{numeric_id}"]

#                         # Try deleting both possible variations
#                         for possible_id in id_variations:
#                             print(f"Trying to delete ID: {possible_id}")
#                             sql = "DELETE FROM details WHERE id=%s"
#                             cursor.execute(sql, (possible_id,))
#                             if cursor.rowcount > 0:
#                                 print(f"Deleted ID: {possible_id}")
#                                 break
#                         # Check how many rows were affected by the DELETE query
#                         rows_affected = cursor.rowcount
#                         print(f"Rows deleted: {rows_affected}")

#                         if rows_affected == 0:
#                             messagebox.showerror("Error", "No record found with this ID", parent=self.root)
#                         else:
#                             conn.commit()
#                             self.fetch_data()
#                             self.reset_data()
#                             conn.close()
#                             messagebox.showinfo("Success", "Details successfully deleted", parent=self.root)
#                     else:
#                         messagebox.showerror("Error", "ID must start with 'BG0'", parent=self.root)
#             except Exception as e:
#                 messagebox.showerror("Error", f"Due to: {str(e)}", parent=self.root)

#     def reset_data(self):
#         self.variable_dept.set("Select Department")
#         self.variable_id.set("")
#         self.variable_name.set("")
#         self.variable_designation.set("")
#         self.variable_Gender.set("Select Gender")
#         self.variable_DOB.set("")
#         self.variable_Address.set("")
#         self.variable_Phone_No.set("")                            
    
#     def detect_faces(self, img):
#         # Resize the image to a smaller size (e.g., 640x480) for faster processing
#         img_small = cv2.resize(img, (600, 400))
#         faces = self.detector.detect_faces(img_small)

#         # Adjust the face coordinates to match the original image size
#         scale_x = img.shape[1] / img_small.shape[1]
#         scale_y = img.shape[0] / img_small.shape[0]

#         for face in faces:
#             # Scale the bounding box
#             face['box'] = [
#                 int(face['box'][0] * scale_x),
#                 int(face['box'][1] * scale_y),
#                 int(face['box'][2] * scale_x),
#                 int(face['box'][3] * scale_y),
#             ]

#             # Scale the keypoints (left_eye, right_eye, etc.)
#             keypoints = face['keypoints']
#             keypoints['left_eye'] = (
#                 int(keypoints['left_eye'][0] * scale_x),
#                 int(keypoints['left_eye'][1] * scale_y)
#             )
#             keypoints['right_eye'] = (
#                 int(keypoints['right_eye'][0] * scale_x),
#                 int(keypoints['right_eye'][1] * scale_y)
#             )
#             keypoints['nose'] = (
#                 int(keypoints['nose'][0] * scale_x),
#                 int(keypoints['nose'][1] * scale_y)
#             )
#             keypoints['mouth_left'] = (
#                 int(keypoints['mouth_left'][0] * scale_x),
#                 int(keypoints['mouth_left'][1] * scale_y)
#             )
#             keypoints['mouth_right'] = (
#                 int(keypoints['mouth_right'][0] * scale_x),
#                 int(keypoints['mouth_right'][1] * scale_y)
#             )
#         return faces
    
#     def generate_dataset(self):
#         if self.variable_dept.get() == "Select Department" or self.variable_name.get() == "" or self.variable_id.get() == "":
#             messagebox.showerror("Error", "All fields are required", parent=self.root)
#         else:
#             try:
#                 conn = mysql.connector.connect(host="localhost", user="root", password="123456", database="face_recognizer")
#                 cursor = conn.cursor()

#                 # Extract only the numeric part of the ID (assuming the ID starts with 'BG0')
#                 full_id = self.variable_id.get()
#                 if full_id.startswith("BG0"):
#                     numeric_id = full_id[3:]  # Extract numeric part after 'BG0'

#                 # Ensure the numeric_id is valid (contains only digits)
#                 if numeric_id.isdigit():
#                     cursor.execute("SELECT * FROM details")
#                     result = cursor.fetchall()
#                     id = 0
#                     for x in result:
#                         id += 1

#                     # Now update the database using only the numeric part of the ID
#                     cursor.execute("""UPDATE details SET department=%s, designation=%s, name=%s, Gender=%s, DOB=%s, Address=%s, Phone_no=%s, radiobtn=%s 
#                                     WHERE id=%s""",
#                                 (
#                                     self.variable_dept.get(),
#                                     self.variable_designation.get(),
#                                     self.variable_name.get(),
#                                     self.variable_Gender.get(),
#                                     self.variable_DOB.get(),
#                                     self.variable_Address.get(),
#                                     self.variable_Phone_No.get(),
#                                     self.variable_radiobtn.get(),
#                                     numeric_id  # Insert only the numeric part (e.g., '1031')
#                                 ))

#                     conn.commit()
#                     self.fetch_data()
#                     self.reset_data()
#                     conn.close()

#                     ##### Face Detection OpenCV ######
#                     script_directory = os.path.dirname(os.path.abspath(__file__))
#                     data_directory = os.path.join(script_directory, "Data")
#                     if not os.path.exists(data_directory):
#                         os.makedirs(data_directory)

#                     def face_and_eye_cropped(img):
#                         faces = self.detect_faces(img)
#                         if not faces:
#                             print("No face detected.")
#                             return None

#                         for face in faces:
#                             x, y, w, h = face['box']
#                             keypoints = face['keypoints']

#                             cv2.circle(img, keypoints['left_eye'], 2, (0, 255, 0), 2)
#                             cv2.circle(img, keypoints['right_eye'], 2, (0, 255, 0), 2)

#                             if 'left_eye' in keypoints and 'right_eye' in keypoints:
#                                 return img[y:y + h, x:x + w]
#                             else:
#                                 return None

#                     cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
                    
#                     if not cap.isOpened():
#                         messagebox.showerror("Error", "Failed to open the camera.")
                    
#                     img_id = 0
#                     no_face_detected_count=0
                    
#                     while True:
#                         ret, my_frame = cap.read()
#                         if not ret or my_frame is None:
#                             messagebox.showerror("Error", "Failed to capture image from camera.")
#                             break
                        
#                         small_frame = cv2.resize(my_frame, (640, 480))
#                         face_crop = face_and_eye_cropped(small_frame) 
                        
#                         if face_and_eye_cropped(my_frame) is not None:
#                             img_id += 1
#                             face = cv2.resize(face_and_eye_cropped(my_frame), (320, 240))
#                             face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

#                             file_name_path = os.path.join(data_directory, "user." + str(numeric_id) + "." + str(img_id) + ".jpg")
#                             cv2.imwrite(file_name_path, face)

#                             cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
#                             cv2.imshow("Cropped_face", face)
                            
#                             no_face_detected_count = 0  # Reset counter if a face is detected
#                         else:
#                             no_face_detected_count += 1  # Increment if no face detected
#                             if no_face_detected_count >= 20:  # Set a threshold, e.g., 30 failed attempts
#                                 messagebox.showerror("Error", "No face detected after multiple attempts.")
#                                 break
                            
#                         if cv2.waitKey(1) == 13 or int(img_id) == 10:
#                             break

#                     cap.release()
#                     cv2.destroyAllWindows()
#                     if img_id > 0:
#                         messagebox.showinfo("Result", "Sample collected successfully")
#                     else:
#                         messagebox.showerror("Error", "No face detected, sample collection failed.")
#                 else:
#                     messagebox.showerror("Error", "ID must contain a numeric part after 'BG0'", parent=self.root)

#             except Exception as e:
#                 messagebox.showinfo("Error", f"Due to : {str(e)}", parent=self.root)
# if __name__ == "__main__":
#     root = Tk()
#     obj = Details(root)
#     root.mainloop()