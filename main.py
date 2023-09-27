import os
import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# importing the mode images into a list
imgBackground = cv2.imread('resources/background.png')
folderModePath = 'resources/Modes'
modePathList = os.listdir(folderModePath)
imageModeList = []
for path in modePathList:
    imageModeList.append(cv2.imread(os.path.join(folderModePath, path)))

print(len(imageModeList))

while True:
    success, img = cap.read()

    imgBackground[162:162 + 480, 55:55 + 640] = img
    imgBackground[44:44 + 633, 808:808 + 414] = imageModeList[1]

    cv2.imshow("Face attention", imgBackground)
    cv2.waitKey(1)
