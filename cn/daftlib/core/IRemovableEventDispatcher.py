class IRemovableEventDispatcher:

    def removeEventsForType(type:str) -> None:
        pass

    def removeEventsForListener(listener:callable) -> None:
        pass

    def removeEventListeners() -> None:
        pass