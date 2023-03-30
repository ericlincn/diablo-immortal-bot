from commands.ClickCommand import ClickCommand
from cn.daftlib.command.ICommand import ICommand
import pydirectinput
import pyautogui

from data.PosVars import Point, PosVars

class ClickCenterCommand(ClickCommand):

    def __init__(self, offsetPoint = None, destPoint = None) -> None:

        super().__init__(offsetPoint, destPoint)

        self.offsetPoint = None
        # size = pyautogui.size()
        # self.destPoint = Point(size.width*.5, size.height*.5)
        self.destPoint = PosVars.getCenter()
