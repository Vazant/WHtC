import cv2 as cv
import time


cap = cv.VideoCapture(0)

cv.VideoCapture.set(cap, cv.CAP_PROP_FRAME_WIDTH, 300)
cv.VideoCapture.set(cap, cv.CAP_PROP_FRAME_HEIGHT, 200)
def new_photo():
    ret, frame = cap.read()
    cap.release()
    #fn = 'img-%s.png' % time.strftime("%Y-%m-%d-%H-%M-%S")
    # fn = 'img-%s.jpg' % time.strftime("%Y-%m-%d-%H-%M-%S")
    fn = 'new_photo.jpg'
    cv.imwrite(fn, frame, [int(cv.IMWRITE_JPEG_QUALITY), 95])
    #cv.imwrite(fn, frame, [int(cv.IMWRITE_PNG_COMPRESSION), 9]) #чем больше значение тем больше сжатие и меньший размер
    #cap.release()

