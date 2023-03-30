from datetime import datetime
from threading import Timer
from cn.daftlib.time.RepeatingTimer import RepeatingTimer
from scripts.General import General
import pydirectinput
from ScreenWatcher import ScreenWatcher
from cn.daftlib.command.Executer import Executer

class AutoVault:

    def __init__(self, watcher:ScreenWatcher, executer:Executer) -> None:
        
        self.locker = False

        timer = RepeatingTimer(.09, self.ticker)
        timer.start()

    def ticker(self):

        if self.locker == False:
            btn = General.hasEnterButton()
            s = str(datetime.now())

            print(s, end='')
            print('\b' * len(s), end='', flush=True)

            if btn:
                # pydirectinput.click(int(btn.left + btn.width), int(btn.top + btn.height * .5))
                offset = 0
                if btn.left <= 1800: offset = 200
                pydirectinput.click(int(btn.left - offset), int(btn.top + btn.height * .5))
                self.locker = True

                print("clicked:", btn, "locker:", self.locker)

                timer = Timer(60, self.reset)
                timer.start()

    def reset(self):

        self.locker = False

        print("reset", "locker:", self.locker)