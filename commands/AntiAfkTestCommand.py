from cn.daftlib.command.ICommand import ICommand
import pydirectinput
from data.PosVars import Point, PosVars

class AntiAfkTestCommand(ICommand):

    def execute(self):
        
        btn = PosVars.getAfkButton()
        pydirectinput.moveTo(int(btn.x + btn.width), int(btn.y + btn.height), 0.2)
        pydirectinput.click()