import cv2
from util import get_limits
from PIL import Image
import webcolors as wb
import numpy as np


input_color = input("Enter color: ")
try:
    rgb_color = wb.name_to_rgb(input_color)
    bgr_color = tuple(np.array(rgb_color)[::-1])
except ValueError:
    print(f"Error: The color '{input_color}' is not recognized.")
    exit()
    
    
# bgr_color = [0, 255, 255]  # BGR Color


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_limit, upper_limit = get_limits(color=bgr_color)

    mask = cv2.inRange(hsv_image, lower_limit, upper_limit)

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox

        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # print(bbox)    # Prints the coordinates of the box

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
