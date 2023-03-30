from threading import Timer
from time import sleep
from ScreenWatcher import ScreenWatcher
from cn.daftlib.events.Event import Event
from cn.daftlib.events.EventDispatcher import EventDispatcher
from cn.daftlib.core.ListenerManager import ListenerManager
from cn.daftlib.observer.INotification import INotification
from cn.daftlib.utils.IftttUtil import IftttUtil
from commands.ClickCenterCommand import ClickCenterCommand
from cn.daftlib.command.Executer import Executer
from commands.ClickCommand import ClickCommand
from commands.MeleeAttackCommand import MeleeAttackCommand
from commands.MoveToCenterCommand import MoveToCenterCommand
from commands.NavigateLegendrayOnMapCommand import NavigateLegendrayOnMapCommand
from commands.NavigateOnMapCommand import MapEvent, NavigateOnMapCommand
from commands.RefuseInviteCommand import RefuseInviteCommand
from commands.ReviveAtTownCommand import ReviveAtTownCommand
from commands.SwitchMapCommand import SwitchMapCommand
from commands.SwitchMenuCommand import SwitchMenuCommand
from commands.DrinkPotionCommand import DrinkPotionCommand
from commands.SkillCommand import SkillCommand
from commands.SwitchNotificationCommand import SwitchNotificationCommand
from commands.SwitchPackageCommand import SwitchPackageCommand
from commands.TestEssenceCommand import EssenceEvent, TestEssenceCommand
from commands.TestDecayCommand import DecayEvent, TestDecayCommand
from data.PosVars import Point, PosVars
from immortal.AutoBase import AutoBase
from cn.daftlib.time.RepeatingTimer import RepeatingTimer
from immortal.AutoPickupLegendaryV2 import AutoPickupLegendaryV2
from immortal.AutoPurifyDecay import AutoPurifyDecay
from immortal.AutoSalvaging import AutoSalvaging
from immortal.AutoSubmitEssence import AutoSubmitEssence
from scripts.EssenceAtlasTester import EssenceAtlasTester
from scripts.General import General
from scripts.Skills import Skill
from scripts.Skills import Skills

class AutoFarmingV4(AutoBase):

    def __init__(self, watcher:ScreenWatcher, executer:Executer, patternBitmap:str, route:list) -> None:
        
        super().__init__(watcher, executer)

        self.patternBitmap = patternBitmap
        self.route = route
        self.routeIndex = 0
        self.loopCount = 0

        self.essenceIsFull = False
        self.decayIsFull = False
        self.hasLegendary = False

        self.executer.addEventListener(Event.ENTER_FRAME, self.onEnterFrame)
        self.executer.start(.2)

        self.playRoute()

        # self.auto = AutoSalvaging(self.watcher, self.executer)
        # self.auto.addEventListener(Event.COMPLETE, self.salvagingCompleteHandler)
    
    def handlerNotification(self, notification:INotification):

        match notification.name:
            case "legendary":
                print(notification.name, notification.body)
                self.hasLegendary = True

    def onEnterFrame(self, e):

        if self.watcher.currentState == ScreenWatcher.DEAD:
            self.executer.removeCommands()
            self.executer.removeEventsForType(Event.COMPLETE)
            self.executer.addPriorityCommmand(ReviveAtTownCommand(), 5)
            self.executer.addEventListener(Event.COMPLETE, self.onRevive)
            # print(ListenerManager.printEventTypeList(self.executer))

        if self.watcher.currentState == ScreenWatcher.DANGER:
            self.executer.addPriorityCommmand(DrinkPotionCommand())

        if self.watcher.currentScene == ScreenWatcher.INVITE:
            self.executer.addPriorityCommmand(RefuseInviteCommand(), 1)

        # slow!!!
        # if self.essenceIsFull == False:
        #     if General.isEssenceFull(): self.essenceIsFull = True
    
    def onRevive(self, e):
        
        print("onRevive")
        self.executer.removeEventListener(Event.COMPLETE, self.onRevive)
        self.executer.removeCommands()
        self.routeIndex = 0
        self.playRoute()

    def playRoute(self):

        routeData = self.route[self.routeIndex]
        self.executer.addCommmand(SwitchMapCommand(), 0.4)

        # self.executer.addCommmand(NavigateOnMapCommand(self.patternBitmap, Point(routeData[0], routeData[1])), routeData[2])
        mapcom = NavigateOnMapCommand(self.patternBitmap, Point(routeData[0], routeData[1]))
        mapcom.addEventListener(MapEvent.SUCCESS, self.onMapSuccess)
        mapcom.addEventListener(MapEvent.FAIL, self.onMapFail)
        # self.executer.addCommmand(mapcom, routeData[2])
        duration = routeData[2]
        if self.routeIndex == len(self.route) - 1 and self.maybePackageIsFull() == True:
            duration += 10
        self.executer.addCommmand(mapcom, duration)
        
        self.executer.addEventListener(Event.COMPLETE, self.onRouteEnd)

        # print(self.routeIndex, routeData)

        if self.routeIndex == 0:
            self.executer.addCommmand(SwitchNotificationCommand())
            com = TestEssenceCommand()
            com.addEventListener(EssenceEvent.IS_FULL, self.essenceFullHander)
            self.executer.addCommmand(com)
            com = TestDecayCommand()
            com.addEventListener(DecayEvent.IS_FULL, self.decayFullHander)
            self.executer.addCommmand(com)

    def onMapSuccess(self, e):
        mapcom = e.target
        mapcom.destroy()
    def onMapFail(self, e):

        self.executer.removeEventsForType(Event.COMPLETE)

        print("地图错误")
        self.executer.addCommmand(SwitchPackageCommand(), 2)
        dest = PosVars.getTownPortalButton(0)
        self.executer.addCommmand(ClickCommand(None, dest), 1)
        dest = PosVars.getTownPortalButton(1)
        self.executer.addCommmand(ClickCommand(None, dest), 11)

        self.executer.addEventListener(Event.COMPLETE, self.onRouteEnd)

        mapcom = e.target
        mapcom.destroy()
    def essenceFullHander(self, e):
        if e.resultRect: self.essenceIsFull = True
    def decayFullHander(self, e):
        if e.resultRect: self.decayIsFull = True

    def onRouteEnd(self, e):

        self.executer.removeEventListener(Event.COMPLETE, self.onRouteEnd)

        # print("onRouteEnd", self.watcher.currentScene, self.routeIndex)
        # for map clicking error
        if self.watcher.currentScene == ScreenWatcher.AREA_MAP:
            self.executer.addCommmand(SwitchMapCommand())
            self.routeIndex = 0
            self.playRoute()
            return
        
        # replay the route
        if self.routeIndex == len(self.route) - 1:

            if self.essenceIsFull == True:
                auto = AutoSubmitEssence(self.watcher, self.executer)
                auto.addEventListener(Event.COMPLETE, self.submitCompleteHandler)
            elif self.decayIsFull == True:
                auto = AutoPurifyDecay(self.watcher, self.executer)
                auto.addEventListener(Event.COMPLETE, self.decayCompleteHandler)
            elif self.maybePackageIsFull() == True:
                auto= AutoSalvaging(self.watcher, self.executer)
                auto.addEventListener(Event.COMPLETE, self.salvagingCompleteHandler)
            else:
                self.loopCount += 1
                print(self.loopCount)
                self.routeIndex = 0
                self.playRoute()
        else:
            self.addSkill()

    def maybePackageIsFull(self):
        if self.loopCount >= 30: return True
        else: return False
    
    def salvagingCompleteHandler(self, e):

        self.loopCount = 0
        self.routeIndex = 0
        self.playRoute()

    def submitCompleteHandler(self, e):

        # auto = e.target
        # auto.removeEventListener(Event.COMPLETE, self.submitCompleteHandler)

        # IftttUtil.sendNotification("legendary_found", "da7GPerkoOUOMFzPc6jha7", "essence")
        self.essenceIsFull = False

        auto = AutoPickupLegendaryV2(self.watcher, self.executer)
        auto.addEventListener(Event.COMPLETE, self.pickupCompleteHandler)

    def pickupCompleteHandler(self, e):

        # self.auto.removeEventListener(Event.COMPLETE, self.pickupCompleteHandler)
        # self.auto = None

        self.routeIndex = 0
        self.playRoute()

    def decayCompleteHandler(self, e):

        self.decayIsFull = False
        
        self.routeIndex = 0
        self.playRoute()

    def onSkillEnd(self, e):

        self.executer.removeEventListener(Event.COMPLETE, self.onSkillEnd)

        if self.hasLegendary == True:
            self.executer.addCommmand(SwitchMapCommand(), 0.4)
            # url = General.PREFIX + 'legendaryItemIconBig.png'
            # mapcom = NavigateOnMapCommand(url, Point(0, 0))
            mapcom = NavigateLegendrayOnMapCommand(None, Point(0, 0))
            mapcom.addEventListener(MapEvent.SUCCESS, self.onMapSuccess)
            mapcom.addEventListener(MapEvent.FAIL, self.onLegendaryMapFail)
            self.executer.addCommmand(mapcom, 15)
            self.addSkill(False)
            self.executer.addEventListener(Event.COMPLETE, self.onLegendaryRouteEnd)
        else:
            self.routeIndex += 1
            self.playRoute()

    def onLegendaryMapFail(self, e):

        print("onLegendaryMapFail")

        self.executer.removeEventListener(Event.COMPLETE, self.onLegendaryRouteEnd)
        self.executer.removeCommands()

        self.hasLegendary = False
        self.routeIndex = 0
        self.playRoute()

        mapcom = e.target
        mapcom.destroy()

    def onLegendaryRouteEnd(self, e):

        print("onLegendaryRouteEnd")

        self.executer.removeEventListener(Event.COMPLETE, self.onLegendaryRouteEnd)

        self.hasLegendary = False
        auto = AutoPickupLegendaryV2(self.watcher, self.executer)
        auto.addEventListener(Event.COMPLETE, self.pickupCompleteHandler)

    def addSkill(self, dispatchEvent = True):

        self.executer.addCommmand(MoveToCenterCommand())

        arr = [1, 3, 2, 4]
        count = 0
        for i in range(0, len(arr)):
            skill = Skill(arr[i], False, 0)
            if Skills.getSkillColddown(skill) == Skills.SKILL_IS_COLD_DOWN:
                self.executer.addCommmand(SkillCommand(arr[i]))
                count += 1

        if count < 2:
            self.executer.addCommmand(MoveToCenterCommand())
            self.executer.addCommmand(MeleeAttackCommand())
            self.executer.addCommmand(MeleeAttackCommand())
            self.executer.addCommmand(MeleeAttackCommand())

        if dispatchEvent == True:
            self.executer.addEventListener(Event.COMPLETE, self.onSkillEnd)
        