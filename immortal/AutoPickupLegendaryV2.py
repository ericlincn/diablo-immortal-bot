from cn.daftlib.events.EventDispatcher import EventDispatcher
from cn.daftlib.utils.IftttUtil import IftttUtil
from commands.ClickCommand import ClickCommand
from commands.MeleeAttackCommand import MeleeAttackCommand
from commands.TestLegendrayCommand import LegendrayEvent, TestLegendrayCommand
from data.PosVars import Point, PosVars
from immortal.AutoBase import AutoBase
from ScreenWatcher import ScreenWatcher
from cn.daftlib.events.Event import Event
from cn.daftlib.command.Executer import Executer
from scripts.General import General
from scripts.Items import Items

class AutoPickupLegendaryV2(AutoBase, EventDispatcher):

    def __init__(self, watcher: ScreenWatcher, executer: Executer) -> None:
        
        AutoBase.__init__(self, watcher, executer)
        EventDispatcher.__init__(self)

        # self.executer.start(.2)
        
        self.executer.removeCommands()
        self.executer.removeEventsForType(Event.COMPLETE)

        self.addSearch()

    def addSearch(self):

        com = TestLegendrayCommand()
        com.addEventListener(LegendrayEvent.FOUND, self.foundHandler)
        self.executer.addCommmand(com)

    def foundHandler(self, e):

        if e.resultRect:
            print("LegendaryAt:", e.resultRect)
            
            box = e.resultRect
            dest = Point(int(box.x + box.width * .5), int(box.y + box.height + 30))
            self.executer.addCommmand(ClickCommand(None, dest), 2)
            self.executer.addEventListener(Event.COMPLETE, self.pickCompleteHandler)
        else:
            print("Legendary pickup completed")
            self.dispatchEvent(Event(Event.COMPLETE))

    def pickCompleteHandler(self, e):

        self.executer.removeEventListener(Event.COMPLETE, self.pickCompleteHandler)
        self.addSearch()