from cn.daftlib.command.ICommand import ICommand
import pydirectinput
from data.PosVars import Point, PosVars

class RefuseInviteCommand(ICommand):

    def execute(self):
        
        btn = PosVars.getInviteButton()
        pydirectinput.moveTo(int(btn.x + btn.width), int(btn.y + btn.height * .5), 0.2)
        pydirectinput.click()