import cv2 as cv


def Camera():
    cam = cv.VideoCapture('test_video.mp4')
    # cam = cv.VideoCapture(0)
    fps = cam.get(cv.CAP_PROP_FPS)
    print("fps for this video",fps)

    while cam.isOpened():
        ret, frame = cam.read()
        print(ret)
        if not ret:
            print("no frame received")
            break
        cv.imshow("image",frame)
        
        if cv.waitKey(25) == ord('q'):
            break
    cam.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    Camera()