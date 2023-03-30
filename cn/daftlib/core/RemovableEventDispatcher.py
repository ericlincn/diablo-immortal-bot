from cn.daftlib.events.EventDispatcher import EventDispatcher
from cn.daftlib.core.IRemovableEventDispatcher import IRemovableEventDispatcher
from cn.daftlib.core.IDestroyable import IDestroyable
from cn.daftlib.events.IEventDispatcher import IEventDispatcher
from cn.daftlib.core.ListenerManager import ListenerManager

class RemovableEventDispatcher(EventDispatcher, IRemovableEventDispatcher, IDestroyable):

    def __init__(self, target: IEventDispatcher = None) -> None:

        super().__init__(target)

    def addEventListener(self, type: str, listener: callable, useCapture: bool = False, priority: int = 0, useWeakReference: bool = False) -> None:
        
        super().addEventListener(type, listener, useCapture, priority, useWeakReference)
        ListenerManager.registerEventListener(self, type, listener, useCapture)

    def removeEventListener(self, type: str, listener: callable, useCapture: bool = False) -> None:
        
        super().removeEventListener(type, listener, useCapture)
        ListenerManager.unregisterEventListener(self, type, listener, useCapture)

    def removeEventsForType(self, type: str) -> None:
        ListenerManager.removeEventsForType(self, type)

    def removeEventsForListener(self, listener: callable) -> None:
        ListenerManager.removeEventsForListener(self, listener)

    def removeEventListeners(self) -> None:
        ListenerManager.removeEventListeners(self)

    def destroy(self) -> None:
        self.removeEventListeners()