import cv2
import numpy as np
import time

capture_video = cv2.VideoCapture(0)

time.sleep(1)
count = 0
background = 0

# This part captures 60 frames of the background(without you in the frame), to store the static background
for i in range(60):
    return_val, background = capture_video.read()
    if return_val == False:
        continue

# background is the actual image frame (Numpy 3D array: Height, Width, 3 for RGB)
background = np.flip(background, axis=1)

while capture_video.isOpened():
    return_val, img = capture_video.read()
    if not return_val:
        break
    count = count + 1 
    img = np.flip(img, axis=1)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# setting the lower and upper range for mask1
    lower_red = np.array([0, 100, 40])
    upper_red = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)

# setting the lower and upper range for mask2
    lower_red = np.array([160, 100, 40])
    upper_red = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red, upper_red)

    mask1 = mask1 + mask2

    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)  #MORPH_OPEN = erosion+ dilation
    mask1 = cv2.dilate(mask1, np.ones((3, 3), np.uint8), iterations=1)
    mask2 = cv2.bitwise_not(mask1)

    res1 = cv2.bitwise_and(background, background, mask=mask1)
    res2 = cv2.bitwise_and(img, img, mask=mask2)

    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)

    cv2.imshow("Invisible T-shirt", final_output)

    k = cv2.waitKey(10)

    if k == 27:
        break



    

