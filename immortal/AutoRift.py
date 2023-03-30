import pydirectinput
import pyautogui
import cv2 as cv
import sys

from ScreenWatcher import ScreenWatcher
from cn.daftlib.command.Executer import Executer
from data.PosVars import PosVars

class AutoRift:

    def __init__(self, watcher:ScreenWatcher, executer:Executer) -> None:
        
        pyautogui.screenshot("minimap.png", region=PosVars.getMinimap())

        img = cv.imread("minimap.png", 0)
        ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
        th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,\
            cv.THRESH_BINARY,11,2)
        th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
                    cv.THRESH_BINARY,11,2)

        cv.imshow("Display window", th3)
        k = cv.waitKey(0)