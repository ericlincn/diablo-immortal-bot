from cn.daftlib.command.ICommand import ICommand
import pydirectinput

class SwitchMenuCommand(ICommand):

    def execute(self):
        pydirectinput.press('esc')