from PIL import Image
import numpy as np
import face_recognition

# Hitu photo
img1 = Image.open("known_faces/hitu.png").convert("RGB")
arr1 = np.ascontiguousarray(np.array(img1, dtype=np.uint8))
locs1 = face_recognition.face_locations(arr1)
enc1 = face_recognition.face_encodings(arr1, locs1)

# Prachi photo
img2 = Image.open("known_faces/prachi.png").convert("RGB")
arr2 = np.ascontiguousarray(np.array(img2, dtype=np.uint8))
locs2 = face_recognition.face_locations(arr2)
enc2 = face_recognition.face_encodings(arr2, locs2)

if enc1 and enc2:
    distance = face_recognition.face_distance([enc1[0]], enc2[0])
    print(f"Distance between hitu and prachi: {distance}")
    if distance < 0.6:
        print("Same person match ho raha hai!")
    else:
        print("Alag log hain - recognition sahi kaam karega!")
else:
    print("Face detect nahi hua")