import cv2

# Step 1: Load the image (THIS WAS MISSING)
image = cv2.imread("your_image.jpg")  # Replace with your actual image path

# Check if image loaded successfully
if image is None:
    print("Error: Could not load image. Check the file path.")
    exit()

# Step 2: Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Load Haar cascade and detect faces
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Step 4: Draw rectangles around detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Step 5: Show result
cv2.imshow("Detected Faces", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
