import cv2
import numpy as np
import matplotlib.pyplot as plt

from utility.edge_detection import cannyimage
from utility.region_of_interest import region_of_interest
from utility.make_coordinates import makeCoordinates

image = cv2.imread('test_image.jpg')
lane_img = image

# edge detection -> sharp change in intensity level from 0 to 255, rapid change in brightness
# changes in brightness is gradient

def display_line_image(image,lines):
    line_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            line_image = cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),10)
    return line_image


def optimizedLines(image, lines):
    left_fit = []
    right_fit = []
    # find slope and y intercept form every line in hough space
    
    for line in lines:
        x1, y1, x2, y2 = line.reshape(4)
        slope, intercept = np.polyfit((x1, x2), (y1,y2), 1)
        if slope < 0:
            left_fit.append((slope,intercept))
        else:
            right_fit.append((slope,intercept))
    left_fit_avg = np.average(left_fit, axis = 0)
    right_fit_avg = np.average(right_fit, axis = 0)
    left_line_optmize = makeCoordinates(image, left_fit_avg)
    right_line_optimize = makeCoordinates(image, right_fit_avg)

    # print(left_fit_avg)
    # print(right_fit_avg)
    return np.array([left_line_optmize,right_line_optimize])



# canny_img = cannyimage(lane_img)
# cropped_img = region_of_interest(canny_img)
# lines = cv2.HoughLinesP(cropped_img,2,np.pi/180,100,minLineLength=40, maxLineGap=5)
# optimized_lines = optimizedLines(lane_img,lines)
# Hough_line_image = display_line_image(lane_img,optimized_lines)


# detectedlineImage = cv2.addWeighted(lane_img,0.8,Hough_line_image,1, 1)


# plt.imshow(cannyimage(lane_img))
# # cv2.waitKey(0)
# plt.show()

# For a video:
cap = cv2.VideoCapture("test2.mp4")
while (cap.isOpened()):
    boolval, frame = cap.read()

    canny_img = cannyimage(frame)
    cropped_img = region_of_interest(canny_img)

    lines = cv2.HoughLinesP(cropped_img,2,np.pi/180,100,minLineLength=40, maxLineGap=5)
    optimized_lines = optimizedLines(frame,lines)
    Hough_line_image = display_line_image(frame,optimized_lines)

    detectedlineImage = cv2.addWeighted(frame,0.8,Hough_line_image,1, 1)

    cv2.imshow("result",detectedlineImage)
    if cv2.waitKey(1) == ord('q'):
    # if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
