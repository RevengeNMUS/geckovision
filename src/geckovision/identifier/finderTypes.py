from enum import Enum
import cv2 as cv
import os

_this_path = os.path.dirname(os.path.abspath(__file__))
_cascadeees_path = os.path.join(_this_path, "cascaaaaaades")

class schmorgusborgus(Enum):
    FACES = cv.CascadeClassifier(os.path.join(_cascadeees_path, "dafaceyboidetector.xml"))
    EYES = cv.CascadeClassifier(os.path.join(_cascadeees_path, "dalookeyboidetector.xml"))