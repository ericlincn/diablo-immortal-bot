import pyautogui
import collections

Point = collections.namedtuple("Point", "x y")
Size = collections.namedtuple("Size", "width height")
Rect = collections.namedtuple("Rect", "x y width height")

class PosVars:

    # @staticmethod
    # def getWindowSize():
    #     return Rect(-9, -23, 1938, 1127)
    #     return Size(1920, 1080)

    ZERO_X = 99
    ZERO_Y = 99

    @staticmethod
    def getZero():
        return Point(PosVars.ZERO_X, PosVars.ZERO_Y)

    @staticmethod
    def getCenter():
        return Point(int(1920*.5), int(1080*.5))

    # @staticmethod
    # def getMenuButton():
    #     return Point(PosVars.getWindowSize().width-33, PosVars.getZero().y+50)

    @staticmethod
    def getHealthBar():
        return Rect(PosVars.getZero().x+14, PosVars.getZero().y+130, 170, 1)

    @staticmethod
    def getReviveTownButton():
        return Point(PosVars.getZero().x+540, PosVars.getZero().y+795)
    
    @staticmethod
    def getReviveBodyButton():
        return Point(PosVars.getZero().x+1385, PosVars.getZero().y+795)
    
    @staticmethod
    def getSkill4():
        return Rect(PosVars.getZero().x+1818, PosVars.getZero().y+783, 72, 72)
    
    @staticmethod
    def getSkill3():
        return Rect(PosVars.getZero().x+1725, PosVars.getZero().y+783, 72, 72)

    @staticmethod
    def getSkill2():
        return Rect(PosVars.getZero().x+1656, PosVars.getZero().y+852, 72, 72)

    @staticmethod
    def getSkill1():
        return Rect(PosVars.getZero().x+1656, PosVars.getZero().y+945, 72, 72)

    @staticmethod
    def getSkillColddownOffse():
        return Point(32, 6)

    @staticmethod
    def getChannleSkillOffseA():
        return Point(32, 3)
    
    @staticmethod
    def getChannleSkillOffseB():
        return Point(70, 35)

    @staticmethod
    def getHealthBarLeftCorner():
        return Rect(PosVars.getZero().x+4, PosVars.getZero().y+131, 10, 10)

    @staticmethod
    def getHealthBarRightCorner():
        return Rect(PosVars.getZero().x+186, PosVars.getZero().y+131, 10, 10)
    
    @staticmethod
    def getInviteButton():
        return Rect(PosVars.getZero().x+657, PosVars.getZero().y+717, 80, 80)

    @staticmethod
    def getAreaMapTitle():
        return Rect(PosVars.getZero().x+50, PosVars.getZero().y+66, 50, 50)
    
    @staticmethod
    def getEchoButton(index):
        match index:
            case 0:
                return Point(PosVars.getZero().x+1526, PosVars.getZero().y-15+584)
            case 1:
                return Point(PosVars.getZero().x+1526, PosVars.getZero().y-15+418)
            case 2:
                return Point(PosVars.getZero().x+1472, PosVars.getZero().y-15+860)
        
    @staticmethod
    def getReadyButton():
        return Rect(PosVars.getZero().x+1001, PosVars.getZero().y-15+943, 50, 50)

    @staticmethod
    def getPassportButton():
        # return Rect(PosVars.getZero().x+76, PosVars.getZero().y-15+238, 33, 27)
        return Rect(PosVars.getZero().x+0, PosVars.getZero().y-15+238, 33+76, 27)

    @staticmethod
    def getRewardText():
        return Rect(PosVars.getZero().x+915, PosVars.getZero().y-15+785, 90, 40)

    @staticmethod
    def getResultCloseButton():
        return Rect(PosVars.getZero().x+1767, PosVars.getZero().y-15+195, 50, 50)

    @staticmethod
    def getReviveTownButtonCorner():
        return Rect(PosVars.getZero().x+695, PosVars.getZero().y-15+767, 80, 80)

    @staticmethod
    def getExitDungeonButton():
        return Point(PosVars.getZero().x+1461, PosVars.getZero().y-15+233)

    @staticmethod
    def getConfirmButton():
        return Point(PosVars.getZero().x+1160, PosVars.getZero().y-15+666)

    @staticmethod
    def getConversationCorner():
        return Rect(PosVars.getZero().x+395, PosVars.getZero().y-15+747, 30, 100)

    @staticmethod
    def getEnterButton():
        return Rect(PosVars.getZero().x+1696, PosVars.getZero().y-15+815, 200, 100)
        # return Rect(PosVars.getZero().x+1470, PosVars.getZero().y-15+816, 100, 100)
        # return Rect(PosVars.getZero().x+1018, PosVars.getZero().y-15+816, 100, 100)

    @staticmethod
    def getSkillTitle():
        return Rect(PosVars.getZero().x+42, PosVars.getZero().y-15+67, 80, 80)

    @staticmethod
    def getSkillSelector():
        # selector图片实际尺寸
        # return Rect(PosVars.getZero().x+579, PosVars.getZero().y-15+597, 50, 50)
        return Rect(PosVars.getZero().x+558, PosVars.getZero().y-15+576, 90, 90)

    @staticmethod
    def getSwordSkillSelectorButton():
        return Point(PosVars.getZero().x+366, PosVars.getZero().y-15+577)

    @staticmethod
    def getSkillSwitchButton():
        return Point(PosVars.getZero().x+966, PosVars.getZero().y-15+908)

    @staticmethod
    def getRightSkillSlot():
        return Point(PosVars.getZero().x+1804, PosVars.getZero().y-15+655)

    @staticmethod
    def getAfkButton():
        return Rect(PosVars.getZero().x+982, PosVars.getZero().y-15+732, 200, 40)

    @staticmethod
    def getMonsterWhiteTitle():
        return Rect(PosVars.getZero().x+736, PosVars.getZero().y-15+63, 60, 50)

    @staticmethod
    def getMonsterBlueTitle():
        return Rect(PosVars.getZero().x+703, PosVars.getZero().y-15+63, 60, 50)

    @staticmethod
    def getMonsterGoldTitle():
        return Rect(PosVars.getZero().x+667, PosVars.getZero().y-15+63, 60, 50)

    @staticmethod
    def getMonsterPurpleTitle():
        return Rect(PosVars.getZero().x+671, PosVars.getZero().y-15+63, 60, 50)

    @staticmethod
    def getMonsterOrangeTitle():
        return Rect(PosVars.getZero().x+666, PosVars.getZero().y-15+63, 60, 50)

    @staticmethod
    def getMonsterTitle():
        return Rect(PosVars.getZero().x+666, PosVars.getZero().y-15+63, 130, 50)

    @staticmethod
    def getMinimap():
        return Rect(PosVars.getZero().x+1499, PosVars.getZero().y-15+22, 357, 237)

    @staticmethod
    def getEssenceNoti():
        # 438, 443
        return Rect(PosVars.getZero().x+438, PosVars.getZero().y-15+250, 250+10, 350)

    @staticmethod
    def getNotiButton():
        return Point(PosVars.getZero().x+270, PosVars.getZero().y-15+250)

    @staticmethod
    def getNotiIcon():
        return Rect(PosVars.getZero().x+254, PosVars.getZero().y-15+238, 33, 27)

    # @staticmethod
    # def getAtlasCloseButton():
    #     return Point(PosVars.getZero().x+1848, PosVars.getZero().y-15+64)

    @staticmethod
    def getAtlasCloseButton():
        return Rect(PosVars.getZero().x+1829, PosVars.getZero().y-15+42, 50, 50)

    @staticmethod
    def getSalvagingButton(index):
        match index:
            case 0:
                return Point(PosVars.getZero().x+1526, PosVars.getZero().y-15+687)
            case 1:
                return Point(PosVars.getZero().x+783, PosVars.getZero().y-15+984)
            case 2:
                return Point(PosVars.getZero().x+871, PosVars.getZero().y-15+984)
            case 3:
                return Point(PosVars.getZero().x+961, PosVars.getZero().y-15+984)
            case 4:
                return Point(PosVars.getZero().x+1498, PosVars.getZero().y-15+967)
            case 5:
                return Point(PosVars.getZero().x+1851, PosVars.getZero().y-15+62)

    # @staticmethod
    # def getFullbagIndicator():
    #     return Rect(PosVars.getZero().x+1511, PosVars.getZero().y-15+970, 50, 50)

    @staticmethod
    def getFullbagText():
        return Rect(PosVars.getZero().x+1177, PosVars.getZero().y-15+915, 146, 30)

    @staticmethod
    def getDefendComplete():
        return Rect(PosVars.getZero().x+946, PosVars.getZero().y-15+233, 50, 50)

    @staticmethod
    def getDefendReward():
        return Rect(PosVars.getZero().x+951, PosVars.getZero().y-15+195, 24, 24)

    @staticmethod
    def getDefendReviveButton():
        return Rect(PosVars.getZero().x+1124, PosVars.getZero().y-15+767, 80, 80)

    @staticmethod
    def getDecayPercentText():
        return Rect(PosVars.getZero().x+110, PosVars.getZero().y-15+300, 45, 50)
    
    @staticmethod
    def getDecayTree():
        return Point(PosVars.getZero().x+1190, PosVars.getZero().y-15+750)

    @staticmethod
    def getTownPortalButton(index):
        match index:
            case 0:
                return Point(PosVars.getZero().x+1326, PosVars.getZero().y-15+994)
            case 1:
                return Point(PosVars.getZero().x+1320, PosVars.getZero().y-15+910)