from cn.daftlib.observer.INotification import INotification

class IObserver:

    def handlerNotification(notification:INotification) -> None:
        pass