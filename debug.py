from PIL import Image
import numpy as np
import face_recognition

img_pil = Image.open("known_faces/hitu.jpg").convert("RGB")
image = np.array(img_pil, dtype=np.uint8)
print("Shape:", image.shape)
print("Dtype:", image.dtype)

image = np.ascontiguousarray(image)
locs = face_recognition.face_locations(image)
print("Face locations:", locs)