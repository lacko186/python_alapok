import cv2
from PIL import ImageGrab
from datetime import datetime
import os

if not os.path.exists('kepek'):
    os.makedirs('kepek')

timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

screenshot = ImageGrab.grab()
screenshot.save(f'kepek/kepernyofoto_{timestamp}.png')

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
if ret:
    cv2.imwrite(f'kepek/kamerakep_{timestamp}.png', frame)

prev_frame = None
motion_threshold = 5000
cooldown = 30
frame_counter = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    
    if prev_frame is None:
        prev_frame = gray
        continue
    
    frame_delta = cv2.absdiff(prev_frame, gray)
    thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2) # type: ignore
    motion_pixels = cv2.countNonZero(thresh)
    
    if motion_pixels > motion_threshold and frame_counter >= cooldown:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        cv2.imwrite(f'kepek/mozgas_{timestamp}.png', frame)
        print(f"Mozgás! mozgas_{timestamp}.png")
        frame_counter = 0
    
    prev_frame = gray
    frame_counter += 1
    
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cap.release()
cv2.destroyAllWindows()