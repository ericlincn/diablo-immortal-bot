from time import sleep
from data.PosVars import PosVars
from cn.daftlib.time.RepeatingTimer import RepeatingTimer
from datetime import datetime
from scripts.General import General
import pydirectinput
import pyautogui
from ScreenWatcher import ScreenWatcher
from cn.daftlib.command.Executer import Executer

class AutoSwitchHorse:

    def __init__(self, watcher:ScreenWatcher, executer:Executer) -> None:
        
        self.phase = -1
        self.currentSkill = None

        timer = RepeatingTimer(1, self.ticker)
        timer.start()

    def ticker(self):
        
        if General.hasSkillTitle():

            if General.hasSkillSelector():
                self.currentSkill = "sword"
            else:
                self.currentSkill = "horse"
            
            # print(self.currentSkill, self.phase)
            if self.phase == -1:

                if self.currentSkill == "sword":
                    self.phase = 0
                    self.switchToHorse()
                    self.currentSkill = "horse"
                    sleep(3)
                    self.phase = -1
                    
                elif self.currentSkill == "horse":
                    self.phase = 0
                    self.switchToSword()
                    self.currentSkill = "sword"
                    sleep(2)
                    self.phase = -1

    def switchToHorse(self):

        print("switchToHorse")

        dest = PosVars.getSwordSkillSelectorButton()
        pydirectinput.moveTo(dest.x, 880, .4)
        pydirectinput.mouseDown()
        pydirectinput.move(0, -600, 2)
        pydirectinput.mouseUp()
        pydirectinput.moveTo(dest.x, 800, .4)

        pydirectinput.click()
        dest = PosVars.getSkillSwitchButton()
        pydirectinput.moveTo(dest.x, dest.y, .4)
        pydirectinput.click()
        dest = PosVars.getRightSkillSlot()
        pydirectinput.moveTo(dest.x, dest.y, .4)
        pydirectinput.click()
        pydirectinput.press("n", 1, .4)

    def switchToSword(self):

        print("switchToSword")

        dest = PosVars.getSwordSkillSelectorButton()
        pydirectinput.moveTo(dest.x, dest.y, .4)
        pydirectinput.click()
        dest = PosVars.getSkillSwitchButton()
        pydirectinput.moveTo(dest.x, dest.y, .4)
        pydirectinput.click()
        dest = PosVars.getRightSkillSlot()
        pydirectinput.moveTo(dest.x, dest.y, .4)
        pydirectinput.click()
        pydirectinput.press("n", 1, .4)