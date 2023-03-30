from cn.daftlib.events.EventPhase import EventPhase

class Event:

    # Events
    ACTIVATE:str = "activate"
    ADDED:str = "added"
    ADDED_TO_STAGE:str = "addedToStage"
    CANCEL:str = "cancel"
    CHANGE:str = "change"
    CLEAR:str = "clear"
    CLOSE:str = "close"
    COMPLETE:str = "complete"
    CONNECT:str = "connect"
    CONTEXT3D_CREATE:str = "context3DCreate"
    COPY:str = "copy"
    CUT:str = "cut"
    DEACTIVATE:str = "deactivate"
    ENTER_FRAME:str = "enterFrame"
    EXIT_FRAME:str = "exitFrame"
    FRAME_CONSTRUCTED:str = "frameConstructed"
    FRAME_LABEL:str = "frameLabel"
    FULLSCREEN:str = "fullScreen"
    ID3:str = "id3"
    INIT:str = "init"
    MOUSE_LEAVE:str = "mouseLeave"
    OPEN:str = "open"
    PASTE:str = "paste"
    REMOVED:str = "removed"
    REMOVED_FROM_STAGE:str = "removedFromStage"
    RENDER:str = "render"
    RESIZE:str = "resize"
    SCROLL:str = "scroll"
    SELECT:str = "select"
    SELECT_ALL:str = "selectAll"
    SOUND_COMPLETE:str = "soundComplete"
    TAB_CHILDREN_CHANGE:str = "tabChildrenChange"
    TAB_ENABLED_CHANGE:str = "tabEnabledChange"
    TAB_INDEX_CHANGE:str = "tabIndexChange"
    TEXTURE_READY:str = "textureReady"
    TEXT_INTERACTION_MODE_CHANGE:str = "textInteractionModeChange"
    UNLOAD:str = "unload"

    # public members
    type:str
    bubbles:bool
    cancelable:bool

    eventPhase:EventPhase
    currentTarget:object
    target:object

    # private members
    __isCanceled:bool
    __isCanceledNow:bool
    __preventDefault:bool

    def __init__(self, type:str, bubbles:bool = False, cancelable:bool = False) -> None:
        
        self.type = type
        self.bubbles = bubbles
        self.cancelable = cancelable

        self.eventPhase = EventPhase.AT_TARGET
        self.currentTarget = None
        self.target = None

        self.__isCanceled = False
        self.__isCanceledNow = False
        self.__preventDefault = False

    # def clone(self) -> Event:
    def clone(self):

        event = Event(self.type, self.bubbles, self.cancelable)
        event.eventPhase = self.eventPhase
        event.target = self.target
        event.currentTarget = self.currentTarget
        return event

    def formatToString(self, className:str, p1:str = None, p2:str = None, p3:str = None, p4:str = None, p5:str = None) -> str:

        parameters = []
        if p1: parameters.append(p1)
        if p2: parameters.append(p2)
        if p3: parameters.append(p3)
        if p4: parameters.append(p4)
        if p5: parameters.append(p5)

        return self.__formatToString(className, parameters)

    def __formatToString(self, className:str, parameters:list) -> str:

        output = '[{_className}'.format(_className = className)
        arg = None

        for param in parameters:
            arg = getattr(self, param)
            if type(arg) == str:
                output += ' {_param}="{_arg}"'.format(_param = param, _arg = arg)
            else:
                output += ' {_param}={_arg}'.format(_param = param, _arg = arg)

        output += "]"
        return output

    def toString(self) -> str:

        return self.__formatToString("Event", ["type", "bubbles", "cancelable"])

    def isDefaultPrevented(self) -> bool:

        return self.__preventDefault

    def preventDefault(self) -> None:

        if self.cancelable:
            self.__preventDefault = True

    def stopImmediatePropagation(self) -> None:

        self.__isCanceled = True
        self.__isCanceledNow = True

    def stopPropagation(self) -> None:

        self.__isCanceled = True


    def isCanceled(self) -> bool:
        return self.__isCanceled
    def isCanceledNow(self) -> bool:
        return self.__isCanceledNow