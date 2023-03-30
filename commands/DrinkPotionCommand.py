from cn.daftlib.command.ICommand import ICommand
import pydirectinput

class DrinkPotionCommand(ICommand):

    def execute(self):
        
        pydirectinput.press('q')