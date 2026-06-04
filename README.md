# Face Detection and Recognition

An AI application that detects and recognizes faces in real-time using OpenCV and face_recognition library.

## Features
- Real-time face detection using webcam
- Face recognition with name display
- Support for multiple faces simultaneously
- Green box for known faces, Red box for unknown faces

## Technologies Used
- Python 3.11
- OpenCV
- face_recognition
- dlib
- NumPy
- Pillow

## Installation

### Clone the repository
```
git clone https://github.com/HitashaParashar/CODESOFT-FACE-DETECTION-AND-RECOGNITION.git
```

### Install dependencies
```
pip install -r requirements.txt
```

## How to Use

### Add known faces
- Add photos in `known_faces/` folder
- Name the file as the person's name (e.g. `hitu.png`)

### Run the project
```
python recognizer.py
```

### Controls
- Press `Q` to quit the application

## Project Structure
```
CODESOFT-FACE-DETECTION-AND-RECOGNITION/
├── known_faces/          # Store labeled photos here
├── recognizer.py         # Main recognition script
├── requirements.txt      # Dependencies
└── README.md             # Project documentation
```

## Internship
This project was built as part of CodSoft Internship Task.