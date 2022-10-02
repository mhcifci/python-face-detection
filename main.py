import numpy as np
import cv2

# Set variable "cv2.VideoCapture(0)" as a function
vid = cv2.VideoCapture(0)

# @https://github.com/opencv/opencv/tree/master/data/haarcascades
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
  
# Run script every True returns
while(True):

    # cv2.VideoCapture(0).read
    ret, frame = vid.read()

    # Turn colors to Gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces via haarcascade_frontalface_default.xml
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Loop every face X Y W H
    for (x , y , w , h ) in faces:
        cv2.rectangle(frame, (x,y), (x + w, y + h), (85, 255 , 0), 2)


    # Show window & Camera
    cv2.imshow('frame', frame)

    # waitKey and stop While loop close window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# Close window
vid.release()
# Close window
cv2.destroyAllWindows()