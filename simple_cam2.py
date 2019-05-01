import cv2
from time import sleep

camera = cv2.VideoCapture(0)

cv2.namedWindow("test")
ret, frame = camera.read()
cv2.imshow("test", frame)
for i in range(10):
    return_value, image = camera.read()
    cv2.imwrite('opencv'+str(i)+'.png', image)
    sleep(5)
del(camera)
