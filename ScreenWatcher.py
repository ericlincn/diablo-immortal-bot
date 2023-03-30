import timeit
from scripts.General import General
from cn.daftlib.time.RepeatingTimer import RepeatingTimer
from scripts.Map import Map

class ScreenWatcher:

    UNKNOWN = "unknown"

    FIELD = "field"
    DUNGEON = "dungeon"
    RIFT = "rift"
    AREA_MAP = "areaMap"
    DUNGEON_MAP = "dungeonMap"
    CONVERSATION = "conversation"
    INVITE = "invite"
    AFK_TEST = "afkTest"

    HEALTHY = "healthy"
    DANGER = "danger"
    DEAD = "dead"

    def __init__(self) -> None:

        self.currentScene = ScreenWatcher.UNKNOWN
        self.currentState = ScreenWatcher.UNKNOWN

        self.__timer = RepeatingTimer(.2, self.__timerHandler)
        self.__timer.start()

    def __timerHandler(self):

        # self.currentScene = ScreenWatcher.UNKNOWN
        # self.currentState = ScreenWatcher.UNKNOWN

        start = timeit.default_timer()

        hasHealthBar = General.hasHealthBar()
        # hasInviteButton = General.hasInviteButton()
        # hasAreaMap = Map.hasAreaMapTitle()
        hasPassportButton = General.hasPassportButton()
        # hasReviveButton = General.hasReviveTownButton()
        # hasConversation = General.hasConversation()
        # hasAfkTest = General.hasAfkButton()

        if hasHealthBar and hasPassportButton:
            self.currentScene = ScreenWatcher.FIELD
        elif Map.hasAreaMapTitle():
            self.currentScene = ScreenWatcher.AREA_MAP
        elif General.hasConversation() and hasHealthBar == None:
            self.currentScene = ScreenWatcher.CONVERSATION
        else:
            self.currentScene = ScreenWatcher.UNKNOWN

        # if hasConversation and hasHealthBar == None:
        #     self.currentScene = ScreenWatcher.CONVERSATION

        if General.hasInviteButton():
            self.currentScene = ScreenWatcher.INVITE
        elif General.hasAfkButton():
            self.currentScene = ScreenWatcher.AFK_TEST

        # if hasHealthBar:
        if hasHealthBar and hasPassportButton:
            health = General.getCurrentHealth()
            # print(health)
            if health < 0.01 and General.hasReviveTownButton():
                self.currentState = ScreenWatcher.DEAD
            elif health < 0.5:
                self.currentState = ScreenWatcher.DANGER
            else:
                self.currentState = ScreenWatcher.HEALTHY
        else:
            self.currentState = ScreenWatcher.UNKNOWN

        # print("scene: "+self.currentScene, "state: "+self.currentState)

        # print(timeit.default_timer() - start)