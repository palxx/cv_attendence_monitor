import os

import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

imgBackground = cv2.imread('resources/background.png')
folderModePath = 'resources/Modes'
modePathList = os.listdir(folderModePath)
imageModeList = []
for path in modePathList:
    imageModeList.append(cv2.imread(os.path.join(folderModePath, path)))

while True:
    success, img = cap.read()

    imgBackground[162:162 + 480, 55:55+ 640] = img
    cv2.imshow("Face attention", img)
    cv2.waitKey(1)
