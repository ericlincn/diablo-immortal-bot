from cn.daftlib.command.ICommand import ICommand
import pydirectinput

class SwitchMapCommand(ICommand):

    def execute(self):
        pydirectinput.press('m')