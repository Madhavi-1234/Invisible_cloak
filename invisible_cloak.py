import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Load background image
background = cv2.imread("image.jpg")

if background is None:
    print("ERROR: 'image.jpg' not found. Run save_bg.py first!")
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Red color ranges
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])

    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])

    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

    red_mask = mask1 + mask2

    # Clean mask
    kernel = np.ones((3, 3), np.uint8)
    red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_OPEN, kernel, iterations=2)
    red_mask = cv2.dilate(red_mask, kernel, iterations=1)

    # Invert mask
    mask_inv = cv2.bitwise_not(red_mask)

    part1 = cv2.bitwise_and(background, background, mask=red_mask)
    part2 = cv2.bitwise_and(frame, frame, mask=mask_inv)

    final = part1 + part2

    cv2.imshow("Invisible Cloak", final)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
