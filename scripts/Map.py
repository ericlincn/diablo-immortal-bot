from time import sleep
import pyautogui
import pydirectinput
from data.PosVars import Point, PosVars
from scripts.General import General
from utils.GeomUtil import GeomUtil

class Map:
    
    @staticmethod
    def getPatternBoxInMap(patternBitmap):
        
        return pyautogui.locateOnScreen(patternBitmap, grayscale=True, confidence=0.5)

    @staticmethod
    def getLegendaryBoxInMap():
        
        url = General.PREFIX + 'legendaryItemIconBig.png'
        return pyautogui.locateOnScreen(url, grayscale=True, confidence=0.8)
    
    @staticmethod
    def hasAreaMapTitle():
        
        btn = pyautogui.locateOnScreen(General.PREFIX + 'mapTitle.png', region=PosVars.getAreaMapTitle(), grayscale=True, confidence=0.8)
        return btn

    @staticmethod
    def hasMonsterWhite():
        
        btn = pyautogui.locateOnScreen(General.PREFIX + 'monster.png', region=PosVars.getMonsterWhiteTitle(), grayscale=True, confidence=0.8)
        return btn

    @staticmethod
    def hasMonsterBlue():
        
        btn = pyautogui.locateOnScreen(General.PREFIX + 'monsterBlue.png', region=PosVars.getMonsterBlueTitle(), grayscale=True, confidence=0.8)
        return btn

    @staticmethod
    def hasMonsterGold():
        
        btn = pyautogui.locateOnScreen(General.PREFIX + 'monsterGold.png', region=PosVars.getMonsterGoldTitle(), grayscale=True, confidence=0.8)
        return btn

    @staticmethod
    def hasMonsterPurple():
        
        btn = pyautogui.locateOnScreen(General.PREFIX + 'monsterPurple.png', region=PosVars.getMonsterPurpleTitle(), grayscale=True, confidence=0.8)
        return btn

    @staticmethod
    def hasMonsterOrange():
        
        btn = pyautogui.locateOnScreen(General.PREFIX + 'monsterOrange.png', region=PosVars.getMonsterOrangeTitle(), grayscale=True, confidence=0.8)
        return btn

    @staticmethod
    def hasMonster():
        
        btn = pyautogui.locateOnScreen(General.PREFIX + '60.png', region=PosVars.getMonsterTitle(), grayscale=True, confidence=0.8)
        return btn

    @staticmethod
    def hasMonsterOrangeOnMinimap():
        
        monster = pyautogui.locateOnScreen(General.PREFIX + 'monsterOrangeIcon.png', region=PosVars.getMinimap(), grayscale=False, confidence=0.95)
        return monster

    @staticmethod
    def hasLegendaryItemOnMinimap():
        
        item = pyautogui.locateOnScreen(General.PREFIX + 'legendaryItemIcon.png', region=PosVars.getMinimap(), grayscale=False, confidence=0.8)
        return item