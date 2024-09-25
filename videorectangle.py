import cv2
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap=cv2.VideoCapture(0)
while True:
    _, img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#only gray color can be processed in cascade fun 
    faces=face_cascade.detectMultiScale(gray,1.1,4)
    #c=label.count("person")#label is not defined.
    count=0
    #print(count)
    for(x,y,w,h) in faces:
        rectangle=cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)#5 parameters (x,y) defines start point,,2 defines thickness
        cv2.putText(img,str(count+1),(x,y),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,2,(255,0,255),3) #3 - size of the font and 3 - thickness of the font
        count+=1
        

    cv2.imshow("VIDEO",img)
    key=cv2.waitKey(1)
    if key==ord("q") or key==ord("Q"):
        break
print("total people count is {}".format(count))
cap.release()
cv2.destroyAllWindows()

#(255,0,0)-Blue color box
#(0,255,0)-Green color box
#(0,0,255)-Red color box