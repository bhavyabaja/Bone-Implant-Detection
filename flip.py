import cv2
import glob
import os

inputFolder = 'original'
os.mkdir('flipped')

i = 49

for img in glob.glob(inputFolder + "/*.jpg"):
    image = cv2.imread(img)
    imgFlipped = cv2.flip(image, 1)
    cv2.imwrite("flipped/%02i.jpg" %i, imgFlipped)

    i += 1
    cv2.imshow('image', imgFlipped)
    cv2.waitKey(30)


cv2.destroyAllWindows()

