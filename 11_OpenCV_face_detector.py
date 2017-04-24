import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("photo.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.05, minNeighbors = 5)

#first_column, first_row, width, height
print (faces)
print (type(faces))

for x, y, width, height in faces:
    #draw a green rectangle around the face, 3 pixels width
    img_face = cv2.rectangle(img, (x, y), (x + width, y + height), (0, 255, 0), 3)
    print (x, y, width, height)

cv2.imwrite("Face_detector.jpg", img_face)