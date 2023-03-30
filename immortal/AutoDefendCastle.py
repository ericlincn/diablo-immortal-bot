from datetime import datetime
from math import sin
from commands.ClickCommand import ClickCommand
from commands.PlayerWalkCommand import PlayerWalkCommand
from commands.RefuseInviteCommand import RefuseInviteCommand
from commands.AntiAfkTestCommand import AntiAfkTestCommand
from commands.MoveToCenterCommand import MoveToCenterCommand
from commands.SkillCommand import SkillCommand
from commands.DrinkPotionCommand import DrinkPotionCommand
from data.PosVars import Point, PosVars
from immortal.AutoBase import AutoBase
from ScreenWatcher import ScreenWatcher
from cn.daftlib.events.Event import Event
from cn.daftlib.command.Executer import Executer
from scripts.General import General
import pydirectinput
import pyautogui
import timeit

from utils.GeomUtil import GeomUtil

class AutoDefendCastle(AutoBase):

    def __init__(self, watcher: ScreenWatcher, executer: Executer) -> None:
        
        super().__init__(watcher, executer)

        self.phase = "idle"
        # self.phase = "battle"
        self.frameCounter = 0
        self.skillLock = False

        self.executer.addEventListener(Event.ENTER_FRAME, self.onEnterFrame)
        self.executer.start(.2)

    def onEnterFrame(self, e):

        nowHour = datetime.now().hour
        # if nowHour > 8 and nowHour < 10: return
        if nowHour == 11 or nowHour == 16:
            self.executer.destroy()
            return

        # print(self.phase)
        start = timeit.default_timer()

        if self.watcher.currentScene == ScreenWatcher.INVITE:
            self.executer.addPriorityCommmand(RefuseInviteCommand())
        elif self.watcher.currentScene == ScreenWatcher.AFK_TEST:
            self.executer.addPriorityCommmand(AntiAfkTestCommand())

        if self.phase == "idle":
            self.executer.addCommmand(MoveToCenterCommand(), 1)
            self.executer.addCommmand(ClickCommand(), 1)

            self.phase = "standby"

        elif self.phase == "standby":
            btn = General.hasEnterButton()
            if btn:
                if btn.left <= 1800: offset = 200
                pydirectinput.click(int(btn.left - offset), int(btn.top + btn.height * .5))
                
                self.phase = "battle"

        elif self.phase == "battle":
            
            if self.frameCounter % 5 == 0:
                complete = General.hasDefendComplete()
                # result = General.hasDefendResult()
                # print(complete)
                if complete:
                    self.phase = "ending"
                    self.executer.addCommmand(MoveToCenterCommand(), 3)
                    self.executer.addCommmand(ClickCommand(), 1)

                # if result:
                #     self.phase = "ending"
                #     self.executer.addCommmand(MoveToCenterCommand(), 5)
                #     self.executer.addCommmand(ClickCommand(), 8)
                #     self.executer.addEventListener(Event.COMPLETE, self.completeHandler)

            reviveButton = General.hasDefendReviveButton()
            if reviveButton:
                self.executer.removeEventsForType(Event.COMPLETE)
                self.executer.removeCommands()
                self.skillLock = False
                dest = Point(PosVars.getDefendReviveButton().x, PosVars.getDefendReviveButton().y + PosVars.getDefendReviveButton().height * .5)
                self.executer.addCommmand(ClickCommand(None, dest))
            else:
                self.fight()

            self.frameCounter += 1

        elif self.phase == "ending":

            if self.frameCounter % 5 == 0:
                result = General.hasDefendResult()

                if result:
                    self.phase = "result"
                    self.executer.addCommmand(MoveToCenterCommand(), 5)
                    self.executer.addCommmand(ClickCommand(), 5)
                    self.executer.addEventListener(Event.COMPLETE, self.completeHandler)

            self.frameCounter += 1

    def completeHandler(self, e):

        print("defend complete", datetime.now())

        self.executer.removeEventsForType(Event.COMPLETE)
        self.executer.removeCommands()

        self.phase = "idle"
        self.frameCounter = 0
        self.skillLock = False
    
    def fight(self):

        # print("fight")
        
        ratio = sin(GeomUtil.degreesToRadians(self.frameCounter*30))
        angle = 90 + ratio * 40 + 10
        dest = General.getPointAroundPlayer(angle, 400)
        # pydirectinput.moveTo(int(dest.x), int(dest.y))
        pyautogui.moveTo(int(dest.x), int(dest.y))

        # if self.watcher.currentState == ScreenWatcher.DANGER:
        health = General.getCurrentHealth()
        if health < 0.3:
            self.executer.addPriorityCommmand(DrinkPotionCommand())

        if self.skillLock == False:
            self.skillLock = True
            self.executer.addCommmand(SkillCommand(3), .2)
            self.executer.addCommmand(SkillCommand(4), .2)
            self.executer.addCommmand(SkillCommand(1, 6), 3)
            self.executer.addCommmand(SkillCommand(2, 5), 2)
            self.executer.addEventListener(Event.COMPLETE, self.skillCompleteHandler)

    def skillCompleteHandler(self, e):

        self.executer.removeEventListener(Event.COMPLETE, self.skillCompleteHandler)

        p1 = General.getPointAroundPlayer(90+45, 200)
        p2 = General.getPointAroundPlayer(360-45, 200)
        self.executer.addCommmand(PlayerWalkCommand(p1))
        self.executer.addCommmand(PlayerWalkCommand(p2))
        self.executer.addEventListener(Event.COMPLETE, self.walkCompleteHandler)

    def walkCompleteHandler(self, e):

        self.executer.removeEventListener(Event.COMPLETE, self.walkCompleteHandler)
        self.skillLock = False