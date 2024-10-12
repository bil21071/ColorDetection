#Hi folks this is my color detection project which
#will detect the yellow object without any trained models
#we will have to use Opencv ,Pillow and numpy and utils.py created for this
#to convert from bgr to hsv format hue saturation and value easy for humans to understand

#done course till 2:12:52 

#we will detect the colour yellow 
import cv2 
from PIL import Image
from utils import get_limits
yellow=[0,255,255] #yellow color in bgr format
cap= cv2.VideoCapture(0)
while True:
    ret, frame=cap.read()   #it will read the frames
    HSVImage=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lowerLimit,upperLimits =get_limits(color=yellow)
    mask=cv2.inRange(HSVImage,lowerLimit,upperLimits)
    mask_=Image.fromarray(mask)
    bbox=mask_.getbbox()
    if bbox is not None:
        x1, y1, x2, y2=bbox

        frame=cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0),5)
    cv2.imshow('frame',frame)
    #The color cycle have 3 values one is the saturation and the other is hue and shape
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()

cv2.destroyAllWindows()

# The cv2. inRange function checks each pixel in the HSV image to see if its H, S, and V values all fall within the specified lower and upper ranges. For each pixel that meets this criterion, the corresponding pixel in the output mask is set to 255 (white). Otherwise, it is set to 0 (black
# Formerly known as PIL, Pillow is an open source library specifically designed for image processing via Python. A veritable goldmine for image file manipulation, let's take a look at some of the basic features of this benchmark library.