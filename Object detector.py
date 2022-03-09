import numpy as n
import cv2 as c

#vid = c.VideoCapture("r11.mkv")
img = c.imread("NAME OF YOUR IMAGE WITH PATH IF IT IS IN A DIFFERENT FOLDER")
_, fframe = vid.read()
x = #LOWER BASE HEIGHT OF THE OBJECT IN THE IMAGE
y = #LOWER VERTICAL HEIGHT OF THE OBJECT IN THE IMAGE
h = #UPPER BASE HEIGHT OF THE OBJECT IN THE IMAGE - y
w = #UPPER VERTICAL HEIGHT OF THE OBJECT IN THE IMAGE - x
# roi = fframe[y:h+y, x: w+x]
roi = img[317: 420, 310: 400]
hsvr = c.cvtColor(roi, c.COLOR_BGR2HSV)
mask = c.inRange(hsvr, n.array((0., 60., 32.)), n.array((180., 255., 255)))
rh = c.calcHist([hsvr], [0], mask, [180], [0, 180])
rh = c.normalize(rh, rh, 0, 255, c.NORM_MINMAX)
tc = (c.TERM_CRITERIA_EPS | c.TERM_CRITERIA_COUNT, 10, 1)
cap = c.VideoCapture(0) #It captues the live video from the webcamera
while True:
    _, frame = cap.read()
    hsv = c.cvtColor(frame, c.COLOR_BGR2HSV)
    dst = c.calcBackProject([hsv], [0], rh, [0, 180], 1)
    ret, tw = c.CamShift(dst, (x, y, w, h), tc)
    p = c.boxPoints(ret)
    p = n.int0(p)
    c.polylines(frame, [p], True, (255, 0, 0), 2)
    c.imshow("First frame", dst)
    c.imshow("Frame", )
    k = c.waitKey(60)
    if k == 27:
        break
vid.release()
c.destroyAllWindows()
