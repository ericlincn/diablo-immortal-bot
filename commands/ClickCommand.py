from cn.daftlib.command.ICommand import ICommand
import pydirectinput

class ClickCommand(ICommand):

    def __init__(self, offsetPoint = None, destPoint = None) -> None:

        self.offsetPoint = offsetPoint
        self.destPoint = destPoint

        super().__init__()

    def execute(self):

        if self.destPoint:
            pydirectinput.moveTo(int(self.destPoint.x), int(self.destPoint.y), 0.1)

        if self.offsetPoint:
            pydirectinput.move(int(self.offsetPoint.x), int(self.offsetPoint.y), 0.1)
        
        pydirectinput.click()