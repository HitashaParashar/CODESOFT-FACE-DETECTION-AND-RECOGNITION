import cv2

cap = cv2.VideoCapture(0)

print("SPACE press karo photo lene ke liye...")
print("Q press karo band karne ke liye...")

while True:
    ret, frame = cap.read()
    cv2.imshow("Apni Photo Lo", frame)
    
    key = cv2.waitKey(1)
    
    # Space press karo photo lene ke liye
    if key == ord(' '):
        cv2.imwrite("known_faces/hitu.jpg", frame)
        print("Photo save ho gayi! known_faces/hitu.jpg")
        break
    
    # Q press karo exit karne ke liye    
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()