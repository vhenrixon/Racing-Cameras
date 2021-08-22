import cv2 as cv

capture = cv.VideoCapture(0)
capture2 = cv.VideoCapture(1)

while True:
    isTrue,frame = capture.read()
    isTrueTwo, frametwo = capture2.read()
    cv.imshow('g', frametwo)
    cv.imshow('Video',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
capture2.release()
cv.destroyAllWindows()