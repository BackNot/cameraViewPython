import cv2
import sys

try:
    camera_index = sys.argv[1]
except IndexError:
    camera_index = 0

cv2.namedWindow("preview")
vc = cv2.VideoCapture(int(camera_index))

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
cv2.destroyWindow("preview")