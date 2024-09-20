from textSprite import *
import time
import math

class Timer(TextSprite):
    def __init__(self, 
                 position: tuple[int, int] = (0, 0), 
                 width: int = 100, fontSize: int = 10, 
                 fontColor: tuple[int, int, int] = (255, 255, 255), 
                 backColor: tuple[int, int, int] = None, 
                 margin: int = 10) -> None:
        super().__init__('', position=position, width=width, fontSize=fontSize, fontColor=fontColor, backColor=backColor, margin=margin)
        self.start = time.time()
        self.stopped = False




    def update(self, eventList):
        if not self.stopped:
            timeTotal = time.time() - self.start
            minutes = math.floor(timeTotal) // 60
            seconds = timeTotal - minutes * 60
            minutes = f'{minutes}m ' if minutes else ''
            self.setText(f'{minutes}{math.floor(seconds*100)/100}s')

    def restart(self):
        self.stopped = False
        self.start = time.time()
        self.update(None)

    def stop(self):
        self.stopped = True