from cn.daftlib.events.IEventDispatcher import IEventDispatcher

class EventInfo:

    def __init__(self, type:str, listener:callable, useCapture:bool) -> None:
        
        self.type = type
        self.listener = listener
        self.useCapture = useCapture

    def equals(self, eventInfo) -> bool:
        
        return self.type == eventInfo.type and self.listener == eventInfo.listener and self.useCapture == eventInfo.useCapture

class ListenerManager:

    __dispatcherMap = dict()

    @staticmethod
    def registerEventListener(dispatcher:IEventDispatcher, type:str, listener:callable, useCapture:bool) -> None:
        
        # eventInfoArr = ListenerManager.__dispatcherMap[dispatcher]
        eventInfoArr = ListenerManager.__dispatcherMap.get(dispatcher)
        newEventInfo:EventInfo = EventInfo(type, listener, useCapture)
        # oldEventInfo:EventInfo

        if eventInfoArr != None:

            i = len(eventInfoArr)
            while i > 0:
                i -= 1
                oldEventInfo = eventInfoArr[i]
                if oldEventInfo.equals(newEventInfo):
                    return
                
            eventInfoArr.append(newEventInfo)
        else:
            ListenerManager.__dispatcherMap[dispatcher] = [newEventInfo]
        
    @staticmethod
    def unregisterEventListener(dispatcher:IEventDispatcher, type:str, listener:callable, useCapture:bool) -> None:

        # var eventInfoArr:Array = __dispatcherMap[dispatcher];
        eventInfoArr = ListenerManager.__dispatcherMap.get(dispatcher)
        newEventInfo = EventInfo(type, listener, useCapture)

        if eventInfoArr == None: return

        i = len(eventInfoArr)
        while i > 0:
            i -= 1
            oldEventInfo = eventInfoArr[i]
            if oldEventInfo.equals(newEventInfo):
                # eventInfoArr.splice(i, 1)
                del eventInfoArr[i]

        if len(eventInfoArr) == 0:
            if dispatcher in ListenerManager.__dispatcherMap:
                del ListenerManager.__dispatcherMap[dispatcher]

    @staticmethod
    def removeEventsForType(dispatcher:IEventDispatcher, type:str) -> None:

        eventInfoArr = ListenerManager.__dispatcherMap.get(dispatcher)

        if eventInfoArr == None: return

        i = len(eventInfoArr)
        while i > 0:
            i -= 1
            oldEventInfo = eventInfoArr[i]
            if oldEventInfo.type == type:
            
                # eventInfoArr.splice(i, 1);
                del eventInfoArr[i]
                dispatcher.removeEventListener(oldEventInfo.type, oldEventInfo.listener, oldEventInfo.useCapture)

        if len(eventInfoArr) == 0:
            if dispatcher in ListenerManager.__dispatcherMap:
                del ListenerManager.__dispatcherMap[dispatcher]

    @staticmethod
    def removeEventsForListener(dispatcher:IEventDispatcher, listener:callable) -> None:

        eventInfoArr = ListenerManager.__dispatcherMap.get(dispatcher)

        if eventInfoArr == None: return

        i = len(eventInfoArr)
        while i > 0:
            i -= 1
            oldEventInfo = eventInfoArr[i]
            if oldEventInfo.listener == listener:
            
                # eventInfoArr.splice(i, 1);
                del eventInfoArr[i]
                dispatcher.removeEventListener(oldEventInfo.type, oldEventInfo.listener, oldEventInfo.useCapture)

        if len(eventInfoArr) == 0:
            if dispatcher in ListenerManager.__dispatcherMap:
                del ListenerManager.__dispatcherMap[dispatcher]

    @staticmethod
    def removeEventListeners(dispatcher:IEventDispatcher) -> None:

        eventInfoArr = ListenerManager.__dispatcherMap.get(dispatcher)
        
        if eventInfoArr == None: return

        i = len(eventInfoArr)
        while i > 0:
            i -= 1
            # oldEventInfo = eventInfoArr.splice(i, 1)[0];
            oldEventInfo = eventInfoArr[i]
            del eventInfoArr[i]
            dispatcher.removeEventListener(oldEventInfo.type, oldEventInfo.listener, oldEventInfo.useCapture)
        
        if dispatcher in ListenerManager.__dispatcherMap:
            del ListenerManager.__dispatcherMap[dispatcher]

    @staticmethod
    def printEventTypeList(dispatcher:IEventDispatcher) -> str:

        eventInfoArr = ListenerManager.__dispatcherMap.get(dispatcher)

        if eventInfoArr == None: return None

        # outputStr = (dispatcher as Object).toString() + " --Event type list-- " + "\n"
        outputStr = str(dispatcher) + " --Event type list-- " + "\n"
        i = len(eventInfoArr)
        while i > 0:
            i -= 1
            oldEventInfo = eventInfoArr[i]
            outputStr += "	EventType:" + oldEventInfo.type

            fix = ""
            if i != 0:
                fix = "\n"
            outputStr += fix
        
        return outputStr