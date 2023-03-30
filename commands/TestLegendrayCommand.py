from cn.daftlib.events.Event import Event
from cn.daftlib.command.ICommand import ICommand
from cn.daftlib.events.EventDispatcher import EventDispatcher
from data.PosVars import Rect
from scripts.General import General
from scripts.Items import Items

class LegendrayEvent(Event):

    FOUND = "found"

    def __init__(self, type: str, bubbles: bool = False, cancelable: bool = False) -> None:
        super().__init__(type, bubbles, cancelable)

        self.resultRect = None

class TestLegendrayCommand(ICommand, EventDispatcher):

    def __init__(self) -> None:

        ICommand.__init__(self)
        EventDispatcher.__init__(self)

        # self.type = type

    def execute(self):
        
        # item = Items.hasLegendrayOnScreen(self.type)
        # event = LegendrayEvent(LegendrayEvent.FOUND)

        # if item:
        #     event.resultRect = Rect(item.left, item.top, item.width, item.height)

        # self.dispatchEvent(event)

        arr = Items.hasLegendrayOnScreen()
        event = LegendrayEvent(LegendrayEvent.FOUND)

        if arr:
            item = arr[0]
            event.resultRect = Rect(item.left, item.top, item.width, item.height)
            
        self.dispatchEvent(event)

