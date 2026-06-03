import face_recognition
import os
import pickle

KNOWN_FACES_DIR = "known_faces"
ENCODINGS_FILE = "encodings.pkl"

known_encodings = []
known_names = []

print("[INFO] Processing known faces...")

for filename in os.listdir(KNOWN_FACES_DIR):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        name = os.path.splitext(filename)[0]  # filename = person's name
        filepath = os.path.join(KNOWN_FACES_DIR, filename)
        
        image = face_recognition.load_image_file(filepath)
        encodings = face_recognition.face_encodings(image)
        
        if encodings:
            known_encodings.append(encodings[0])
            known_names.append(name)
            print(f"  ✅ Encoded: {name}")
        else:
            print(f"  ⚠️  No face found in: {filename}")

# Save encodings to file
data = {"encodings": known_encodings, "names": known_names}
with open(ENCODINGS_FILE, "wb") as f:
    pickle.dump(data, f)

print(f"\n[INFO] Saved {len(known_names)} encodings to {ENCODINGS_FILE}")