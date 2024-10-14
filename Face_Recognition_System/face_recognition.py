# from logging import root
# from tkinter import *
# from tkinter import ttk
# from PIL import Image, ImageTk
# from tkinter import messagebox
# import os
# import numpy as np
# import cv2
# import mysql.connector
# from time import strftime
# from datetime import datetime
# import time

# class Face_recognition:
#     def __init__(self, root):  # root=Current_Window
#         self.root = root
#         self.root.geometry("1530x790+0+0")
#         self.root.title("Face Recognition Attendance System")

#         self.variable_id = StringVar()  # To store the ID
        
#         imagetop = Image.open(r"Face_Image\Face_recog8.jpg")
#         imagetop = imagetop.resize((1530, 300), Image.LANCZOS)
#         self.photoimagetop = ImageTk.PhotoImage(imagetop)

#         top_img = Label(self.root, image=self.photoimagetop)
#         top_img.place(x=0, y=0, width=1530, height=300)

#         btn_recognition = Button(self.root, bd=2, text="FACE RECOGNITION", command=self.face_recognition, cursor="hand2", fg="White", bg="Blue", font=("times new roman", 22, "bold"))
#         btn_recognition.place(x=0, y=300, width=1530, height=45)

#         imagebtmleft = Image.open(r"Face_Image\Face_recog4.jpg")
#         imagebtmleft = imagebtmleft.resize((800, 500), Image.LANCZOS)
#         self.photoimagebtmleft = ImageTk.PhotoImage(imagebtmleft)

#         btmleft_img = Label(self.root, image=self.photoimagebtmleft)
#         btmleft_img.place(x=0, y=345, width=800, height=500)

#         imagebtmright = Image.open(r"Face_Image\Face_recog2.jpg")
#         imagebtmright = imagebtmright.resize((800, 500), Image.LANCZOS)
#         self.photoimagebtmright = ImageTk.PhotoImage(imagebtmright)

#         btmright_img = Label(self.root, image=self.photoimagebtmright)
#         btmright_img.place(x=750, y=345, width=800, height=500)

#     def face_recognition(self):
#         def draw_boundary(img, classifier, scaleFactor, minNeighbor, color, text, clf):
#             grey_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#             features = classifier.detectMultiScale(grey_image, scaleFactor=1.1, minNeighbors=5)
            
#             coordinates = []
            
#             for (x, y, w, h) in features:
#                 cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
#                 E_id, predict = clf.predict(grey_image[y:y + h, x:x + w])
#                 confidence = int(100 * (1 - predict / 300))
                
#                 print(f"Predicted ID: {E_id}, Confidence: {confidence}")
                
#                 # Connect to the database and fetch the required data
#                 conn = mysql.connector.connect(host="localhost", user="root", password="123456", database="face_recognizer")
#                 cursor = conn.cursor()
        
#               #  Fetch the roll and name from the database        
#    #(set-1 from video)
#                 cursor.execute("SELECT id FROM details WHERE id=%s", (E_id,))
#                 # cursor.execute("SELECT id FROM details WHERE id = {}".format(id))
#                 roll=cursor.fetchone()
#                 #roll="+".join(roll)
#                 if roll:
#                     roll = "+".join(map(str, roll))  # Ensures that elements are converted to strings before joining
#                 else:
#                     roll = "Unknown"

#                 cursor.execute("SELECT name FROM details WHERE id=%s", (E_id,))
#                # N="+".join(N)
#                 N = cursor.fetchone()
#                 if N:
#                     N = "+".join(map(str, N))  # Ensures that elements are converted to strings before joining
#                 else:
#                     N = "Unknown"
#                 print(f"Fetched Roll: {roll}, Fetched Name: {N}")  

#                 if confidence > 80:
#                     cv2.putText(img, f"Name: {N}", (x, y - 55), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 3)
#                     cv2.putText(img, f"ID: {roll}", (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 3)
#                 else:
#                     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
#                     cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 3)

#                 coordinates = [x, y, w, h]
#             return coordinates

        # def draw_boundary(img, classifier, scaleFactor, minNeighbor, color, text, clf):
        #     grey_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #     features = classifier.detectMultiScale(grey_image, scaleFactor, minNeighbor)

        #     coordinates = []
            
        #     for (x, y, w, h) in features:
        #         cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
        #         id, predict = clf.predict(grey_image[y:y + h, x:x + w])
        #         confidence = int(100 * (1 - predict / 300))
                
        #         print(f"Predicted Numeric ID: {id}, Confidence: {confidence}")
                
        #         # Connect to the database and fetch the corresponding ID and name
        #         conn = mysql.connector.connect(host="localhost", user="root", password="123456", database="face_recognizer")
        #         cursor = conn.cursor()

        #         # Fetch the ID and name from the database
        #         query = "SELECT id, name FROM details WHERE id = %s"
        #         cursor.execute(query, (id,))  # Use the numeric ID to fetch the alphanumeric ID and name
        #         result = cursor.fetchone()

        #         if result:
        #             roll, name = result
        #             print(f"Fetched Roll: {roll}, Fetched Name: {name}")
        #         else:
        #             roll = "Unknown"
        #             name = "Unknown"
        #             print("No matching record found in the database.")

        #         # Display the data on the image
        #         if confidence > 40:
        #             cv2.putText(img, f"Name: {name}", (x, y - 55), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 3)
        #             cv2.putText(img, f"Roll: {roll}", (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 3)
        #         else:
        #             cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
        #             cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 3)

        #         coordinates = [x, y, w, h]
        #     return coordinates
        
#         def recognize(img, clf, faceCascade):
#             # if img is None:
#             #     print("No image captured")
#             #     return img
#             coordinates = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
#             return img

#         script_directory = os.path.dirname(os.path.abspath(__file__))
#         classifier_path = os.path.join(script_directory, "Classifier.xml")
#         haarcascade_path = os.path.join(script_directory, "haarcascade_frontalface_default.xml")

#         faceCascade = cv2.CascadeClassifier(haarcascade_path)
#         clf = cv2.face.LBPHFaceRecognizer_create()
#         try:
#             clf.read(classifier_path)
#         except Exception as e:
#             print(f"Failed to open Classifier.xml file: {e}")
#             return

#         print("Opening camera...")
#         video_cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
#         print("Camera opened!")
#         # time.sleep(2)
#         # if not video_cap.isOpened():
#         #     print("Error: Could not open video capture.")
#         #     return

#         while True:
#             ret, img = video_cap.read()
#             # if not ret:
#             #     print("Error: Could not read frame.")
#             #     break

#             img = recognize(img, clf, faceCascade)
#             cv2.imshow("Welcome to Face_recognition", img)

#             if cv2.waitKey(1) == 13:  # Enter key to exit
#                 break
            
#         video_cap.release()
#         cv2.destroyAllWindows()

# if __name__ == "__main__":
#     root = Tk()
#     obj = Face_recognition(root)
#     root.mainloop()

                ##############              Working one

# import threading
# from tkinter import *
# from PIL import Image, ImageTk
# import os
# import cv2
# import mysql.connector
# from mtcnn import MTCNN
# import concurrent.futures
# from time import strftime
# from datetime import datetime
# import time

# class Face_recognition:
#     def __init__(self, root):  # root=Current_Window
#         self.root = root
#         self.root.geometry("1530x790+0+0")
#         self.root.title("Face Recognition Attendance System")

#         self.variable_id = StringVar()  # To store the ID

#         # Top Image
#         imagetop = Image.open(r"Face_Image\Face_recog8.jpg")
#         imagetop = imagetop.resize((1530, 300), Image.LANCZOS)
#         self.photoimagetop = ImageTk.PhotoImage(imagetop)
#         top_img = Label(self.root, image=self.photoimagetop)
#         top_img.place(x=0, y=0, width=1530, height=300)

#         # Recognition Button
#         btn_recognition = Button(self.root, bd=2, text="FACE RECOGNITION", command=self.start_recognition_thread, cursor="hand2", fg="White", bg="Blue", font=("times new roman", 22, "bold"))
#         btn_recognition.place(x=0, y=300, width=1530, height=45)

#         # Bottom Left Image
#         imagebtmleft = Image.open(r"Face_Image\Face_recog4.jpg")
#         imagebtmleft = imagebtmleft.resize((800, 500), Image.LANCZOS)
#         self.photoimagebtmleft = ImageTk.PhotoImage(imagebtmleft)
#         btmleft_img = Label(self.root, image=self.photoimagebtmleft)
#         btmleft_img.place(x=0, y=345, width=800, height=500)

#         # Bottom Right Image
#         imagebtmright = Image.open(r"Face_Image\Face_recog2.jpg")
#         imagebtmright = imagebtmright.resize((800, 500), Image.LANCZOS)
#         self.photoimagebtmright = ImageTk.PhotoImage(imagebtmright)
#         btmright_img = Label(self.root, image=self.photoimagebtmright)
#         btmright_img.place(x=750, y=345, width=800, height=500)

#     def start_recognition_thread(self):
#         # Run face recognition in a separate thread to prevent GUI freezing
#         recognition_thread = threading.Thread(target=self.face_recognition)
#         recognition_thread.daemon = True
#         recognition_thread.start()

#     def detect_faces(self, img, clf):
#         detector = MTCNN()  # Initialize MTCNN face detector
#         faces = detector.detect_faces(img)
#         #self.faces = faces
#         return faces
    
#     def face_recognition(self):
#         def recognize_faces(img, clf):
#             detector = MTCNN()  # Initialize MTCNN face detector
#             faces = detector.detect_faces(img)
            
#             if not faces:
#                 print("No faces detected.")
#                 return img  # No faces found, return original image

#             for face in faces:
#                 x, y, w, h = face['box']  # Extract the bounding box coordinates
#                 cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

#                 # Convert the region of interest (face) to grayscale for recognition
#                 roi_gray = cv2.cvtColor(img[y:y + h, x:x + w], cv2.COLOR_BGR2GRAY)

#                 try:
#                     E_id, predict = clf.predict(roi_gray)
#                     confidence = int(100 * (1 - predict / 300))

#                     # Connect to the database to fetch name and ID
#                     conn = mysql.connector.connect(host="localhost", user="root", password="123456", database="face_recognizer")
#                     cursor = conn.cursor()

#                     # Fetch ID and name from the database based on predicted ID
#                     cursor.execute("SELECT id FROM details WHERE id=%s", (E_id,))
#                     roll = cursor.fetchone()
#                     roll = "+".join(map(str, roll)) if roll else "Unknown"

#                     cursor.execute("SELECT name FROM details WHERE id=%s", (E_id,))
#                     N = cursor.fetchone()
#                     N = "+".join(map(str, N)) if N else "Unknown"

#                     print(f"Recognized face with ID: {roll}, Name: {N}, Confidence: {confidence}")  # Debugging output

#                     if confidence > 80:
#                         cv2.putText(img, f"Name: {N}", (x, y - 55), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
#                         cv2.putText(img, f"ID: {roll}", (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
#                     else:
#                         cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
#                         cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
#                 except cv2.error as e:
#                     print(f"Error predicting face: {e}")

#             return img  # Return the image with bounding boxes and recognition results

#         # Load classifier and Haar cascade
#         script_directory = os.path.dirname(os.path.abspath(__file__))
#         classifier_path = os.path.join(script_directory, "Classifier.xml")
        
#         clf = cv2.face.LBPHFaceRecognizer_create(radius=2, neighbors=8, grid_x=8, grid_y=8)

#         try:
#             clf.read(classifier_path)
#         except Exception as e:
#             print(f"Failed to open Classifier.xml file: {e}")
#             return

#         # Open the camera and start recognition
#         video_cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

#         while True:
#             ret, img = video_cap.read()
#             if not ret:
#                 print("Error: Could not read frame.")
#                 break
            
#             with concurrent.futures.ThreadPoolExecutor() as executor:
#                 futures = []
#                 for _ in range(5):  # Adjust the number of threads as needed
#                     future = executor.submit(self.detect_faces, img, clf)
#                     futures.append(future)

#             # Wait for all threads to finish
#                 faces = []
#                 for future in futures:
#                     faces.extend(future.result()) 

#             img = recognize_faces(img, clf)  # <--- Add this line here
#             cv2.imshow("Face Recognition", img)

#             if cv2.waitKey(1) == 13:  # Enter key to exit
#                 break

#         video_cap.release()
#         cv2.destroyAllWindows()

# if __name__ == "__main__":
#     root = Tk()
#     obj = Face_recognition(root)
#     root.mainloop()

###########               Working One using concurrent features

# import threading
# from tkinter import *
# from PIL import Image, ImageTk
# import os
# import cv2
# import mysql.connector
# from mtcnn import MTCNN
# import concurrent.futures
# from time import strftime
# from datetime import datetime
# import time

# class Face_recognition:
#     def __init__(self, root):  # root=Current_Window
#         self.root = root
#         self.root.geometry("1530x790+0+0")
#         self.root.title("Face Recognition Attendance System")

#         self.variable_id = StringVar()  # To store the ID

#         # Top Image
#         imagetop = Image.open(r"Face_Image\Face_recog8.jpg")
#         imagetop = imagetop.resize((1530, 300), Image.LANCZOS)
#         self.photoimagetop = ImageTk.PhotoImage(imagetop)
#         top_img = Label(self.root, image=self.photoimagetop)
#         top_img.place(x=0, y=0, width=1530, height=300)

#         # Recognition Button
#         btn_recognition = Button(self.root, bd=2, text="FACE RECOGNITION", command=self.start_recognition_thread, cursor="hand2", fg="White", bg="Blue", font=("times new roman", 22, "bold"))
#         btn_recognition.place(x=0, y=300, width=1530, height=45)

#         # Bottom Left Image
#         imagebtmleft = Image.open(r"Face_Image\Face_recog4.jpg")
#         imagebtmleft = imagebtmleft.resize((800, 500), Image.LANCZOS)
#         self.photoimagebtmleft = ImageTk.PhotoImage(imagebtmleft)
#         btmleft_img = Label(self.root, image=self.photoimagebtmleft)
#         btmleft_img.place(x=0, y=345, width=800, height=500)

#         # Bottom Right Image
#         imagebtmright = Image.open(r"Face_Image\Face_recog2.jpg")
#         imagebtmright = imagebtmright.resize((800, 500), Image.LANCZOS)
#         self.photoimagebtmright = ImageTk.PhotoImage(imagebtmright)
#         btmright_img = Label(self.root, image=self.photoimagebtmright)
#         btmright_img.place(x=750, y=345, width=800, height=500)
        

#     def start_recognition_thread(self):
#         # Run face recognition in a separate thread to prevent GUI freezing
#         recognition_thread = threading.Thread(target=self.face_recognition)
#         recognition_thread.daemon = True
#         recognition_thread.start()

#     # def detect_faces(self, img):
#     #     detector = MTCNN()  # Initialize MTCNN face detector
#     #     faces = detector.detect_faces(img)
#     #     #self.faces = faces
#     #     return faces
#     def detect_faces(self, img):
#         faces = self.detector.detect_faces(img)
#         return faces
    
    # def face_recognition(self):
    #     def recognize_faces(img,clf,faces):
    #         detector = MTCNN()  # Initialize MTCNN face detector
    #         faces = detector.detect_faces(img)
            
    #         if not faces:
    #             print("No faces detected.")
    #             return img  # No faces found, return original image

    #         for face in faces:
    #             x, y, w, h = face['box']  # Extract the bounding box coordinates
    #             cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    #             # Convert the region of interest (face) to grayscale for recognition
    #             roi_gray = cv2.cvtColor(img[y:y + h, x:x + w], cv2.COLOR_BGR2GRAY)

    #             try:
    #                 E_id, predict = clf.predict(roi_gray)
    #                 confidence = int(100 * (1 - predict / 300))

    #                 # Connect to the database to fetch name and ID
    #                 conn = mysql.connector.connect(host="localhost", user="root", password="123456", database="face_recognizer")
    #                 cursor = conn.cursor()

    #                 # Fetch ID and name from the database based on predicted ID
    #                 cursor.execute("SELECT id FROM details WHERE id=%s", (E_id,))
    #                 roll = cursor.fetchone()
    #                 roll = "+".join(map(str, roll)) if roll else "Unknown"

    #                 cursor.execute("SELECT name FROM details WHERE id=%s", (E_id,))
    #                 N = cursor.fetchone()
    #                 N = "+".join(map(str, N)) if N else "Unknown"

    #                 print(f"Recognized face with ID: {roll}, Name: {N}, Confidence: {confidence}")  # Debugging output

    #                 if confidence > 80:
    #                     cv2.putText(img, f"Name: {N}", (x, y - 55), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    #                     cv2.putText(img, f"ID: {roll}", (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    #                 else:
    #                     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    #                     cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    #             except cv2.error as e:
    #                 print(f"Error predicting face: {e}")

    #         return img  # Return the image with bounding boxes and recognition results

    #     # Load classifier and Haar cascade
    #     script_directory = os.path.dirname(os.path.abspath(__file__))
    #     classifier_path = os.path.join(script_directory, "Classifier.xml")
        
    #     clf = cv2.face.LBPHFaceRecognizer_create(radius=2, neighbors=8, grid_x=8, grid_y=8)

    #     try:
    #         clf.read(classifier_path)
    #     except Exception as e:
    #         print(f"Failed to open Classifier.xml file: {e}")
    #         return

    #     # Open the camera and start recognition
    #     video_cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    #     while True:
    #         ret, img = video_cap.read()
    #         if not ret:
    #             print("Error: Could not read frame.")
    #             break
            
    #         with concurrent.futures.ThreadPoolExecutor() as executor:
    #             futures = []
    #             for _ in range(5):  # Adjust the number of threads as needed
    #                 future = executor.submit(self.detect_faces, img, clf)
    #                 futures.append(future)

    #         # Wait for all threads to finish
    #             faces = []
    #             for future in futures:
    #                 faces.extend(future.result()) 

    #         img = recognize_faces(img, clf,faces)  # <--- Add this line here
    #         cv2.imshow("Face Recognition", img)

    #         if cv2.waitKey(1) == 13:  # Enter key to exit
    #             break

    #     video_cap.release()
    #     cv2.destroyAllWindows()
# if __name__ == "__main__":
#     root = Tk()
#     obj = Face_recognition(root)
#     root.mainloop()


# import threading
# from tkinter import *
# from PIL import Image, ImageTk
# import os
# import cv2
# import mysql.connector
# import mediapipe as mp
# import numpy as np

# class FaceRecognition:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("1530x790+0+0")
#         self.root.title("Face Recognition Attendance System")

#         self.variable_id = StringVar()  # To store the ID

#         # Top Image
#         imagetop = Image.open(r"Face_Image\Face_recog8.jpg"
# )
#         imagetop = imagetop.resize((1530, 300), Image.LANCZOS)
#         self.photoimagetop = ImageTk.PhotoImage(imagetop)
#         top_img = Label(self.root, image=self.photoimagetop)
#         top_img.place(x=0, y=0, width=1530, height=300)

#         # Recognition Button
#         btn_recognition = Button(self.root, bd=2, text="FACE RECOGNITION", command=self.start_recognition_thread, cursor="hand2", fg="White", bg="Blue", font=("times new roman", 22, "bold"))
#         btn_recognition.place(x=0, y=300, width=1530, height=45)

#         # Bottom Left Image
#         imagebtmleft = Image.open(r"Face_Image\Face_recog4.jpg")
#         imagebtmleft = imagebtmleft.resize((800, 500), Image.LANCZOS)
#         self.photoimagebtmleft = ImageTk.PhotoImage(imagebtmleft)
#         btmleft_img = Label(self.root, image=self.photoimagebtmleft)
#         btmleft_img.place(x=0, y=345, width=800, height=500)

#         # Bottom Right Image
#         imagebtmright = Image.open(r"Face_Image\Face_recog2.jpg")
#         imagebtmright = imagebtmright.resize((800, 500), Image.LANCZOS)
#         self.photoimagebtmright = ImageTk.PhotoImage(imagebtmright)
#         btmright_img = Label(self.root, image=self.photoimagebtmright)
#         btmright_img.place(x=750, y=345, width=800, height=500)

#         # Initialize MediaPipe Face Detection
#         self.mp_face_detection = mp.solutions.face_detection
#         self.face_detection = self.mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.3)

#         script_directory = os.path.dirname(os.path.abspath(__file__))
#         classifier_path = os.path.join(script_directory, "Classifier.xml")

#         # Initialize face recognizer
#         try:
#             self.clf = cv2.face.LBPHFaceRecognizer_create()
#             self.clf.read(classifier_path)
#             print("Classifier model loaded successfully.")
#         except cv2.error as e:
#             print(f"Error loading classifier model: {e}")
#             exit(1)

#         # Pre-fetch user data from the database
#         try:
#             conn = mysql.connector.connect(host="localhost", user="root", password="123456", database="face_recognizer")
#             cursor = conn.cursor()
#             cursor.execute("SELECT id, name FROM details")
#             user_info = cursor.fetchall()
#             self.user_dict = {user_id: name for user_id, name in user_info}
#             cursor.close()
#             conn.close()
#         except mysql.connector.Error as err:
#             print(f"Error connecting to MySQL: {err}")
#             exit(1)

#     def start_recognition_thread(self):
#         print("Recognition button clicked")  # Debugging: check if button click is registered
#         recognition_thread = threading.Thread(target=self.face_recognition)
#         recognition_thread.daemon = True
#         recognition_thread.start()

#     def face_recognition(self):
#         try:
#             print("Starting face recognition...")  # Debugging statement
#             video_cap = cv2.VideoCapture(0)
#             if not video_cap.isOpened():
#                 print("Error: Cannot access camera.")
#                 return

#             video_cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#             video_cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

#             while True:
#                 ret, frame = video_cap.read()
#                 if not ret:
#                     print("Error: Could not read frame.")
#                     break

#                 print("Frame captured.")  # Debugging statement

#                 rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#                 results = self.face_detection.process(rgb_frame)

#                 if results.detections:
#                     print(f"{len(results.detections)} face(s) detected.")  # Debugging statement
#                     for detection in results.detections:
#                         bbox = detection.location_data.relative_bounding_box
#                         h, w, _ = frame.shape
#                         x_min = int(bbox.xmin * w)
#                         y_min = int(bbox.ymin * h)
#                         width = int(bbox.width * w)
#                         height = int(bbox.height * h)
#                         x_min = max(0, x_min)
#                         y_min = max(0, y_min)
#                         x_max = min(w, x_min + width)
#                         y_max = min(h, y_min + height)

#                         face_roi = frame[y_min:y_max, x_min:x_max]
#                         gray_face = cv2.cvtColor(face_roi, cv2.COLOR_BGR2GRAY)
#                         resized_face = cv2.resize(gray_face, (100, 100))

#                         if resized_face.size == 0:
#                             continue

#                         try:
#                             E_id, confidence = self.clf.predict(resized_face)
#                             confidence = 100 - confidence

#                             name = self.user_dict.get(E_id, "Unknown")

#                             if confidence > 50:
#                                 cv2.putText(frame, f"Name: {name}", (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)
#                             else:
#                                 cv2.putText(frame, "Unknown", (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
#                         except Exception as e:
#                             print(f"Recognition Error: {e}")
#                             cv2.putText(frame, "Recognition Error", (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
#                 else:
#                     print("No faces detected.")  # Debugging statement

#                 cv2.imshow("Face Recognition", frame)
#                 if cv2.waitKey(1) & 0xFF == ord('q'):
#                     break

#             video_cap.release()
#             cv2.destroyAllWindows()

#         except Exception as e:
#             print(f"Error in face recognition thread: {e}")

# if __name__ == "__main__":
#     root = Tk()
#     obj = FaceRecognition(root)
#     root.mainloop()

# import threading
# from tkinter import *
# from PIL import Image, ImageTk
# import os
# import cv2
# import mysql.connector
# from mtcnn import MTCNN

# class Face_recognition:
#     def __init__(self, root):  # root=Current_Window
#         self.root = root
#         self.root.geometry("1530x790+0+0")
#         self.root.title("Face Recognition Attendance System")

#         self.variable_id = StringVar()  # To store the ID

#         # Top Image
#         imagetop = Image.open(r"Face_Image\Face_recog8.jpg")
#         imagetop = imagetop.resize((1530, 300), Image.LANCZOS)
#         self.photoimagetop = ImageTk.PhotoImage(imagetop)
#         top_img = Label(self.root, image=self.photoimagetop)
#         top_img.place(x=0, y=0, width=1530, height=300)

#         # Recognition Button
#         btn_recognition = Button(
#             self.root, 
#             bd=2, 
#             text="FACE RECOGNITION", 
#             command=self.start_recognition_thread, 
#             cursor="hand2", 
#             fg="White", 
#             bg="Blue", 
#             font=("times new roman", 22, "bold")
#         )
#         btn_recognition.place(x=0, y=300, width=1530, height=45)

#         # Bottom Left Image
#         imagebtmleft = Image.open(r"Face_Image\Face_recog4.jpg")
#         imagebtmleft = imagebtmleft.resize((800, 500), Image.LANCZOS)
#         self.photoimagebtmleft = ImageTk.PhotoImage(imagebtmleft)
#         btmleft_img = Label(self.root, image=self.photoimagebtmleft)
#         btmleft_img.place(x=0, y=345, width=800, height=500)

#         # Bottom Right Image
#         imagebtmright = Image.open(r"Face_Image\Face_recog2.jpg")
#         imagebtmright = imagebtmright.resize((800, 500), Image.LANCZOS)
#         self.photoimagebtmright = ImageTk.PhotoImage(imagebtmright)
#         btmright_img = Label(self.root, image=self.photoimagebtmright)
#         btmright_img.place(x=750, y=345, width=800, height=500)

#         # Initialize resources
#         self.initialize_resources()

#     def initialize_resources(self):
#         # Initialize MTCNN face detector
#         self.detector = MTCNN()

#         # Initialize classifier
#         script_directory = os.path.dirname(os.path.abspath(__file__))
#         classifier_path = os.path.join(script_directory, "Classifier.xml")
#         self.clf = cv2.face.LBPHFaceRecognizer_create()
#         try:
#             self.clf.read(classifier_path)
#             print("Classifier loaded successfully.")
#         except Exception as e:
#             print(f"Failed to open Classifier.xml file: {e}")
#             self.clf = None

#         # Initialize database connection
#         try:
#             self.conn = mysql.connector.connect(
#                 host="localhost", 
#                 user="root", 
#                 password="123456", 
#                 database="face_recognizer"
#             )
#             self.cursor = self.conn.cursor()
#             print("Database connection established.")
#         except mysql.connector.Error as err:
#             print(f"Error connecting to database: {err}")
#             self.conn = None
#             self.cursor = None

#         # Initialize video capture
#         self.video_cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
#         if not self.video_cap.isOpened():
#             print("Error: Could not open video capture.")
#             self.video_cap = None

#         # Flag to control the loop
#         self.running = False

#     def start_recognition_thread(self):
#         if not self.running:
#             self.running = True
#             recognition_thread = threading.Thread(target=self.face_recognition, daemon=True)
#             recognition_thread.start()

#     def stop_recognition(self):
#         self.running = False
#         if self.video_cap and self.video_cap.isOpened():
#             self.video_cap.release()
#         cv2.destroyAllWindows()
#         if self.conn:
#             self.cursor.close()
#             self.conn.close()
#         print("Recognition stopped and resources released.")

#     def face_recognition(self):
#         if not all([self.detector, self.clf, self.cursor, self.video_cap]):
#             print("Necessary resources not initialized. Exiting recognition.")
#             return

#         while self.running:
#             ret, img = self.video_cap.read()
#             if not ret:
#                 print("Error: Could not read frame.")
#                 break

#             # Optionally resize the image for faster processing
#             img_resized = cv2.resize(img, (640, 480))
#             img_processed = self.recognize_faces(img_resized)

#             cv2.imshow("Face Recognition", img_processed)

#             # Exit on Enter key
#             if cv2.waitKey(1) & 0xFF == 13:
#                 self.stop_recognition()
#                 break

#         self.stop_recognition()

#     def recognize_faces(self, img):
#         faces = self.detector.detect_faces(img)
        
#         if not faces:
#             # No faces detected; return original image
#             return img

#         for face in faces:
#             x, y, w, h = face['box']
#             # Ensure coordinates are within image bounds
#             x, y = max(0, x), max(0, y)
#             w, h = max(0, w), max(0, h)
#             cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

#             # Extract the face ROI and convert to grayscale
#             roi_gray = cv2.cvtColor(img[y:y + h, x:x + w], cv2.COLOR_BGR2GRAY)

#             try:
#                 E_id, predict = self.clf.predict(roi_gray)
#                 confidence = int(100 * (1 - predict / 300))

#                 # Fetch ID and name from the database
#                 self.cursor.execute("SELECT id, name FROM details WHERE id=%s", (E_id,))
#                 result = self.cursor.fetchone()
#                 if result:
#                     roll, name = result
#                 else:
#                     roll, name = "Unknown", "Unknown"

#                 print(f"Recognized face with ID: {roll}, Name: {name}, Confidence: {confidence}")

#                 if confidence > 80:
#                     cv2.putText(
#                         img, 
#                         f"Name: {name}", 
#                         (x, y - 55), 
#                         cv2.FONT_HERSHEY_SIMPLEX, 
#                         0.8, 
#                         (255, 255, 255), 
#                         2
#                     )
#                     cv2.putText(
#                         img, 
#                         f"ID: {roll}", 
#                         (x, y - 30), 
#                         cv2.FONT_HERSHEY_SIMPLEX, 
#                         0.8, 
#                         (255, 255, 255), 
#                         2
#                     )
#                 else:
#                     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
#                     cv2.putText(
#                         img, 
#                         "Unknown Face", 
#                         (x, y - 5), 
#                         cv2.FONT_HERSHEY_SIMPLEX, 
#                         0.8, 
#                         (255, 255, 255), 
#                         2
#                     )
#             except cv2.error as e:
#                 print(f"Error predicting face: {e}")
#             except mysql.connector.Error as db_err:
#                 print(f"Database error: {db_err}")

#         return img

#     def on_closing(self):
#         self.stop_recognition()
#         self.root.destroy()

# if __name__ == "__main__":
#     root = Tk()
#     obj = Face_recognition(root)
#     root.protocol("WM_DELETE_WINDOW", obj.on_closing)  # Handle window closing
#     root.mainloop()

############  Working one Latest ####################

# import threading
# from tkinter import *
# from PIL import Image, ImageTk
# import os
# import cv2
# import mysql.connector
# from mtcnn import MTCNN
# import concurrent.futures
# from time import strftime
# from datetime import datetime
# import time


# class Face_recognition:
#     def __init__(self, root):  # root=Current_Window
#         self.root = root
#         self.root.geometry("1530x790+0+0")
#         self.root.title("Face Recognition Attendance System")

#         self.variable_id = StringVar()  # To store the ID
#         # Top Image
#         imagetop = Image.open(r"Face_Image\Face_recog8.jpg")
#         imagetop = imagetop.resize((1530, 300), Image.LANCZOS)
#         self.photoimagetop = ImageTk.PhotoImage(imagetop)
#         top_img = Label(self.root, image=self.photoimagetop)
#         top_img.place(x=0, y=0, width=1530, height=300)

#         # Recognition Button
#         btn_recognition = Button(self.root, bd=2, text="FACE RECOGNITION", command=self.start_recognition_thread, cursor="hand2", fg="White", bg="Blue", font=("times new roman", 22, "bold"))
#         btn_recognition.place(x=0, y=300, width=1530, height=45)

#         # Bottom Left Image
#         imagebtmleft = Image.open(r"Face_Image\Face_recog4.jpg")
#         imagebtmleft = imagebtmleft.resize((800, 500), Image.LANCZOS)
#         self.photoimagebtmleft = ImageTk.PhotoImage(imagebtmleft)
#         btmleft_img = Label(self.root, image=self.photoimagebtmleft)
#         btmleft_img.place(x=0, y=345, width=800, height=500)

#         # Bottom Right Image
#         imagebtmright = Image.open(r"Face_Image\Face_recog2.jpg")
#         imagebtmright = imagebtmright.resize((800, 500), Image.LANCZOS)
#         self.photoimagebtmright = ImageTk.PhotoImage(imagebtmright)
#         btmright_img = Label(self.root, image=self.photoimagebtmright)
#         btmright_img.place(x=750, y=345, width=800, height=500)

#         # Initialize the face detector (MTCNN) and the classifier (LBPH recognizer)
#         self.detector = MTCNN()  # <-- This line initializes the MTCNN detector

#     def start_recognition_thread(self):
#         # Run face recognition in a separate thread to prevent GUI freezing
#         recognition_thread = threading.Thread(target=self.face_recognition)
#         recognition_thread.daemon = True
#         recognition_thread.start()
    
#     def face_recognition_cycle(self):
#     # This method will be used for an infinite cycle of face recognition when the button is pressed.
#         while True:
#             self.face_recognition()  # Run face recognition when button is clicked
#             time.sleep(2)

#     def detect_faces(self, img):
#         faces = self.detector.detect_faces(img)  # Use the pre-initialized detector
#         return faces

#     def recognize_faces(self, img, clf, faces):
#         faces=self.detect_faces(img)
#         if not faces:
#             print("No faces detected.")
#             return img  # No faces found, return original image

#         for face in faces:
#             x, y, w, h = face['box']  # Extract the bounding box coordinates
#             cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

#             # Convert the region of interest (face) to grayscale for recognition
#             roi_gray = cv2.cvtColor(img[y:y + h, x:x + w], cv2.COLOR_BGR2GRAY)

#             try:
#                 E_id, predict = clf.predict(roi_gray)
#                 confidence = int(100 * (1 - predict / 300))

#                 # Connect to the database to fetch name and ID
#                 conn = mysql.connector.connect(host="localhost", user="root", password="123456", database="face_recognizer")
#                 cursor = conn.cursor()

#                 # Fetch ID and name from the database based on predicted ID
#                 cursor.execute("SELECT id FROM details WHERE id=%s", (E_id,))
#                 roll = cursor.fetchone()
#                 roll = "+".join(map(str, roll)) if roll else "Unknown"

#                 cursor.execute("SELECT name FROM details WHERE id=%s", (E_id,))
#                 N = cursor.fetchone()
#                 N = "+".join(map(str, N)) if N else "Unknown"

#                 print(f"Recognized face with ID: {roll}, Name: {N}, Confidence: {confidence}")

#                 if confidence > 80:
#                     cv2.putText(img, f"Name: {N}", (x, y - 55), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
#                     cv2.putText(img, f"ID: {roll}", (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
#                 else:
#                     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
#                     cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
#             except cv2.error as e:
#                 print(f"Error predicting face: {e}")

#         return img

#     def face_recognition(self):
        
#         script_directory = os.path.dirname(os.path.abspath(__file__))
#         classifier_path = os.path.join(script_directory, "Classifier.xml")

#         clf = cv2.face.LBPHFaceRecognizer_create(radius=2, neighbors=5, grid_x=8, grid_y=8)

#         try:
#             clf.read(classifier_path)
#         except Exception as e:
#             print(f"Failed to open Classifier.xml file: {e}")
#             return
#         # Open the camera and start recognition
#         video_cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

#         while True:
#             ret, img = video_cap.read()
#             if not ret:
#                 print("Error: Could not read frame.")
#                 break

#             # Run face detection in the background using a thread pool
#             with concurrent.futures.ThreadPoolExecutor() as executor:
#                 future = executor.submit(self.detect_faces, img)
#                 faces = future.result()

#             # Perform face recognition on the detected faces
#             img = self.recognize_faces(img,clf,faces)

#             # Show the resulting image with face boxes and details
#             cv2.imshow("Face Recognition", img)

#             if cv2.waitKey(1) == 13:  # Enter key to exit
#                 break

#         video_cap.release()
#         cv2.destroyAllWindows()

# if __name__ == "__main__":
#     root = Tk()
#     obj = Face_recognition(root)
#     root.mainloop()
    
#################   22.09.2024 #############        New one testing 

import threading
from tkinter import *
from PIL import Image, ImageTk
import os
import cv2
import mysql.connector
from mtcnn import MTCNN
import concurrent.futures
from time import strftime
from datetime import datetime
import time

class Face_recognition:
    def __init__(self, root):  # root=Current_Window
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition Attendance System")

        self.variable_id = StringVar()  # To store the ID
        # Top Image
        imagetop = Image.open(r"Face_Image\Face_recog8.jpg")
        imagetop = imagetop.resize((1530, 300), Image.LANCZOS)
        self.photoimagetop = ImageTk.PhotoImage(imagetop)
        top_img = Label(self.root, image=self.photoimagetop)
        top_img.place(x=0, y=0, width=1530, height=300)

        # Recognition Button
        btn_recognition = Button(self.root, bd=2, text="FACE RECOGNITION", command=self.start_recognition_thread, cursor="hand2", fg="White", bg="Blue", font=("times new roman", 22, "bold"))
        btn_recognition.place(x=0, y=300, width=1530, height=45)

        # Bottom Left Image
        imagebtmleft = Image.open(r"Face_Image\Face_recog4.jpg")
        imagebtmleft = imagebtmleft.resize((800, 500), Image.LANCZOS)
        self.photoimagebtmleft = ImageTk.PhotoImage(imagebtmleft)
        btmleft_img = Label(self.root, image=self.photoimagebtmleft)
        btmleft_img.place(x=0, y=345, width=800, height=500)

        # Bottom Right Image
        imagebtmright = Image.open(r"Face_Image\Face_recog2.jpg")
        imagebtmright = imagebtmright.resize((800, 500), Image.LANCZOS)
        self.photoimagebtmright = ImageTk.PhotoImage(imagebtmright)
        btmright_img = Label(self.root, image=self.photoimagebtmright)
        btmright_img.place(x=750, y=345, width=800, height=500)

        # Initialize the face detector (MTCNN) and the classifier (LBPH recognizer)
        self.detector = MTCNN()  # <-- This line initializes the MTCNN detector

    ############### attendance ##################
    
    def mark_attendance(self,N,roll,D):
        script_directory = os.path.dirname(os.path.abspath(__file__))
        attendance_path = os.path.join(script_directory, "attendance.csv")
        with open(attendance_path,"r+",newline="\n") as f:
            myDataList=f.readlines()

            name_list=[] 
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            
            if((N not in name_list) and (roll not in name_list) and (D not in name_list)):
                now=datetime.now()
                full_date=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{N},{roll},{D},{dtString},{full_date},Present")
                   
    def start_recognition_thread(self):
        # Run face recognition in a separate thread to prevent GUI freezing
        recognition_thread = threading.Thread(target=self.face_recognition)
        recognition_thread.daemon = True
        recognition_thread.start()
    
    def face_recognition_cycle(self):
    # This method will be used for an infinite cycle of face recognition when the button is pressed.
        while True:
            self.face_recognition()  # Run face recognition when button is clicked
            time.sleep(2)

    def detect_faces(self, img):
        faces = self.detector.detect_faces(img)  # Use the pre-initialized detector
        return faces

    def recognize_faces(self, img, clf, faces):
        faces=self.detect_faces(img)
        if not faces:
            print("No faces detected")
            return img  # No faces found, return original image

        for face in faces:
            x, y, w, h = face['box']  # Extract the bounding box coordinates
            keypoints = face['keypoints']
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            cv2.circle(img, keypoints['left_eye'], 2, (0, 255, 0), 2)  # Left eye
            cv2.circle(img, keypoints['right_eye'], 2, (0, 255, 0), 2) # Right Eye
            cv2.circle(img, keypoints['nose'], 2, (255, 0, 0), 2)  # Nose
            cv2.circle(img, keypoints['mouth_left'], 2, (255, 0, 0), 2)  # Left corner of mouth
            cv2.circle(img, keypoints['mouth_right'], 2, (255, 0, 0), 2) # Right corner

            if 'left_eye' in keypoints and 'right_eye' in keypoints:
                print("Eyes detected.")
      
            # Convert the region of interest (face) to grayscale for recognition
            roi_gray = cv2.cvtColor(img[y:y + h, x:x + w], cv2.COLOR_BGR2GRAY)
            try:
                E_id, predict = clf.predict(roi_gray)
                confidence = int(100 * (1 - predict / 300))

                # Connect to the database to fetch name and ID
                conn = mysql.connector.connect(host="localhost", user="root", password="123456", database="face_recognizer")
                cursor = conn.cursor()

                # Fetch ID and name from the database based on predicted ID
                # cursor.execute("SELECT id FROM details WHERE id=%s", (E_id,))
                # roll = cursor.fetchone()
                # roll = "+".join(map(str, roll)) if roll else "Unknown"

                # cursor.execute("SELECT name FROM details WHERE id=%s", (E_id,))
                # N = cursor.fetchone()
                # N = "+".join(map(str, N)) if N else "Unknown"
                
                # cursor.execute("SELECT department FROM details WHERE id=%s", (E_id,))
                # D = cursor.fetchone()
                # D = "+".join(map(str, D)) if N else "Unknown"

                cursor.execute("SELECT id, name, department FROM details WHERE id=%s", (E_id,))
                result = cursor.fetchone()

                if result:
                    numeric_id, N, D = result  # Unpack the tuple
                    roll = f"BG{numeric_id}"   # Reconstruct the full ID by adding "BG" prefix
                else:
                    roll, N, D = "Unknown", "Unknown", "Unknown"
                    
                print(f"Recognized face with ID: {roll}, Name: {N},Department: {D} Confidence: {confidence}")

                if confidence > 80:
                    cv2.putText(img, f"Name: {N}", (x, y - 55), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"ID: {roll}", (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Department: {D}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
                    self.mark_attendance(roll,N,D)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
            except cv2.error as e:
                print(f"Error predicting face: {e}")
        return img

    def face_recognition(self):
        script_directory = os.path.dirname(os.path.abspath(__file__))
        classifier_path = os.path.join(script_directory, "Classifier.xml")
        clf = cv2.face.LBPHFaceRecognizer_create(radius=2, neighbors=5, grid_x=8, grid_y=8)

        try:
            clf.read(classifier_path)
        except Exception as e:
            print(f"Failed to open Classifier.xml file: {e}")
            return
        # Open the camera and start recognition
        video_cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        while True:
            ret, img = video_cap.read()
            if not ret:
                print("Error: Could not read frame.")
                break

            # Run face detection in the background using a thread pool
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(self.detect_faces, img)
                faces = future.result()

            # Perform face recognition on the detected faces
            img = self.recognize_faces(img,clf,faces)
            # Show the resulting image with face boxes and details
            cv2.imshow("Face Recognition", img)
            if cv2.waitKey(1) == 13:  # Enter key to exit
                break
            
        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition(root)
    root.mainloop()