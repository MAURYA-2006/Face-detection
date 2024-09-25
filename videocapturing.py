import cv2 as c
vc=c.VideoCapture(0)#pass video name here like (vid.mp4)....0 represents lap camera

while True:#to run the video continuously
    ret, frame=vc.read()
    c.imshow("video",frame)

    key=c.waitKey(1)#to quit the window
    if key==ord("q"):
        break

vc.release()#release the video capture object
c.destroyAllWindows()#clear all running windows
