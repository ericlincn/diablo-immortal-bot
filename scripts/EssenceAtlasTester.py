from time import sleep
from cn.daftlib.events.Event import Event
from cn.daftlib.command.ICommand import ICommand
from cn.daftlib.events.IEventDispatcher import IEventDispatcher
from cn.daftlib.events.EventDispatcher import EventDispatcher
from cn.daftlib.time.RepeatingTimer import RepeatingTimer
from data.PosVars import Point, PosVars, Rect
from scripts.General import General

import pyautogui
import pydirectinput
import cv2 as cv
import numpy as np

class EssenceAtlasTester(EventDispatcher):

    def __init__(self, target: IEventDispatcher = None) -> None:

        super().__init__(target)

        self.a = -90
        self.r = 100
        self.timer = RepeatingTimer(0.2, self.__testing)
        self.timer.start()

    def __testing(self):

        p = General.getPointAroundPlayer(self.a, self.r)
        pydirectinput.moveTo(int(p.x), int(p.y))
        # box = (300, 200)
        # img = pyautogui.screenshot(region=(p.x - box[0]*.5, p.y - box[1], box[0], box[1]))
        # img = cv.cvtColor(np.array(img), cv.COLOR_RGB2BGR)
        # rect = Rect(int(p.x - box[0]*.5), int(p.y - box[1]), box[0], box[1])
        target = General.hasEssenceAtlas(None)
        # mouse = pyautogui.position()

        if target:
            # pydirectinput.moveTo(mouse.x, mouse.y, 0.2)
            pydirectinput.click()
            self.timer.cancel()
            sleep(16)
            rect = General.hasAtlasCloseButton()
            if rect:
                dest = Point(int(rect.left + rect.width*.5), int(rect.top + rect.height*.5))
                pydirectinput.moveTo(dest.x, dest.y, 0.2)
                pydirectinput.click()
            print("Atlas closed")
            sleep(5)
            event = Event(Event.COMPLETE)
            self.dispatchEvent(event)
        else:
            self.a += 30
            if self.a >= 270:
                self.a = -90
                self.r += 100
            if self.r >= 400:
                self.timer.cancel()
                print("Atlas test failed")
                event = Event(Event.COMPLETE)
                self.dispatchEvent(event)
