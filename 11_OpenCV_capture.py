import cv2, time

# video = cv2.VideoCapture("movie.mp4") #capture from movie
video = cv2.VideoCapture(0) #capture from camera

while True:
    check, frame = video.read()

    cv2.imshow("Capturing", frame)

    key = cv2.waitKey(2)

    if key == ord('q'):
        break





video.release() #to close the already opened files or camera