from cn.daftlib.command.ICommand import ICommand
import pydirectinput
import pyautogui
from data.PosVars import Point, PosVars

class SwitchNotificationCommand(ICommand):

    def execute(self):
        
        btn = PosVars.getNotiButton()

        pydirectinput.moveTo(btn.x, btn.y, 0.1)
        pydirectinput.click()
