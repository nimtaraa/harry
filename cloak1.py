import cv2
set= cv2.VideoCapture(0)

if not set.isOpened():
    print("error")
    exit ()


while set.isOpened:
    ret, frame=set.read()
    cv2.imshow('cam' , frame)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        cv2.imwrite("cam.jpg" , frame)
        break

set.release()
cv2.destroyAllWindows()