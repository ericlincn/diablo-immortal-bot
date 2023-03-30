from cn.daftlib.command.ICommand import ICommand
import pydirectinput
import pyautogui
from data.PosVars import Point, PosVars

class ExitDungeonCommand(ICommand):

    def execute(self):
        
        exit = PosVars.getExitDungeonButton()
        btn = PosVars.getConfirmButton()

        pydirectinput.moveTo(exit.x, exit.y, 0.2)
        pydirectinput.click()

        pydirectinput.moveTo(btn.x, btn.y, 0.1)
        pydirectinput.click()
