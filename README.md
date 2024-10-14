# Face Recognition Attendance System

This project is a **Facial Recognition Attendance System** built using Python. It uses real-time facial recognition to automate the process of marking attendance. The system features several user-friendly interfaces to manage data, train the system, and record attendance.

## Features

- **Real-time Face Detection and Recognition**
- **Automated Attendance Marking**
- **Multiple Interfaces for Ease of Use**
- **Attendance Reports and Data Management**

## Interfaces

1. **Details**: Displays information about registered users (e.g., Name, ID, Registration Date).
2. **Train Data**: Facilitates the registration of new users and trains the system for recognition.
3. **Attendance**: Allows the viewing and export of attendance records with timestamps.
4. **Face Recognition**: Uses the camera to detect and recognize faces in real-time.
5. **Photos**: View and manage stored face images in the system.
6. **Exit**: Safely terminates the application.

## Technologies Used

- **Python**: Core language for developing the system.
- **OpenCV**: For camera integration and face detection using Haar Cascade Classifier.
- **Haar Cascade**: (`haarcascade_frontalface_default.xml`) used for face detection.
- **FaceNet (Keras)**: Deep learning model used for facial recognition.
- **Keras and TensorFlow**: Libraries to support FaceNet for facial embeddings and matching.
- **SQLite/MySQL**: Database system for storing attendance records.
- **Tkinter**: Graphical user interface to interact with the system.

## Project Structure
  /project_root │ ├── /dataset # Registered face images ├── /src # Source code │ ├── attendance.py # Main attendance system logic │ ├── train_data.py # Handles training of new faces │ ├── face_recognition.py # Facial recognition logic │ ├── database.py # Database operations │ └── gui.py # Tkinter-based interface ├── /img # System images and icons └── README.md # Project documentation


## Installation

### Prerequisites

- **Python 3.x** installed on your system.
- Install required libraries:
  ```bash
  pip install opencv-python
  pip install dlib
  pip install keras
  pip install tensorflow
  pip install numpy
