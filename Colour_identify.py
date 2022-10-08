from statistics import mode
import cv2 as cv
import numpy as np

drawing = False
ix,iy = -1,-1

img = cv.imread('parrot.jpg')
img1 = cv.resize(img,(1080, 860))
img2 = cv.cvtColor(img1, cv.COLOR_BGR2HSV)


def Mouse_click(event,x,y,flags,param):
    
    global ix,iy,drawing,mode

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            cv.rectangle(img1, (ix,iy),(x,y),(255,255,255,),1)

    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        print(ix,iy,x,y)
        colour_identify(ix,iy,x,y)
        

def colour_identify(ix,iy,x,y):
    img_crop = img1[iy:y,ix:x]
    # cv.imshow("img",img_crop)
    
    height, width, _ = img_crop.shape
    

    ch = int(height/2)
    cw = int(width/2)
    print(ch,cw)

    pix_center = img2[ch,cw]
    b,g,r   = img2[ch,cw]
    A = img2[ch,cw]
    print("A",A)

    print("b,g,r",b,g,r)
    hue_value = pix_center[0]
    print("hue",hue_value)







    color = "Undefined"
    if hue_value < 5:
        color = "RED"
    elif hue_value < 22:
        color = "ORANGE"
    elif hue_value < 33:
        color = "YELLOW"
    elif hue_value < 78:
        color = "GREEN"
    elif hue_value < 131:
        color = "BLUE"
    elif hue_value < 170:
        color = "VIOLET"
    else:
        color = "RED"



    pixel_center_bgr = img1[ch, cw]
    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])
    
    print("color",color)

    
    





    


cv.namedWindow('image')
cv.setMouseCallback('image', Mouse_click)




while(1):
    cv.imshow('image',img1)
    if cv.waitKey(20) & 0xFF == 27:
        break

cv.destroyAllWindows()

