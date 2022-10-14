from time import time
import cv2 as cv
import time

# cam = cv.VideoCapture(0)
no_frames = 120
# start = time.time()
# for i in range (0, no_frames):
#     ret, frame = cam.read()
# end = time.time()

# seconds = end - start
# fps = no_frames/seconds

# fps_1 = ("fps:{0}".format(fps))
# print(fps)

def Camera():
    cam = cv.VideoCapture(0)
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    out = cv.VideoWriter('output3.avi', fourcc, 30.0, (640,480))
    while cam.isOpened():
        ret, frame = cam.read()
        if not ret:
            print("video is not recived")
            break

        start = time.time()
        for i in range (0, no_frames):
            ret, frame = cam.read()
        end = time.time()

        seconds = end - start
        fps = no_frames/seconds
        fps_1 = ("fps:{0}".format(fps))
        frame1 = cv.putText(frame,fps_1,(20,20),cv.FONT_HERSHEY_DUPLEX,1,(0,0,0),1)
        out.write(frame)
        cv.imshow("image",frame1)

        if cv.waitKey(30) == ord('q'):
            break

    
    cam.release()
    out.release()
    cv.destroyAllWindows()


    
   

if __name__ == '__main__':
    Camera()