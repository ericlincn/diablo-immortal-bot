from cn.daftlib.events.Event import Event
from cn.daftlib.command.ICommand import ICommand
from cn.daftlib.events.EventDispatcher import EventDispatcher
from data.PosVars import Rect
from scripts.General import General

class EssenceEvent(Event):

    IS_FULL = "isFull"

    def __init__(self, type: str, bubbles: bool = False, cancelable: bool = False) -> None:
        super().__init__(type, bubbles, cancelable)

        self.resultRect = None

class TestEssenceCommand(ICommand, EventDispatcher):

    def execute(self):
        
        box = General.isEssenceFull()
        event = EssenceEvent(EssenceEvent.IS_FULL)
        # print(box)
        if box:
            event.resultRect = Rect(box.left, box.top, box.width, box.height)

        self.dispatchEvent(event)
