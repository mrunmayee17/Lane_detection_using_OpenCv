import cv2
def cannyimage(lane_img):

    # Converting a image to gray scale - contains 1 channel 1 intensity value ranging from 0 - 255 ? -> normal image has 3 channels and processing in 1 channel is better than processing in three channel , 3 channels has combiantions of 3 intensity value.

    gray_img = cv2.cvtColor(lane_img, cv2.COLOR_RGB2GRAY)

    # Inorder to capture maximum edges, we need to remove noise from the image 
    # Gaussian Filter -> averages out the value from the surrounding pixels which is done using kernal -> [[1 2 1][2 4 2][1 2 1]] this kernal is the placed on each pixel find average values - smoothening them
    blur_img = cv2.GaussianBlur(gray_img,(5,5),0)

    # Canny Edge Detection
    # It calculates the derivative of each pixel with its neighbouring pixel- computing gradient in all directions 
    # gradient is compared with upper threshold if > then considered as edge 
    # -> 1:2 or 1:3 ratio -> lower threshold and upper threshold 
    # small changes in brightness are not traced hence, they are black as they fall below lower threshhold

    canny_img = cv2.Canny(blur_img,50,150)
    return canny_img