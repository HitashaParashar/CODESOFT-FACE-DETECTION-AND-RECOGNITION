import cv2
import face_recognition
import os
import numpy as np
from PIL import Image
import warnings
import logging
warnings.filterwarnings("ignore")
os.environ["OPENCV_LOG_LEVEL"] = "OFF"
logging.disable(logging.CRITICAL)

known_encodings = []
known_names = []

known_faces_dir = "known_faces"
for filename in os.listdir(known_faces_dir):
    if filename.lower().endswith((".jpg", ".png", ".jpeg")):
        img_pil = Image.open(f"{known_faces_dir}/{filename}").convert("RGB")
        image = np.ascontiguousarray(np.array(img_pil, dtype=np.uint8))
        face_locs = face_recognition.face_locations(image)
        encodings = face_recognition.face_encodings(image, face_locs)
        if len(encodings) > 0:
            known_encodings.append(encodings[0])
            name = os.path.splitext(filename)[0]
            known_names.append(name)
            print(f"✅ Loaded: {name}")
        else:
            print(f"❌ No face found in: {filename}")

print(f"\n✅ Total known faces: {len(known_encodings)}")
print("📷 Camera starting... Q press karo band karne ke liye\n")

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    small_frame = cv2.resize(rgb_frame, (0, 0), fx=0.5, fy=0.5)

    face_locations = face_recognition.face_locations(small_frame)
    face_encodings = face_recognition.face_encodings(small_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        distances = face_recognition.face_distance(known_encodings, face_encoding)
        name = "Unknown"

        if len(distances) > 0:
            best_index = np.argmin(distances)
            if distances[best_index] < 0.5:
                name = known_names[best_index]

        top *= 2; right *= 2; bottom *= 2; left *= 2

        color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)
        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
        cv2.putText(frame, name.upper(), (left, top - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

    cv2.imshow("Face Recognition - Press Q to quit", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("👋 Program band ho gaya!")
