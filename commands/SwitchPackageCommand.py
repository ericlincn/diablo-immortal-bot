from cn.daftlib.command.ICommand import ICommand
import pydirectinput

class SwitchPackageCommand(ICommand):

    def execute(self):
        pydirectinput.press('i')