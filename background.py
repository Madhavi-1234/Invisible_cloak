import cv2

#creating a video capture object
cap = cv2.VideoCapture(0) 

#Getting the background image
while cap.isOpened():
    ret, background = cap.read()
    if ret:
        cv2.imshow("image", background)
        if cv2.waitKey(5) == ord('q'):

        
        #save the background image
            cv2.imwrite("image.jpg", background)
            break
cap.release()
cv2.destroyAllWindows()