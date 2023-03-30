from cn.daftlib.command.ICommand import ICommand
import pydirectinput
import pyautogui

class MoveToCenterCommand(ICommand):

    def execute(self):
        
        size = pyautogui.size()
        pydirectinput.moveTo(int(size.width*.5), int(size.height*.5), 0.2)
        # pyautogui.moveTo(int(size.width*.5), int(size.height*.5), 0.2)