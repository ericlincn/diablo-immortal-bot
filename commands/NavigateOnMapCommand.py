from cn.daftlib.command.ICommand import ICommand
from cn.daftlib.events.Event import Event
import pydirectinput
import pyautogui
from data.PosVars import Point
from cn.daftlib.core.RemovableEventDispatcher import RemovableEventDispatcher

from scripts.Map import Map

class MapEvent(Event):

    SUCCESS = "success"
    FAIL = "fail"

    def __init__(self, type: str, bubbles: bool = False, cancelable: bool = False) -> None:
        super().__init__(type, bubbles, cancelable)

class NavigateOnMapCommand(ICommand, RemovableEventDispatcher):

    def __init__(self, patternBitmap, destPoint) -> None:

        self.patternBitmap = patternBitmap
        self.destPoint = destPoint

        # super().__init__()
        RemovableEventDispatcher.__init__(self)

    def getBox(self):

        return Map.getPatternBoxInMap(self.patternBitmap)

    def execute(self):

        # box = Map.getPatternBoxInMap(self.patternBitmap)
        box = self.getBox()
        # print("map box:", box)

        if box:
            dest = Point(self.destPoint.x + box.left, self.destPoint.y + box.top)
            # print(dest)
            pydirectinput.moveTo(dest.x, dest.y, 0.2)
            # pydirectinput.click()
            # pydirectinput.mouseDown()
            # pydirectinput.mouseUp()
            pydirectinput.rightClick()

            pydirectinput.move(0, -100, 0.1)
            pydirectinput.click()
            # pydirectinput.mouseDown()
            # pydirectinput.mouseUp()

            # pyautogui.moveTo(dest.x, dest.y, 0.2)
            # pyautogui.click()

            # pyautogui.move(0, -100, 0.1)
            # pyautogui.click()

            self.dispatchEvent(MapEvent(MapEvent.SUCCESS))
        
        else:

            self.dispatchEvent(MapEvent(MapEvent.FAIL))