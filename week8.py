import cv2
import numpy as np
# Start video capture, '0' is the default webcam
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(frame_hsv)
    s = cv2.multiply(s, 0.2)
    hsv_merged = cv2.merge([h,s,v])
    hsv_merged = np.clip(hsv_merged, 0, 255).astype('uint8')
    frame_bgr= cv2.cvtColor(hsv_merged, cv2.COLOR_HSV2BGR)
    cv2.imshow('Edge map', frame_bgr)

        # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()