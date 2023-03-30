from commands.ClickCommand import ClickCommand
from cn.daftlib.command.ICommand import ICommand
import pydirectinput
import pyautogui

from data.PosVars import Point, PosVars

class ReviveAtBodyCommand(ICommand):

    def __init__(self) -> None:

        button = PosVars.getReviveBodyButton()

        pydirectinput.moveTo(button.x, button.y, 2)
        pydirectinput.click()

        super().__init__()
