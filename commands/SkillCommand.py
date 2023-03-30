from threading import Timer
from cn.daftlib.command.ICommand import ICommand
import pydirectinput

class SkillCommand(ICommand):

    def __init__(self, keynum, duration = 0) -> None:

        self.keynum = str(keynum)
        self.duration = duration

        super().__init__()

    def execute(self):

        isChannle = False
        if self.duration > 0:
            isChannle = True

        if isChannle:
            pydirectinput.keyDown(self.keynum)
            t = Timer(self.duration, pydirectinput.keyUp, (self.keynum))
            t.start()
        else:
            pydirectinput.press(self.keynum)