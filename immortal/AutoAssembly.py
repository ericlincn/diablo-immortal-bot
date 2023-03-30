from threading import Timer
from ScreenWatcher import ScreenWatcher
from cn.daftlib.events.Event import Event
from commands.ClickCenterCommand import ClickCenterCommand
from cn.daftlib.command.Executer import Executer
from commands.RefuseInviteCommand import RefuseInviteCommand
from commands.SwitchMenuCommand import SwitchMenuCommand
from immortal.AutoBase import AutoBase
from cn.daftlib.time.RepeatingTimer import RepeatingTimer

class AutoAssembly(AutoBase):

    def __init__(self, watcher:ScreenWatcher, executer:Executer) -> None:
        
        super().__init__(watcher, executer)

        self.counter = 0
        self.executer.addEventListener(Event.ENTER_FRAME, self.onEnterFrame)
        self.executer.start(2)

    def onEnterFrame(self, e):

        if self.counter == 0:
            if self.watcher.currentScene == ScreenWatcher.INVITE:
                self.executer.addCommmand(RefuseInviteCommand())

            self.executer.addCommmand(SwitchMenuCommand())
            self.executer.addCommmand(ClickCenterCommand())

            print("Start")
        
        self.counter += 1

        if self.counter >= 120/2:
            self.counter = 0
            
            print("Reset")