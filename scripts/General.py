import pyautogui
import pydirectinput
from data.PosVars import PosVars, Size
from utils.ColorUtil import ColorUtil
from utils.GeomUtil import GeomUtil

import cv2 as cv
import numpy as np

class General:

    GAME_TITLE = "Diablo Immortal"
    PREFIX = "__images/"

    # @staticmethod
    # def resizeWindow(window):

    #     rect = PositionVars.getWindowRect()
    #     window.resizeTo(rect.width, rect.height)
    #     window.moveTo(rect.x, rect.y)

    @staticmethod
    def resizePositionWindow():

        if pyautogui.getWindowsWithTitle(General.GAME_TITLE):
            window = pyautogui.getWindowsWithTitle(General.GAME_TITLE)[0]
            
            if window.isActive:
                bar = pyautogui.locateOnScreen(General.PREFIX + 'healthBar.png', grayscale=True, confidence=0.95)
                
                if bar:
                    barMarginLeft = 3
                    barMarginTop = 120
                    diffX = barMarginLeft - bar.left
                    diffY = barMarginTop - bar.top
                    window.move(int(diffX), int(diffY))
                    PosVars.ZERO_X = 0
                    PosVars.ZERO_Y = 0
                    print(diffX, diffY, bar, PosVars.ZERO_X, PosVars.ZERO_Y)

    @staticmethod
    def getCurrentHealth():

        shot = pyautogui.screenshot(None, PosVars.getHealthBar())
        w = shot.width

        # mat = cv.cvtColor(np.array(shot),cv.COLOR_RGB2BGR)
        # mat = cv.imread(cv.samples.findFile("s2.png"))
        # cv.imshow("shot", mat)

        img = cv.cvtColor(np.array(shot), cv.COLOR_RGB2HSV_FULL)
        # print(img[0, 160, 2])
        
        i=0
        arr = [0, 0]
        while i < w:

            # p = shot.getpixel((i, 0))[0]
            # if p > 93:
            #     arr[0] += 1
            # else:
            #     arr[1] += 1

            v = img[0, i, 2]
            if v >= 84: arr[0] += 1
            else: arr[1] += 1
            
            i += 10

        return arr[0] / (arr[0] + arr[1])

    @staticmethod
    def hasHealthBar():
        
        left = pyautogui.locateOnScreen(General.PREFIX + 'healthBarLeft.png', region=PosVars.getHealthBarLeftCorner(), grayscale=True, confidence=0.8)
        right = pyautogui.locateOnScreen(General.PREFIX + 'healthBarRight.png', region=PosVars.getHealthBarRightCorner(), grayscale=True, confidence=0.8)
        return left and right

    @staticmethod
    def hasInviteButton():
        
        btn = pyautogui.locateOnScreen(General.PREFIX + 'inviteButton.png', region=PosVars.getInviteButton(), grayscale=True, confidence=0.8)
        return btn

    @staticmethod
    def hasPassportButton():
        
        btn = pyautogui.locateOnScreen(General.PREFIX + 'passport.png', region=PosVars.getPassportButton(), grayscale=True, confidence=0.8)
        return btn

    @staticmethod
    def getPointAroundPlayer(angle, radius):

        # size = pyautogui.size()
        # return GeomUtil.getPositionOnCircle(size.width*.5, size.height*.5, angle, 200, 200)
        
        p = PosVars.getCenter()
        return GeomUtil.getPositionOnCircle(p.x, p.y, angle, radius, radius)

    # 不朽回音
    @staticmethod
    def hasReadyButton():
        
        btn = pyautogui.locateOnScreen(General.PREFIX + 'readyButton.png', region=PosVars.getReadyButton(), grayscale=True, confidence=0.8)
        return btn

    # 不朽回音
    @staticmethod
    def hasRewardText():
        
        btn = pyautogui.locateOnScreen(General.PREFIX + 'rewardText.png', region=PosVars.getRewardText(), grayscale=True, confidence=0.5)
        return btn

    # 不朽回音
    @staticmethod
    def hasResultCloseButton():
        
        btn = pyautogui.locateOnScreen(General.PREFIX + 'resultCloseButton.png', region=PosVars.getResultCloseButton(), grayscale=True, confidence=0.8)
        return btn

    # 不朽回音
    @staticmethod
    def hasBattlegroundCaptainOnScreen():

        cap = pyautogui.locateOnScreen(General.PREFIX + 'captainText.png', grayscale=True, confidence=0.5)
        return cap

    @staticmethod
    def hasReviveTownButton():

        btn = pyautogui.locateOnScreen(General.PREFIX + 'reviveButton.png', region=PosVars.getReviveTownButtonCorner(), grayscale=True, confidence=0.8)
        return btn

    @staticmethod
    def hasConversation():

        corner = pyautogui.locateOnScreen(General.PREFIX + 'conversationCorner.png', region=PosVars.getConversationCorner(), grayscale=True, confidence=0.8)
        return corner
    
    @staticmethod
    def hasEnterButton():

        btn = pyautogui.locateOnScreen(General.PREFIX + 'enterButton.png', region=PosVars.getEnterButton(), grayscale=False, confidence=0.9)
        return btn

    @staticmethod
    def hasSkillTitle():
        
        btn = pyautogui.locateOnScreen(General.PREFIX + 'skillTitle.png', region=PosVars.getSkillTitle(), grayscale=True, confidence=0.8)
        return btn

    @staticmethod
    def hasSkillSelector():
        
        btn = pyautogui.locateOnScreen(General.PREFIX + 'skillSelector.png', region=PosVars.getSkillSelector(), grayscale=True, confidence=0.8)
        return btn

    @staticmethod
    def hasAfkButton():
        
        btn = pyautogui.locateOnScreen(General.PREFIX + 'afkButton.png', region=PosVars.getAfkButton(), grayscale=True, confidence=0.8)
        return btn

    @staticmethod
    def isEssenceFull():
        
        noti = pyautogui.locateOnScreen(General.PREFIX + 'essenceText.png', region=PosVars.getEssenceNoti(), grayscale=True, confidence=0.8)
        return noti

    @staticmethod
    def hasEssenceAtlas(scanArea):
        
        box = pyautogui.locateOnScreen(General.PREFIX + 'atlasText.png', region = scanArea, grayscale=True, confidence=0.6)
        return box

    @staticmethod
    def hasNotification():
        
        noti = pyautogui.locateOnScreen(General.PREFIX + 'notification.png', region=PosVars.getNotiIcon(), grayscale=True, confidence=0.8)
        return noti

    @staticmethod
    def hasAtlasCloseButton():
        
        btn = pyautogui.locateOnScreen(General.PREFIX + 'atlasCloseButton.png', region=PosVars.getAtlasCloseButton(), grayscale=True, confidence=0.8)
        return btn

    @staticmethod
    def hasBlacksmithOnScreen():

        black = pyautogui.locateOnScreen(General.PREFIX + 'blacksmithText.png', grayscale=True, confidence=0.5)
        return black

    # 防御西兰加
    @staticmethod
    def hasDefendComplete():
        
        box = pyautogui.locateOnScreen(General.PREFIX + 'defendComplete.png', region=PosVars.getDefendComplete(), grayscale=True, confidence=0.8)
        return box

    # 防御西兰加
    @staticmethod
    def hasDefendResult():
        
        box = pyautogui.locateOnScreen(General.PREFIX + 'defendReward.png', region=PosVars.getDefendReward(), grayscale=True, confidence=0.8)
        return box

    # 防御西兰加
    @staticmethod
    def hasDefendReviveButton():
        
        btn = pyautogui.locateOnScreen(General.PREFIX + 'reviveButton.png', region=PosVars.getDefendReviveButton(), grayscale=True, confidence=0.8)
        return btn

    @staticmethod
    def isDecay100Percent():
        
        text = pyautogui.locateOnScreen(General.PREFIX + 'decay100.png', region=PosVars.getDecayPercentText(), grayscale=True, confidence=0.8)
        return text