from time import sleep
from cn.daftlib.command.ICommand import ICommand
from cn.daftlib.events.EventDispatcher import EventDispatcher
from commands.ClickCommand import ClickCommand
from data.PosVars import Point, PosVars
from immortal.AutoBase import AutoBase
from ScreenWatcher import ScreenWatcher
from cn.daftlib.events.Event import Event
from cn.daftlib.command.Executer import Executer
from scripts.General import General

class AutoSalvaging(AutoBase, EventDispatcher):

    def __init__(self, watcher: ScreenWatcher, executer: Executer) -> None:
        
        AutoBase.__init__(self, watcher, executer)
        EventDispatcher.__init__(self)

        # self.executer.start(.2)
        self.start()

    def start(self):

        # print(General.hasBlacksmithOnScreen())

        self.executer.removeCommands()
        self.executer.removeEventsForType(Event.COMPLETE)
        self.executer.addEventListener(Event.COMPLETE, self.completeHandler)

        black = General.hasBlacksmithOnScreen()

        if black:
            dest = Point(black.left + black.width * .5, black.top + black.height + 100)
            self.executer.addCommmand(ClickCommand(None, dest), 3)

            self.executer.addCommmand(ClickCommand(None, PosVars.getSalvagingButton(0)))
            self.executer.addCommmand(ClickCommand(None, PosVars.getSalvagingButton(1)))
            self.executer.addCommmand(ClickCommand(None, PosVars.getSalvagingButton(2)))
            self.executer.addCommmand(ClickCommand(None, PosVars.getSalvagingButton(3)))
            self.executer.addCommmand(ClickCommand(None, PosVars.getSalvagingButton(4)))
            self.executer.addCommmand(ClickCommand(None, PosVars.getSalvagingButton(4)))
            self.executer.addCommmand(ClickCommand(None, PosVars.getSalvagingButton(5)), 1)
        else:
            # self.completeHandler(None)
            self.executer.addCommmand(ICommand(), 1)

    def completeHandler(self, e):
        
        self.executer.removeEventListener(Event.COMPLETE, self.completeHandler)
        print("Salvaging Complete")
        event = Event(Event.COMPLETE)
        self.dispatchEvent(event)