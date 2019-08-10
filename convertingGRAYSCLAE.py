import argparse 
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
   help="here is the input")
args= vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("image", image)
cv2.waitKey(1)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("GRAY", gray)
cv2.waitKey(1) 

Edged = cv2.Canny(gray, 30, 150)
cv2.imshow("Edged", Edged)
cv2.waitKey(1)
thresh= cv2.threshold(gray, 255, 255, cv2.THRESH_BINARY_INV)[1]
cv2.imshow("Thresh", thresh)
cv2.waitKey(1)


cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
     cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
output = image.copy()
for c in cnts:
     cv2.drawContours(output, [c], -1, (240, 0, 159), 3)
     cv2.imshow("Contours", output)
     cv2.waitKey(1)
text = "mjhe itte objects mile {}".format(len(cnts))
cv2.putText(output , text, (150, 250), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
    (240, 0, 159), 2)
cv2.imshow("Contours", output)
cv2.waitKey(1)

mask = gray.copy()
mask = cv2.erode(mask, None, iterations=5)
cv2.imshow("ERODED", mask)
cv2.waitKey(1)

mask = gray.copy()
mask = cv2.dilate(mask, None, iterations=5)
cv2.imshow("DILATED", mask)
cv2.waitKey(0)

mask = thresh.copy()
output = cv2.bitwise_and(image , image , mask = mask)
cv2.imshow("Bitwaise ", output)
cv2.waitKey(0)