import imp


import numpy as np

def makeCoordinates(image,lineparam):
    slope, intercept = lineparam
    # height -> y1
    y1 = image.shape[0]
    y2 = int(y1 * (3/5))
    # y = slope * x + intercept
    x1 = int((y1 -intercept)/slope)
    x2 = int((y2 -intercept)/slope)

    return np.array([x1, y1, x2, y2])