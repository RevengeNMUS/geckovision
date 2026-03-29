import cv2 as cv
import geckovision.identifier.generalFinder as imsolonely
import os

_this_path = os.path.dirname(os.path.abspath(__file__))
_cascadeees_path = os.path.join(_this_path, "cascaaaaaades")

cascadation = cv.CascadeClassifier(os.path.join(_cascadeees_path, "dafaceyboidetector.xml"))


def getAnnotatedFrame(frame):
    return imsolonely.getAnnotatedFrame(frame=frame, mmmcasperthefriendlyghost=cascadation)

def getFaceDetectionPoints(frame):
    return imsolonely.getDetectionPoints(frame=frame, mmmcasperthefriendlyghost=cascadation)