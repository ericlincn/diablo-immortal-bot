from cn.daftlib.events.Event import Event
from cn.daftlib.command.ICommand import ICommand
from cn.daftlib.time.RepeatingTimer import RepeatingTimer
from cn.daftlib.events.EventDispatcher import EventDispatcher
from cn.daftlib.core.RemovableEventDispatcher import RemovableEventDispatcher
import timeit

class Executer(RemovableEventDispatcher):

    __timer = None
    __commandsArr = None
    __undoCommand = None
    __frameDuration = 0.1

    def __init__(self, target = None) -> None:

        super().__init__(target)

        self.removeCommands()
    
    def removeCommands(self):

        self.__commandsArr = []
        self.__undoCommand = None

    def start(self, frameDuration):

        if self.__timer: return

        self.__frameDuration = frameDuration
        self.__timer = RepeatingTimer(self.__frameDuration, self.__timerHandler)
        self.__timer.start()

    def destroy(self) -> None:

        super().destroy()

        self.removeCommands()
        
        self.__timer.cancel()

    def __timerHandler(self):

        # start = timeit.default_timer()

        # 执行第一条Command前
        event = Event(Event.ENTER_FRAME)
        self.dispatchEvent(event)


        # 打印所有命令
        # all = self.printCommmands()
        # if len(all) > 0: print(all)


        l = len(self.__commandsArr)
        if l > 0:
            # print(self.commandsArr[0])
            self.__commandsArr[0].execute()
            try:
                self.__undoCommand = self.__commandsArr.pop(0)
            except IndexError as e:
                print("IndexError: ", e, "@class Executer")


            # 执行完所有命令后
            if len(self.__commandsArr) == 0:
                event = Event(Event.COMPLETE)
                self.dispatchEvent(event)


        # 执行第一条Command后
        event = Event(Event.EXIT_FRAME)
        self.dispatchEvent(event)

        # print(timeit.default_timer() - start)

    def addCommmand(self, command:ICommand, duration:float = 0):

        self.__commandsArr.append(command)

        totalFrame = int(duration / self.__frameDuration)

        i = 0
        while i < totalFrame:
            self.__commandsArr.append(ICommand())
            i += 1
    
    def addPriorityCommmand(self, command:ICommand, duration:float = 0):

        self.__commandsArr.insert(0, command)

        totalFrame = int(duration / self.__frameDuration)

        i = 0
        while i < totalFrame:
            self.__commandsArr.insert((i+1), ICommand())
            i += 1

    def printCommmands(self):

        s = ""
        l = len(self.__commandsArr)
        if l > 0:
            for i in range(0, l):
                c = str(type(self.__commandsArr[i]))
                c = c.replace("<class '", "")
                c = c.replace("'>", "")
                c = c.split(".")[-1]

                if c == "ICommand": c = "."
                else: c = c.replace("Command", ""); c += " "
                
                s += c
        return s