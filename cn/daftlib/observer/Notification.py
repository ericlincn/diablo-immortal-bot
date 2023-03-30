from cn.daftlib.observer.INotification import INotification

class Notification(INotification):

    __name:str
    __body:object

    def __init__(self, name:str, body:object) -> None:
        
        self.__name = name
        self.__body = body

    @property
    def name(self) -> str:
        
        return self.__name

    @property
    def body(self) -> object:
        
        return self.__body