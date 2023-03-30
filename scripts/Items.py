import pyautogui
import pydirectinput
from data.PosVars import PosVars

from scripts.General import General

class Items:

    HEAD = "Head"
    BODY = "Body"
    SHOULDER = "Shoulder"
    LGE = "Leg"
    HAMMER = "Hammer"
    SWORD = "Sword"
    SHIELD = "Shield"

    # @staticmethod
    # def hasLegendrayOnScreen(type):
        
    #     return pyautogui.locateOnScreen(General.PREFIX + 'item' + type + '.png', grayscale=False, confidence=0.9)

    @staticmethod
    def hasLegendrayOnScreen():
        
        arr = [Items.HEAD, Items.BODY, Items.SHOULDER, Items.LGE, Items.HAMMER, Items.SWORD, Items.SHIELD]
        out = []
        for i in range(0, len(arr)):
            url = General.PREFIX + 'item' + arr[i] + '.png'
            result = list(pyautogui.locateAllOnScreen(url, grayscale=False, confidence=0.8))
            # print(url, result)
            if len(result) > 0:
                out += result
        
        if len(out) > 0: return out

        return None
    
    @staticmethod
    def isFullbag():

        # red = pyautogui.locateOnScreen(General.PREFIX + 'fullbag.png', region=PosVars.getFullbagIndicator(), grayscale=False, confidence=0.99)
        # return red

        text = pyautogui.locateOnScreen(General.PREFIX + 'fullbagText.png', region=PosVars.getFullbagText(), grayscale=True, confidence=0.8)
        return text

    @staticmethod
    def hasLegendrayChipOnScreen():

        chip = pyautogui.locateOnScreen(General.PREFIX + 'itemChip.png', grayscale=True, confidence=0.5)
        return chip