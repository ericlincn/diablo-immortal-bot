from threading import Timer

class RepeatingTimer(Timer):

    def run(self) -> None:
        
        while not self.finished.is_set():
            self.function(*self.args, **self.kwargs)
            self.finished.wait(self.interval)