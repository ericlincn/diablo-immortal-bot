from ScreenWatcher import ScreenWatcher
from cn.daftlib.command.Executer import Executer

class AutoBase:

    def __init__(self, watcher:ScreenWatcher, executer:Executer) -> None:
        
        self.watcher = watcher
        self.executer = executer