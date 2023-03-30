from time import sleep
from commands.ClickCommand import ClickCommand
from commands.SwitchNotificationCommand import SwitchNotificationCommand
from commands.TestEssenceCommand import EssenceEvent, TestEssenceCommand
from cn.daftlib.events.EventDispatcher import EventDispatcher
from data.PosVars import Point
from immortal.AutoBase import AutoBase
from ScreenWatcher import ScreenWatcher
from cn.daftlib.events.Event import Event
from cn.daftlib.command.Executer import Executer
from scripts.EssenceAtlasTester import EssenceAtlasTester
from scripts.General import General

class AutoSubmitEssence(AutoBase, EventDispatcher):

    def __init__(self, watcher: ScreenWatcher, executer: Executer) -> None:
        
        # super().__init__(watcher, executer)
        AutoBase.__init__(self, watcher, executer)
        EventDispatcher.__init__(self)

        # self.executer.start(.2)
        self.openNoti()
        # self.naviEssenceCompleteHandler(None)

    def openNoti(self):

        # print("open noti")

        if General.hasNotification():
            self.executer.addCommmand(SwitchNotificationCommand(), 1)
            com = TestEssenceCommand()
            com.addEventListener(EssenceEvent.IS_FULL, self.fullHander)
            self.executer.addCommmand(com)

            # sleep(1)
            # box = General.isEssenceFull()
            # print(box)
            # if box:
            #     dest = Point(int(box.left + box.width * .5), int(box.top + box.height * .5))
            #     self.executer.addCommmand(ClickCommand(None, dest), 12)
            #     self.executer.addEventListener(Event.COMPLETE, self.naviEssenceCompleteHandler)
        else:
            # self.routeIndex = 0
            # self.playRoute()
            self.dispatchEvent(Event(Event.COMPLETE))

    def fullHander(self, e):

        # print("is full?")

        if e.resultRect:
            print("EssenceText:", e.resultRect)
            box = e.resultRect
            dest = Point(int(box.x + box.width * .5), int(box.y + box.height * .5))
            self.executer.addCommmand(ClickCommand(None, dest), 12)
            self.executer.addEventListener(Event.COMPLETE, self.naviEssenceCompleteHandler)
        else:
            self.dispatchEvent(Event(Event.COMPLETE))

    def naviEssenceCompleteHandler(self, e):

        self.executer.removeEventListener(Event.COMPLETE, self.naviEssenceCompleteHandler)
        tester = EssenceAtlasTester()
        tester.addEventListener(Event.COMPLETE, self.atlasCompleteHandler)

    def atlasCompleteHandler(self, e):

        self.dispatchEvent(Event(Event.COMPLETE))