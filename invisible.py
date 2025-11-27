import cv2 
import numpy as np

cap = cv2.VideoCapture(0)
background = cv2.imread('./image.jpg')

while cap.isOpened():
    #capture the live frame
    ret, current_frame = cap.read()
    if ret:
     #convering from rgb to hsv color space
        hsv_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2HSV)

        #Range for lower red
        lower_red = np.array([0, 120, 70])
        upper_red = np.array([10, 255, 255])  
        mask1 =  cv2.inRange(hsv_frame, lower_red, upper_red)

        #Range for upper red
        lower_red = np.array([170, 120, 70])
        upper_red = np.array([180, 255, 255])
        mask2 = cv2.inRange(hsv_frame, lower_red, upper_red)

        #generating the final red mask
        red_mask = mask1 + mask2

        red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=10)
        red_mask = cv2.morphologyEx(red_mask, np.ones((3, 3), np.uint8), iterations=1)

        #substituting the red portion with backgrounf image
        part1 = cv2.bitwise_and(background, background, mask=red_mask)

        #detecting the non red part
        red_free = cv2.bitwise_not(red_mask)

        #if claok is not present, show the current image
        part2 = cv2.bitwise_and(current_frame, current_frame, mask=red_free)

        #final output
        cv2.imshow("cloak", part1 + part2)

        cv2.imshow("red cloak", part1)
        if cv2.waitKey(5) == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
