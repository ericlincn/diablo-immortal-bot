from datetime import datetime
from ScreenWatcher import ScreenWatcher
from cn.daftlib.events.Event import Event
from commands.AntiAfkTestCommand import AntiAfkTestCommand
from commands.ClickCommand import ClickCommand
from commands.ClickCenterCommand import ClickCenterCommand
from cn.daftlib.command.Executer import Executer
from commands.ExitDungeonCommand import ExitDungeonCommand
from commands.NavigateOnMapCommand import NavigateOnMapCommand
from commands.RefuseInviteCommand import RefuseInviteCommand
from commands.SwitchMapCommand import SwitchMapCommand
from immortal.AutoBase import AutoBase
from data.PosVars import Point, PosVars
from scripts.General import General
from scripts.Map import Map

class AutoEchoV2(AutoBase):

    def __init__(self, watcher:ScreenWatcher, executer:Executer) -> None:
        
        super().__init__(watcher, executer)
        
        self.phase = -1
        self.frameCounter = 0

        self.executer.addEventListener(Event.ENTER_FRAME, self.onEnterFrame)
        self.executer.start(.5)

    def onMovingComplete(self, e):

        self.executer.removeEventListener(Event.COMPLETE, self.onMovingComplete)
        self.phase = -1
        print("moving complete")

    def onEnterFrame(self, e):

        if self.watcher.currentScene == ScreenWatcher.INVITE:
            self.executer.addPriorityCommmand(RefuseInviteCommand())
        elif self.watcher.currentScene == ScreenWatcher.AFK_TEST:
            self.executer.addPriorityCommmand(AntiAfkTestCommand())

        # UTC+9
        nowHour= datetime.now().hour + 1
        # 8-10 12-14 18-20 22-0
        is8 = nowHour >= 8 and nowHour < 10
        is12 = nowHour >= 12 and nowHour < 14
        is18 = nowHour >= 18 and nowHour < 20
        is22 = nowHour >= 22 and nowHour <= 23
        isOnTime = is8 or is12 or is18 or is22
        if isOnTime == False: return

        # idle in town
        if self.phase == -1:

            cap = General.hasBattlegroundCaptainOnScreen()
            print(cap)
            if cap:
                dest = Point(cap.left + cap.width * .5, cap.top + cap.height + 100)
                self.executer.addCommmand(ClickCommand(None, dest), 2)

                self.executer.addCommmand(ClickCommand(None, PosVars.getEchoButton(0)))
                self.executer.addCommmand(ClickCommand(None, PosVars.getEchoButton(1)))
                self.executer.addCommmand(ClickCommand(None, PosVars.getEchoButton(2)))

                # next
                self.phase = 0
            else:
                # search for cap
                self.executer.addCommmand(SwitchMapCommand())
                self.executer.addCommmand(NavigateOnMapCommand(General.PREFIX + "west1.png", Point(164, 54)), 3)
                self.executer.addEventListener(Event.COMPLETE, self.onMovingComplete)
                self.phase = -2

        # into the battle
        if self.phase == 0:

            if General.hasReadyButton():
                dest = PosVars.getReadyButton()
                self.executer.addCommmand(ClickCommand(None, Point(dest.x+dest.width, dest.y+dest.height)))
                
                # next
                self.phase = 1

            if self.frameCounter > 16 and self.watcher.currentScene == ScreenWatcher.FIELD:
                self.reset()

            if self.frameCounter > 16 and self.watcher.currentScene == ScreenWatcher.CONVERSATION:
                self.reset()

            self.frameCounter += 1
        
        # on battle
        if self.phase == 1:

            # 有傻逼没点匹配
            if General.hasReadyButton():
                dest = PosVars.getReadyButton()
                self.executer.addCommmand(ClickCommand(None, Point(dest.x+dest.width, dest.y+dest.height)))

            if General.hasResultCloseButton():
                r = PosVars.getResultCloseButton()
                dest = Point(r.x + r.width *.5, r.y + r.height * .5)
                self.executer.addCommmand(ClickCommand(None, dest))

            if General.hasRewardText():
                self.executer.addCommmand(ClickCenterCommand(), 3)
                self.executer.addCommmand(ExitDungeonCommand())

                # next
                self.phase = 2
                print("finished at:", datetime.now())
            
            # if self.watcher.currentScene == ScreenWatcher.FIELD:
            #     self.phase = 2
            #     self.reset()

        if self.phase == 2:

            if General.hasResultCloseButton():
                r = PosVars.getResultCloseButton()
                dest = Point(r.x + r.width *.5, r.y + r.height * .5)
                self.executer.addCommmand(ClickCommand(None, dest))
                
            if self.watcher.currentScene == ScreenWatcher.FIELD:
                self.reset()

    def reset(self):

        self.executer.removeCommands()
        self.phase = -1
        self.frameCounter = 0