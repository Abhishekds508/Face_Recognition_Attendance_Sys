This Face Recognition Attendance System is built using Python and uses real-time facial recognition to automate attendance. 
The system provides multiple interfaces to manage the registration, recognition, and attendance process efficiently.

Features
  Real-time Face Detection: Captures faces in real-time using the camera.
  Face Registration and Training: Easily register new users and train the system for face recognition.
  Automated Attendance: Marks attendance once a face is recognized, storing it with the current date and time.
  View Attendance Records: Generate and export attendance records based on specific dates or users.
  Multiple Interfaces: User-friendly interfaces to manage different aspects of the system.

Interfaces
  Details: Displays detailed information about registered individuals, such as name, ID, and registration date.
  Train Data: Allows the system to train its recognition model using new face data. After capturing face images, the model is trained to recognize individuals.
  Attendance: Displays attendance records for all recognized individuals, along with timestamps.
  Face Recognition: The core feature that opens the camera feed, detects faces using the Haar Cascade Classifier, and recognizes them using the FaceNet model.
  Photos: Provides access to the dataset of registered face images, allowing you to view and manage stored photos.
  Exit: Closes the application and safely terminates the process.

Technologies Used
  Python: Programming language for the system.
  OpenCV: For image capture and face detection.
  Haar Cascade Classifier: For real-time face detection (haarcascade_frontalface_default.xml).
  FaceNet (Keras): Deep learning model used for face recognition by generating facial embeddings.
  SQLite/MySQL: Database for storing attendance records.
  Tkinter: Provides a graphical user interface for ease of use.

How It Works
  Face Detection: Uses Haar Cascade Classifier to detect faces from a live camera feed.
  Face Recognition: Detected faces are processed using FaceNet to generate embeddings that are compared with the registered faces.
  Attendance Marking: Once a match is found, attendance is marked in the database.
  Interface Navigation: Users can navigate through various interfaces like Details, Train Data, Attendance, and more for easy management of the system.
