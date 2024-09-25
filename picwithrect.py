import cv2 as c
face_cascade=c.CascadeClassifier('haarcascade_frontalface_default.xml')
img="photo1.jpg"
imd=c.imread(img)
gray=c.cvtColor(imd,c.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray,1.1,4)
for(x,y,w,h) in faces:
    c.rectangle(imd,(x,y),(x+w,y+h),(225,0,0),2)
while True:
    c.imshow("IMG",imd)
    key=c.waitKey(1)
    if key==ord("q") or key==ord("Q"):
            break

