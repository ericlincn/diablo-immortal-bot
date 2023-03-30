from cn.daftlib.observer.IObserver import IObserver
from cn.daftlib.observer.Notification import Notification

class NotificationsCenter:

    __observerMap = dict()

    def register(notificationName:str, observer:IObserver) -> None:

        observersArr:list = NotificationsCenter.__observerMap.get(notificationName)
        if observersArr:
            i = len(observersArr)
            while i > 0:
                i -= 1
                if observersArr[i] == observer:
                    return
            observersArr.append(observer)
        else:
            NotificationsCenter.__observerMap[notificationName] = [observer]

    def sendNotification(notificationName:str, data:object) -> None:

        observersArr:list = NotificationsCenter.__observerMap.get(notificationName)
        if observersArr == None: return

        i = 0
        while i < len(observersArr):
            observer:IObserver = observersArr[i]
            callback = observer.handlerNotification
            notification:Notification = Notification(notificationName, data)
            callback(notification)
            i += 1

    def unregisterForNotification(notificationName:str) -> None:
        del NotificationsCenter.__observerMap[notificationName]

    def unregisterForObserver(observer:IObserver) -> None:

        for key in NotificationsCenter.__observerMap:
            observersArr:list = NotificationsCenter.__observerMap[key]

            i = len(observersArr)
            while i > 0:
                i -= 1
                if observersArr[i] == observer:
                    # observersArr.remove(observer)
                    del observersArr[i]

            if len(observersArr) == 0:
                del NotificationsCenter.__observerMap[key]

    def unregister(notificationName:str, observer:IObserver) -> None:
        
        observersArr:list = NotificationsCenter.__observerMap.get(notificationName)
        if observersArr == None: return

        i = len(observersArr)
        while i > 0:
            i -= 1
            if observersArr[i] == observer:
                del observersArr[i]

        if len(observersArr) == 0:
            del NotificationsCenter.__observerMap[notificationName]
