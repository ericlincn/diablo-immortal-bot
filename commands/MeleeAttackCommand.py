from threading import Timer
from cn.daftlib.command.ICommand import ICommand
import pydirectinput

class MeleeAttackCommand(ICommand):

    def __init__(self, duration = 0) -> None:

        self.duration = duration

        super().__init__()

    def execute(self):

        if self.duration > 0:
            # pydirectinput.keyDown('space')
            # t = Timer(self.duration, pydirectinput.keyUp, ('space'))
            # t.start()
            pydirectinput.press('space', 1, self.duration)
        else:
            pydirectinput.press('space')