# For find the pose of any person 
import cv2
from cvzone.PoseModule import PoseDetector
cap = cv2.VideoCapture(0)
detector = PoseDetector()
while True:
    Success, img = cap.read()
    img = detector.findPose(img)
    lmList, bboxInfo = detector.findPosition(img)
    
    cv2.imshow("Image",img)
    cv2.waitKey(1)



# import cv2
# from cvzone.PoseModule import PoseDetector
# cap = cv2.VideoCapture('Video.Mp4')
# detector = PoseDetector()
# posList = []
# while True:
#     Success, img = cap.read()
#     img = detector.findPose(img)
#     lmList, bboxInfo = detector.findPosition(img)

#     if bboxInfo:
#         lmString=''
#         for lm in lmList:
#             print(lm)
#             lmString += f'{lm[1]}, {img.shape[0]-lm[2]},{lm[3]},'
#         posList.append(lmString)
#     print(len(posList))
    
#     cv2.imshow("Image",img)
#     key=cv2.waitKey(1)
#     if key == ord('s'):
#         with open("AnimationFile.txt", 'w') as f:
#             f.writelines(["%s\n" % item for item in posList])