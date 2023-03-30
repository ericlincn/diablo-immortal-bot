from cn.daftlib.command.ICommand import ICommand
import pydirectinput
from data.PosVars import Point, PosVars

class PlayerWalkCommand(ICommand):

    def __init__(self, destPoint) -> None:

        self.destPoint = destPoint

        super().__init__()

    def execute(self):
        
        pydirectinput.moveTo(int(self.destPoint.x), int(self.destPoint.y), 0.1)
        pydirectinput.rightClick()