from cn.daftlib.events.Event import Event

class IEventDispatcher:

    # def addEventListener(type:str, listener:function, useCapture:bool = False, useWeakReference:bool = False) -> None:
    def addEventListener(type:str, listener:callable, useCapture:bool = False, useWeakReference:bool = False) -> None:
        pass

    def dispatchEvent(event:Event) -> bool:
        pass

    def hasEventListener(type:str) -> bool:
        pass

    def removeEventListener(type:str) -> None:
        pass

    def willTrigger(type:str) -> bool:
        pass